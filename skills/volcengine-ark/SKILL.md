---
name: "volcengine-ark"
description: "Use Volcengine Ark (火山引擎方舟) when the user asks for it or this provider's API."
---

# Volcengine Ark （火山引擎方舟）

## Purpose

Use Volcengine Ark (`https://ark.cn-beijing.volces.com`) — the unified API for
Doubao （豆包） and other models on Volcengine. Use it whenever the user asks
for Volcengine Ark or this provider's API.

## Auth

Set the `VOLCENGINE_ARK_API_KEY` environment variable (get one at
https://console.volcengine.com/ark):

```bash
export VOLCENGINE_ARK_API_KEY="your-key-here"
```

The CLI never prints, logs, or persists the key. A 401/403 is a question about
the request before it is a question about the key — check that the header was
attached, then verify the key in the console.

## Tooling

CLI: `./bin/ark` (Python 3, stdlib only, executable).

- `ark check` — verify the key: `GET /api/v3/models` (free, no token spend). Run this first whenever auth is in doubt.
- `ark chat --model <endpoint-id> --prompt "<text>" [--max-tokens N]` — dispatch one chat completion. `--model` takes the **推理接入点 ID** (`ep-xxxx`), not the public model name — create the endpoint in the console first.

## Operating Rules

1. Use this skill when the user asks for Volcengine Ark or this provider's API.
2. Restrict authenticated requests to: `ark.cn-beijing.volces.com`.
3. Do not print, log, or persist raw credentials.
