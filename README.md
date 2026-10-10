# Muse 中文 Skill 包

小羽（Muse）的专属 skill 包：**聚焦个人生活场景**，全部为第一方原创、
开箱可用。不收录任何第三方项目链接。

每个 skill 都是一个文件夹，核心是 `SKILL.md`（YAML frontmatter + Markdown 指令），
可选带 `bin/`（可执行工具）、`scripts/`（辅助脚本）、`references/`（按需加载的参考文档）。

## 📦 收录的 Skill

### 🏠 个人生活场景

| Skill | 说明 |
|---|---|
| [life-decision-guide](skills/life-decision-guide/) | 人生决策：按《高性价比人生指南》（CC BY 4.0）正文回答"该不该/值不值/怎么选"，先定位章节、整条读完、按证据等级 A/B/C 排序作答 |
| [moments-display](skills/moments-display/) | 朋友圈展示面：勾魂体配文 7 法则、选图 9 规则、发布运营原则、方法自进化 |
| [email-triage](skills/email-triage/) | 邮箱分拣与定期清理：提醒/噪音/清理三类规则，重要邮件即时提醒、噪音静默、过期验证码定期归档 |
| [video-transcript](skills/video-transcript/) | 视频/音频转带说话人区分的逐字稿：抽音频→faster-whisper 转写→ECAPA 声纹聚类→话轮合并 |

### 🛠️ 技术与开发

| Skill | 说明 | 工具 |
|---|---|---|
| [openrouter](skills/openrouter/) | OpenRouter 统一 API：几百个模型一个 Key 调，支持 chat / 文生图 | `bin/openrouter` |
| [volcengine-ark](skills/volcengine-ark/) | 火山引擎方舟：豆包等模型的统一 API（需先建推理接入点） | `bin/ark` |
| [zhizengzeng](skills/zhizengzeng/) | 智增增 API：SystemOne / Jev 系列模型 | curl 示例 |
| [tencent-map](skills/tencent-map/) | 腾讯位置服务 WebService：中国大陆地址解析、POI 搜索、距离矩阵、驾车路线 | `bin/tencent-map` |
| [x-post-fetch](skills/x-post-fetch/) | X（Twitter）帖子获取：关键词搜索/单帖/评论，官方代理 API | `bin/x_fetch.py` |
| [github-gitdb-push](skills/github-gitdb-push/) | GitHub 推送：走 Git Database API，直调接口完成推送 | `bin/gitdb_push.py` |

## 🚀 安装使用

```bash
# 1. 克隆仓库
git clone https://github.com/juliasadler/muse-skills-cn.git

# 2. 按需取用：把某个 skill 文件夹复制到你的 skills 目录
cp -r muse-skills-cn/skills/openrouter ~/.claude/skills/

# 3. 设置对应环境变量（如 OPENROUTER_API_KEY），即可使用
```

各 skill 的具体用法见其目录下的 `SKILL.md`。

## 🤝 投稿

欢迎提交原创 skill 或改进现有内容，先读 [CONTRIBUTING.md](CONTRIBUTING.md)。
新 skill 可以从 [template-skill](template-skill/) 模板起步。

## 📄 许可证

本仓库全部内容采用 [MIT License](LICENSE)。
