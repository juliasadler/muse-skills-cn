---
name: "github-gitdb-push"
description: "SSH 被墙/只有 API token 时推送 GitHub：走 Git Database API（建 blob→组 tree→建 commit→更新 ref），推送前先拉远端、禁止盲推、推完回读验证。"
---

# GitHub 推送（Git Database API 直调）

适用于：SSH 不可用、只有 API token 的环境。
全程走 `https://api.github.com`，不依赖 git 协议。

## 铁律

1. **推送前必须先拉取远端新版**，三方比对，禁止盲推（盲推会覆盖/误删他人提交）；
2. **文本文件禁止传 base64 原样入库的野路子**——用正规 blob 接口（`content` + `encoding: base64`），Python 内做编解码，文件保持原文 UTF-8；
3. **推完必须回读验证**：读回远端 tree，确认文件清单一致、首行与正文可读。

## 流程

```
1. GET  /repos/{owner}/{repo}/git/ref/heads/{branch}   → 拿到 base commit
2. POST /repos/{owner}/{repo}/git/blobs                → 每个文件建 blob（base64）
3. POST /repos/{owner}/{repo}/git/trees                 → 用 base_tree + blobs 组新 tree
4. POST /repos/{owner}/{repo}/git/commits               → 建 commit（parents=[base]）
5. PATCH /repos/{owner}/{repo}/git/refs/heads/{branch}  → 更新分支指向新 commit
```

认证：请求头 `Authorization: Bearer <token>`（classic PAT 需 `repo` 权限）。
token 只放环境变量 `GITHUB_TOKEN`，绝不写进代码和日志。

## 工具

`./bin/gitdb_push.py`（Python 3，stdlib only）：

```bash
export GITHUB_TOKEN="ghp_..."
./bin/gitdb_push.py --owner <owner> --repo <repo> --dir <本地目录> [--branch main] \
  --message "提交说明"
```

- 只推送 `--dir` 下的文件（自动跳过 `.git/`）；
- 可执行文件（`bin/` 下）自动用 `100755` mode，其余 `100644`；
- 推送后自动回读远端 tree 做文件清单校验，不一致则报错。

## 多人协作补充

- 远端有新提交时：先 `GET` 最新 ref，以它为 base 重组 tree 再推；
- 远端删除了文件：不自动跟删本地，一律先上报人工确认。
