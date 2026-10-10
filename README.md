# Muse 中文 Skill 包：35 个生活场景技巧 + 10 个开箱即用的 Skill

> 内容形式参考 [jasonbitsmith/muse-skills](https://github.com/jasonbitsmith/muse-skills)（一句话痛点 + 三步做法），技巧全部原创，对应本仓库真实可用的 Skill。

小羽（Muse）的专属 skill 包：**聚焦个人生活场景**，第一方原创，开箱可用。
每条技巧都能点开对应的 Skill 直接用。

## 📌 技巧速查

### 🏠 人生决策 · [life-decision-guide](skills/life-decision-guide/)

1. **大事纠结到失眠，该不该做拿不定主意** → ① 把问题原样抛给 skill ② 它去《高性价比人生指南》里定位到具体章节和条目 ③ 按证据等级 A＞B＞C 给你"先做这几条 + 别做这些"的清单，每条带出处
2. **怕被营销号忽悠花冤枉钱** → ① 问"值不值" ② skill 只认证据等级，C 级以下的建议直接告诉你别当结论用 ③ 有"争议"标注的条目会把反方证据也摆出来
3. **政策类问题怕过时（补贴/报销/时限）** → ① skill 会带上书里写的截至日期 ② 明确提醒你去官方渠道二次确认 ③ 不拿旧数字当现行政策
4. **帮朋友做决定怕好心办坏事** → ① 按受益人四档拆开写（自己/家人/朋友/陌生人） ② 写到"替人担保、帮人转账"这种，风险面和好处一起列 ③ 只给方向，不替对方拍板

### 📸 朋友圈展示面 · [moments-display](skills/moments-display/)

5. **朋友圈发了没人点赞评论** → ① 按选图 9 规则重组：张数取 1/4/9、色调统一 ② 九宫格用 2 环境 + 2 美食 + 5 人像公式 ③ 最出彩的一张放中心
6. **文案总写成"报菜名"（茶刚倒好月饼还没动）** → ① 套勾魂体：只给入口不给答案 ② 用画面代替道理，写感受不写物品清单 ③ 词穷就堆自然意象：月亮/风/光/树
7. **想立人设但不想用力过猛** → ① 不晒努力晒状态，说从容不说累 ② 高级感 = 有生活有状态，不晒奢侈品 ③ 证书奖项自然入镜，一学期一条封顶
8. **旧照片想发又怕穿帮** → ① 文案禁用"今天"等时效词 ② 被问就大方承认拍摄时间 ③ 新旧照片穿插发，别扎堆

### 📧 邮箱分拣 · [email-triage](skills/email-triage/)

9. **邮箱爆了，重要邮件总被淹没** → ① 按三类规则分拣：提醒 / 噪音 / 清理 ② 工作邮件、账单、待办通知命中立刻推给你 ③ 促销简报直接静默
10. **验证码邮件堆成山** → ① 每周自动清理 7 天前的验证码 ② 只移回收站、不永久删 ③ 购买收据、安全提醒类自动避开
11. **怕 AI 手滑发出不该发的回复** → ① 回复只存草稿 ② 发送前必须展示收件人 + 主题 + 正文等你点头 ③ 邮件里的链接绝不自动点
12. **好几个邮箱来回切** → ① 规则一次配置，多邮箱自动覆盖 ② 每天早 8 点收一份汇总 ③ 30 分钟扫一次，有事才打扰你

### 🎙️ 视频转逐字稿 · [video-transcript](skills/video-transcript/)

13. **2 小时会议录音没人愿意整理** → ① 丢给 skill ② faster-whisper 转写 + 声纹聚类分说话人 ③ 输出"时间戳 + 说话人 + 整段话"的逐字稿
14. **访谈里多人分不清谁说了啥** → ① 按说话人数设置聚类数 ② 同一人连续发言自动合并成一段 ③ 名字是推断的会明确标注，对不上你纠正
15. **谐音字转写总翻车** → ① 正式用途换 medium/large 模型 ② 或人工校一遍 ③ 小模型只适合先听个大概
16. **转写环境总配不好** → ① 按 skill 里的清单装（faster-whisper 等） ② 记住两个坑：PyAV 锁 18.x、no_proxy 别带方括号写法 ③ 配好一次一直用

### 🤖 OpenRouter · [openrouter](skills/openrouter/)

17. **想一个 Key 玩遍几百个大模型** → ① 去 OpenRouter 领 Key ② 设环境变量 ③ `chat --model` 直接换模型名调用
18. **免费模型总遇到降智版** → ① `--quantizations bf16,fp16` 过滤低精度部署 ② `--provider` 锁定靠谱服务商 ③ 先 `check` 确认 Key 有效再跑
19. **想用 AI 生图又不想开一堆会员** → ① `image` 走多模态接口 ② 纯生图模型用 `images` 走专用接口 ③ 图自动存本地、文件名带时间戳
20. **跑一半报错先别怪 Key** → ① 401/403 先检查请求头带没带 Key ② 确认 Key 在后台有效 ③ 再考虑换模型/供应商

### 🔥 火山方舟 · [volcengine-ark](skills/volcengine-ark/)

21. **想在国内稳定调用豆包** → ① 控制台领 Key ② 设环境变量 ③ `ark check` 免费验证连通性
22. **chat 报模型不存在** → ① 方舟的 `--model` 填的是推理接入点 ID（ep- 开头） ② 不是公开模型名 ③ 先去控制台建接入点再调

### 🗺️ 腾讯地图 · [tencent-map](skills/tencent-map/)

23. **地址转坐标总对不上** → ① `geocode --address` 一键解析 ② 返回经纬度 + 行政区划 ③ 先 `check` 确认 Key 开了 WebServiceAPI 权限
24. **想找附近的店/设施** → ① `search --keyword` ② 加 `--location` 做周边搜、或 `--region` 按城市搜 ③ 结果带电话和分类
25. **算两地开车要多久** → ① `distance --mode driving` ② 返回米数 + 秒数 ③ 步行/骑行换 `--mode` 就行
26. **规划驾车路线** → ① `route --from --to` ② 返回距离、时长、预估打车费 ③ 常见报错：311 = 没开 WebServiceAPI，348 = 额度用完

### 🧠 智增增 · [zhizengzeng](skills/zhizengzeng/)

27. **想调用 Jev 系列模型** → ① 拿 Key 设环境变量 ② 按 skill 里的模板调 `/v1/systemone` ③ 先对着官方文档确认认证位置
28. **401 先别急着换 Key** → ① 检查请求里 Key 带没带上 ② 确认 Key 在服务商后台有效 ③ 再排查模型名

### 🐦 X 帖子获取 · [x-post-fetch](skills/x-post-fetch/)

29. **想看 X 上某个话题在聊啥** → ① 设 `TWITTERAPI_IO_KEY` ② `search "关键词"` ③ 输出统一字段：正文/作者/点赞/转发
30. **看到一条帖子想看评论区** → ① `replies <帖子ID或链接>` ② ID 和链接都认 ③ `--limit` 控制条数
31. **免费额度别浪费** → ① 注意有效期（一般 30 天） ② 控制频率，免费 tier QPS 很低 ③ 先小批量试通再批量跑

### 💾 GitHub 推送 · [github-gitdb-push](skills/github-gitdb-push/)

32. **SSH 推不动、只有 token** → ① 设 `GITHUB_TOKEN` ② 一条命令走 Git Database API 全量推送 ③ 自动跳过 `.git`
33. **怕推送覆盖别人的提交** → ① 脚本先拉远端 ref ② 新 commit 认远端为父提交 ③ 非快进直接报错、不硬推
34. **推完不放心** → ① 自动回读远端 tree ② 逐文件比对清单 ③ 对不上直接报错
35. **文本文件推送乱码** → ① 别用野路子传 base64 ② 走正规 blob 接口（`content` + `encoding: base64`） ③ Python 内做编解码，文件保持原文 UTF-8

## 📦 Skill 包（10 个）

| Skill | 说明 | 工具 |
|---|---|---|
| [openrouter](skills/openrouter/) | OpenRouter 统一 API：几百个模型一个 Key 调，支持 chat / 文生图 | `bin/openrouter` |
| [volcengine-ark](skills/volcengine-ark/) | 火山引擎方舟：豆包等模型的统一 API（需先建推理接入点） | `bin/ark` |
| [zhizengzeng](skills/zhizengzeng/) | 智增增 API：SystemOne / Jev 系列模型 | curl 示例 |
| [tencent-map](skills/tencent-map/) | 腾讯位置服务 WebService：中国大陆地址解析、POI 搜索、距离矩阵、驾车路线 | `bin/tencent-map` |
| [x-post-fetch](skills/x-post-fetch/) | X（Twitter）帖子获取：关键词搜索/单帖/评论，官方代理 API | `bin/x_fetch.py` |
| [github-gitdb-push](skills/github-gitdb-push/) | GitHub 推送：走 Git Database API，直调接口完成推送 | `bin/gitdb_push.py` |
| [life-decision-guide](skills/life-decision-guide/) | 人生决策：按《高性价比人生指南》（CC BY 4.0）正文作答 | — |
| [moments-display](skills/moments-display/) | 朋友圈展示面：配文 7 法则、选图 9 规则、运营原则 | — |
| [email-triage](skills/email-triage/) | 邮箱分拣与定期清理：提醒/噪音/清理三类规则 | — |
| [video-transcript](skills/video-transcript/) | 视频/音频转带说话人区分的逐字稿 | `scripts/diarize_transcribe.py` |

> 认证方式：统一用环境变量（如 `OPENROUTER_API_KEY`），脚本绝不打印、记录或落盘原始凭证。

## 🚀 安装使用

```bash
# 1. 克隆仓库
git clone https://github.com/juliasadler/muse-skills-cn.git

# 2. 按需取用：把某个 skill 文件夹复制到你的 skills 目录
cp -r muse-skills-cn/skills/openrouter ~/.claude/skills/

# 3. 设置对应环境变量（如 OPENROUTER_API_KEY），即可使用
```

各 skill 的具体用法见其目录下的 `SKILL.md`，新 skill 可从 [template-skill](template-skill/) 模板起步。

## 🤝 投稿

欢迎提交原创 skill 或改进现有内容，先读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

本仓库原创内容采用 [MIT License](LICENSE)。
