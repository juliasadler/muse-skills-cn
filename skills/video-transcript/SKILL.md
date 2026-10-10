---
name: video-transcript
description: 把视频链接或音频文件转成带说话人区分的逐字稿。链路：下载→抽音频→faster-whisper 转写→ECAPA 声纹聚类分说话人→话轮合并。
---

# 视频转逐字稿（标准流程）

把录音或视频链接转成文字稿，统一按以下样式和流程处理。

## 一、固定输出样式

```
[00:00:00] 说话人A：同一人连续说的完整的一段话……
[00:00:05] 说话人B：另一人接的完整的一段话……
```

规则：

- **每话轮只记一个开始时间戳**（`[HH:MM:SS]`），不逐句打时间戳；
- **必须区分说话人**（声纹聚类自动分，名字按内容推断后须经用户确认）；
- **同一说话人连续说的内容合并为一段完整的话**，不要碎成短句。

## 二、流程（按顺序执行）

### 1. 获取音频

- **B 站**：网页接口有 412 风控，yt-dlp 直连失败时改走 `api.bilibili.com` 的 view/playurl 接口拿直链下载：
  ```bash
  # 先拿 aid/cid
  # https://api.bilibili.com/x/web-interface/view?bvid=BVxxxx
  # 再拿直链
  # https://api.bilibili.com/x/player/playurl?avid=xxx&cid=xxx&qn=64
  ```
- **油管**：机房 IP 会被 bot 验证拦截（"Sign in to confirm you're not a bot"），需用户提供登录 cookies 后再下载。
- **抖音**：需 fresh cookies；拿不到时请用户直接在 App 里保存视频发文件过来。
- **本地音频/视频文件**：直接用。

### 2. 抽音频（统一转 16kHz 单声道 wav）

```bash
ffmpeg -y -i 输入.mp4 -vn -ar 16000 -ac 1 -c:a pcm_s16le 音频.wav
```

### 3. 转写 + 说话人分离 + 话轮合并（一键脚本）

```bash
python scripts/diarize_transcribe.py 音频.wav --speakers 2 --names "说话人1,说话人2" --out 逐字稿.txt
```

- `--speakers`：说话人数（访谈一般为 2）；
- `--names`：可选，名字顺序对应聚类标签 0,1,…；不填则输出"说话人A/B"；
- 脚本逻辑：faster-whisper 转写 → 每个片段提 ECAPA 声纹 embedding → 余弦聚类分说话人 → 连续同说话人片段合并为话轮。

### 4. 质检后交付

- small 模型有少量谐音误识别（如"太干货"→"太干活"），正式用途换 medium/large 模型或人工校一遍；
- 说话人名字为内容推断时，必须在交付时说明"名字是推断的，对不上请纠正"。

## 三、环境准备

需要 Python 环境，安装：

```bash
pip install faster-whisper speechbrain scikit-learn scipy soundfile
```

系统工具：`ffmpeg`、`yt-dlp`。

### 两个必记的坑

1. **PyAV 必须 `<19`**：PyAV 19.0.0 删掉了 `av.open()` 的 `metadata_errors` 参数，faster-whisper 1.2.1 仍在传它，会报 `TypeError`。固定安装 `av==18.1.0`，不要升级。
2. **模型下载时 httpx 报 `Invalid port`**：如果本机 `no_proxy` 环境变量含 `[::1]` 方括号写法，huggingface_hub 解析不了。运行时覆盖：
   ```bash
   no_proxy="localhost,127.0.0.1" NO_PROXY="localhost,127.0.0.1" python scripts/diarize_transcribe.py ...
   ```

## 四、可选加速（云端 ASR）

本地转写吃 CPU/耗时较长时，可考虑云端 ASR 替代（按各自免费额度政策）：

- **硅基流动 SenseVoiceSmall**：免费、OpenAI 兼容接口、中文识别强，适合替换本地转写；
- **腾讯云语音识别**：新用户有免费资源包额度。

接入时做好"额度用尽降级回本地 faster-whisper"的兜底。
