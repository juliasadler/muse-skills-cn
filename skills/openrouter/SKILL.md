---
name: "openrouter"
description: "Use OpenRouter when the user asks for OpenRouter or this provider's API."
---

# OpenRouter

## Purpose

Use OpenRouter (`https://openrouter.ai`) — one API key for hundreds of models.
Use it whenever the user asks for OpenRouter or a specific model served through it.

## Auth

Set the `OPENROUTER_API_KEY` environment variable (get one at
https://openrouter.ai/keys):

```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
```

The CLI never prints, logs, or persists the key. A 401/403 is a question
about the request before it is a question about the key — check that the
header was attached, then verify the key in the OpenRouter dashboard.

## Tooling

CLI: `./bin/openrouter` (Python 3, stdlib only, executable).

- `openrouter check` — verify the key: `GET /api/v1/auth/key` (free, no token spend). Run this first whenever auth is in doubt.
- `openrouter chat --model <slug> --prompt "<text>" [--max-tokens N] [--provider "A,B"] [--quantizations "bf16,fp16"]` — dispatch one chat completion. `--provider` pins the serving provider(s); `--quantizations` filters by precision (use `bf16,fp16` to avoid low-bit "dumbed-down" deployments).
- `openrouter image --model <slug> --prompt "<text>" [--out PATH] [--modalities image,text]` — generate via chat/completions with modalities (for Gemini/GPT image models).
- `openrouter images --model <slug> --prompt "<text>" [--out PATH] [--size 1024x1024]` — generate via `POST /api/v1/images` (for pure image models like qwen-image, seedream, flux that reject chat/completions).

## Operating Rules

1. Use this skill when the user asks for OpenRouter or this provider's API.
2. Restrict authenticated requests to: `openrouter.ai`.
3. Do not print, log, or persist raw credentials.
4. Tip: omit `HTTP-Referer` / `X-Title` headers — some free-tier providers return empty content when they are present.
