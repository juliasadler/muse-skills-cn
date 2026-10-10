---
name: "x-post-fetch"
description: "通过官方代理 API 获取 X（Twitter）帖子内容：关键词搜索、单帖读取、评论读取，统一输出字段。"
---

# X 帖子获取（TwitterAPI.io）

走官方代理 API，不碰任何非官方抓取手段。

## 认证

`TWITTERAPI_IO_KEY` 环境变量，请求头 `X-API-Key`（HTTP 头大小写不敏感）：

```bash
export TWITTERAPI_IO_KEY="your-key"
```

## 接口

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

`id / text / user / screen_name / created_at / likes / rts / replies / url`。

## 工具

`./bin/x_fetch.py`（Python 3，stdlib only）：

```bash
export TWITTERAPI_IO_KEY="your-key"
./bin/x_fetch.py search "关键词" --limit 20
./bin/x_fetch.py tweet <帖子ID或链接>
./bin/x_fetch.py replies <帖子ID> --limit 20
```

## 注意事项

- 免费额度有有效期（如 30 天），注意在到期前用完；
- 控制请求频率，免费 tier QPS 很低（如 0.2）。
