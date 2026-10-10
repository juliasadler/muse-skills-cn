---
name: "x-post-fetch"
description: "获取 X（Twitter）帖子内容：关键词搜索、单帖读取、评论读取。双通道：TwitterAPI.io（API Key）为主，twikit（小号 cookie）为备，统一输出字段。"
---

# X 帖子获取（双通道）

## 通道

| 通道 | 凭证 | 说明 |
|---|---|---|
| TwitterAPI.io（主） | `TWITTERAPI_IO_KEY` 环境变量，请求头 `X-API-Key` | 官方代理 API，按量计费，有免费额度；HTTP 头大小写不敏感 |
| twikit（备） | X 小号的 `auth_token` + `ct0` cookie | 需在小号浏览器 DevTools 提取；免费但有风控风险 |

**策略**：优先主通道；主通道无凭证或失败时自动切备用通道。

## TwitterAPI.io 接口

Base: `https://api.twitterapi.io`

```bash
# 关键词搜索
curl -s "https://api.twitterapi.io/twitter/tweet/advanced_search?query=<关键词>&queryType=Latest" \
  -H "X-API-Key: $TWITTERAPI_IO_KEY"

# 单帖读取
curl -s "https://api.twitterapi.io/twitter/tweets?tweet_ids=<id>" \
  -H "X-API-Key: $TWITTERAPI_IO_KEY"

# 评论读取
curl -s "https://api.twitterapi.io/twitter/tweet/replies/v2?tweetId=<id>" \
  -H "X-API-Key: $TWITTERAPI_IO_KEY"
```

## 统一输出字段

无论走哪个通道，归一化为：`id / text / user / screen_name / created_at / likes / rts / replies / url`。

## 工具

`./bin/x_fetch.py`（Python 3，stdlib only）：TwitterAPI.io 通道的最小可用客户端。

```bash
export TWITTERAPI_IO_KEY="your-key"
./bin/x_fetch.py search "关键词" --limit 20
./bin/x_fetch.py tweet <帖子ID或链接>
./bin/x_fetch.py replies <帖子ID> --limit 20
```

## 注意事项

- 免费额度有有效期（如 30 天），注意在到期前用完；
- 控制请求频率，免费 tier QPS 很低（如 0.2）；
- twikit 通道用小号 cookie，不要用主力账号，避免风控连带。
