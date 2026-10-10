#!/usr/bin/env python3
"""X 帖子获取：TwitterAPI.io 通道最小客户端（搜索 / 单帖 / 评论）。

Auth: export TWITTERAPI_IO_KEY="your-key"
Docs: https://twitterapi.io
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.parse
import urllib.request
import urllib.error

BASE = "https://api.twitterapi.io"


def _key() -> str:
    k = os.environ.get("TWITTERAPI_IO_KEY", "").strip()
    if not k:
        raise SystemExit("TWITTERAPI_IO_KEY is not set.")
    return k


def _get(path: str, params: dict) -> dict:
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("X-API-Key", _key())
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:300]
        raise SystemExit(f"HTTP {e.code}: {body}")


def _norm(t: dict) -> dict:
    a = t.get("author") or {}
    return {
        "id": str(t.get("id")),
        "text": t.get("text"),
        "user": a.get("name"),
        "screen_name": a.get("userName"),
        "created_at": t.get("createdAt"),
        "likes": t.get("likeCount"),
        "rts": t.get("retweetCount"),
        "replies": t.get("replyCount"),
        "url": t.get("url") or f"https://x.com/i/status/{t.get('id')}",
    }


def _tweet_id(url_or_id: str) -> str:
    m = re.search(r"(?:status/)(\d+)", url_or_id)
    return m.group(1) if m else url_or_id.strip()


def cmd_search(args):
    d = _get("/twitter/tweet/advanced_search",
             {"query": args.keyword, "queryType": "Latest"})
    tweets = d.get("tweets") or []
    out = [_norm(t) for t in tweets[: args.limit]]
    print(json.dumps({"provider": "twitterapi.io", "tweets": out},
                     ensure_ascii=False, indent=2))


def cmd_tweet(args):
    tid = _tweet_id(args.id)
    d = _get("/twitter/tweets", {"tweet_ids": tid})
    tweets = d.get("tweets") or []
    if not tweets:
        raise SystemExit("tweet not found")
    print(json.dumps({"provider": "twitterapi.io", "tweet": _norm(tweets[0])},
                     ensure_ascii=False, indent=2))


def cmd_replies(args):
    tid = _tweet_id(args.id)
    d = _get("/twitter/tweet/replies/v2", {"tweetId": tid})
    tweets = d.get("tweets") or []
    out = [_norm(t) for t in tweets[: args.limit]]
    print(json.dumps({"provider": "twitterapi.io", "tweets": out},
                     ensure_ascii=False, indent=2))


def main():
    p = argparse.ArgumentParser(prog="x_fetch")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="关键词搜索")
    s.add_argument("keyword")
    s.add_argument("--limit", type=int, default=20)

    t = sub.add_parser("tweet", help="单帖读取")
    t.add_argument("id", help="帖子 ID 或链接")

    r = sub.add_parser("replies", help="评论读取")
    r.add_argument("id", help="帖子 ID 或链接")
    r.add_argument("--limit", type=int, default=20)

    a = p.parse_args()
    {"search": cmd_search, "tweet": cmd_tweet, "replies": cmd_replies}[a.cmd](a)


if __name__ == "__main__":
    main()
