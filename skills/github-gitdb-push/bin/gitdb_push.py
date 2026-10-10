#!/usr/bin/env python3
"""GitHub push via Git Database API (for environments where SSH is blocked).

Auth: export GITHUB_TOKEN="ghp_..." (classic PAT with `repo` scope).

Usage:
    gitdb_push.py --owner <owner> --repo <repo> --dir <local-dir>
                  [--branch main] --message "commit message"

Rules enforced:
  - pulls the remote ref first (no blind pushes; new commit parents the base)
  - verifies after push by reading back the remote tree and comparing file lists
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import urllib.request
import urllib.error

API = "https://api.github.com"


def _token() -> str:
    t = os.environ.get("GITHUB_TOKEN", "").strip()
    if not t:
        raise SystemExit("GITHUB_TOKEN is not set.")
    return t


def _api(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(API + path, data=data, method=method)
    req.add_header("Authorization", f"Bearer {_token()}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:300]
        raise SystemExit(f"{method} {path} -> HTTP {e.code}: {body}")


def main() -> None:
    ap = argparse.ArgumentParser(prog="gitdb_push")
    ap.add_argument("--owner", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--dir", required=True, help="local directory to push")
    ap.add_argument("--branch", default="main")
    ap.add_argument("--message", required=True)
    a = ap.parse_args()
    base = f"/repos/{a.owner}/{a.repo}"
    local_dir = os.path.abspath(os.path.expanduser(a.dir))

    # 1. pull remote ref first (no blind push)
    try:
        ref = _api("GET", f"{base}/git/ref/heads/{a.branch}")
        parents = [ref["object"]["sha"]]
        base_tree = _api("GET", f"{base}/git/commits/{parents[0]}")["tree"]["sha"]
        print(f"remote {a.branch} at {parents[0][:7]}")
    except SystemExit as e:
        if "HTTP 404" in str(e):
            parents, base_tree = [], None
            print(f"remote branch {a.branch} does not exist yet; creating")
        else:
            raise

    # 2. collect files
    files = []
    for root, dirs, names in os.walk(local_dir):
        if ".git" in dirs:
            dirs.remove(".git")
        for n in sorted(names):
            p = os.path.join(root, n)
            files.append((os.path.relpath(p, local_dir), p))
    if not files:
        raise SystemExit("nothing to push: empty directory")

    # 3. blobs
    tree = []
    for rel, p in files:
        with open(p, "rb") as f:
            raw = f.read()
        b = _api("POST", f"{base}/git/blobs",
                 {"content": base64.b64encode(raw).decode(), "encoding": "base64"})
        mode = "100755" if (os.access(p, os.X_OK) and "/bin/" in rel) else "100644"
        tree.append({"path": rel, "mode": mode, "type": "blob", "sha": b["sha"]})
    print(f"blobs: {len(tree)}")

    # 4. tree + commit
    tp = {"tree": tree}
    if base_tree:
        tp["base_tree"] = base_tree
    t = _api("POST", f"{base}/git/trees", tp)
    c = _api("POST", f"{base}/git/commits",
             {"message": a.message, "tree": t["sha"], "parents": parents})

    # 5. update ref
    if parents:
        _api("PATCH", f"{base}/git/refs/heads/{a.branch}", {"sha": c["sha"]})
    else:
        _api("POST", f"{base}/git/refs",
             {"ref": f"refs/heads/{a.branch}", "sha": c["sha"]})
    print(f"pushed {c['sha'][:7]} to {a.branch}")

    # 6. verify: read back remote tree
    rt = _api("GET", f"{base}/git/trees/{c['sha']}?recursive=1")
    pushed = sorted(x["path"] for x in rt["tree"] if x["type"] == "blob")
    local = sorted(rel for rel, _ in files)
    if pushed != local:
        raise SystemExit(f"VERIFY FAILED: diff={set(local) ^ set(pushed)}")
    print(f"verified: {len(pushed)} files match")


if __name__ == "__main__":
    main()
