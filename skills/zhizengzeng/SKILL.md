---
name: "zhizengzeng"
description: "Use Zhizengzeng when the user asks for Zhizengzeng or this provider's API."
---

# Zhizengzeng （智增增）

## Purpose

Use Zhizengzeng (`https://api.zhizengzeng.com`) — an API relay provider,
notably for the SystemOne / Jev (`jev-1.x`) models. Use it whenever the user
asks for Zhizengzeng or this provider's API.

## Auth

Set the `ZHIZENGZENG_API_KEY` environment variable:

```bash
export ZHIZENGZENG_API_KEY="your-key-here"
```

Never print, log, or persist the key. A 401/403 is a question about the
request before it is a question about the key — check that the credential was
attached, then verify the key with the provider.

## Usage

Zhizengzeng exposes a native SystemOne endpoint:

```
POST https://api.zhizengzeng.com/v1/systemone
```

Example (verify the exact auth placement against the provider's current docs
before relying on it):

```bash
curl -s https://api.zhizengzeng.com/v1/systemone \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ZHIZENGZENG_API_KEY" \
  -d '{"model":"jev-1.13","messages":[{"role":"user","content":"hi"}]}'
```

## Operating Rules

1. Use this skill when the user asks for Zhizengzeng or this provider's API.
2. Restrict authenticated requests to: `api.zhizengzeng.com`.
3. Do not print, log, or persist raw credentials.
