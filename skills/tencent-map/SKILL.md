---
name: "tencent-map"
description: "Use Tencent Maps (腾讯位置服务) WebService API: geocoding, reverse geocoding, POI keyword search, distance matrix, and driving route planning in mainland China."
---

# Tencent Maps (腾讯位置服务)

## Purpose

Query Tencent Maps WebService API (`https://apis.map.qq.com`) whenever precise
Chinese addresses, POI search, or road distances / driving routes are needed.

## Auth

Set the `TENCENT_MAP_KEY` environment variable. Create a key at
https://lbs.qq.com/ (QQ/WeChat sign-in): enable **WebServiceAPI** for the key
and allocate quota in the console.

```bash
export TENCENT_MAP_KEY="your-key-here"
```

The CLI attaches the key as the `key` query parameter and never prints, logs,
or persists it. A Tencent `status != 0` is a question about the request before
it is a question about the key. Common statuses: `121` (key missing/denied),
`311` (key not authorized for this API — enable WebServiceAPI on the key),
`348` (quota exhausted — allocate quota in the lbs.qq.com console).

## Tooling

CLI: `./bin/tencent-map` (Python 3, stdlib only, executable).

- `tencent-map check` — verify the key (cheap address-resolve call). Run this first whenever auth is in doubt.
- `tencent-map geocode --address "<地址>"` — address to coordinates.
- `tencent-map reverse --location "<lat,lng>"` — coordinates to address.
- `tencent-map search --keyword "<关键词>" [--location "<lat,lng>" --radius 5000] [--region 北京市] [--page-size 10]` — POI keyword search, nearby or by region.
- `tencent-map distance --from "<lat,lng;lat,lng>" --to "<lat,lng>" --mode driving|walking|bicycling` — distance matrix (returns meters + seconds).
- `tencent-map route --from "<lat,lng>" --to "<lat,lng>"` — driving route plan (distance, duration, taxi fee).

## Operating Rules

1. Use this skill when the user asks for Tencent Maps or this provider's API.
2. Restrict authenticated requests to: `apis.map.qq.com`.
3. Do not print, log, or persist raw credentials.
