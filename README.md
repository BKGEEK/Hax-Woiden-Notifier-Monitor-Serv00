# 📦 Hax & Woiden VPS 库存监控脚本

## 🦊 项目简介

一个轻量级的 Python 脚本，用于监控 **Hax** 和 **Woiden** 免费 VPS 的库存情况。
脚本每分钟自动抓取 `/create-vps` 页面，解析数据中心库存，并通过 **Telegram** 推送库存状态。

* ✅ **有库存时**：推送可用数据中心名称
* ❌ **无库存时**：支持静默模式（可选择不推送）

可部署在 **Serv00 免费主机**。

---

## 📋 功能概览

* 抓取 Hax 和 Woiden 的 VPS 创建页面
* 解析 `<select id="datacenter">` 内的有效选项
* 自动过滤 `-select-` 占位项
* 判断是否有库存，并合并结果为一条消息推送
* 支持自定义监控间隔
* 支持 **静默模式**（无库存不推送）

---

## 📁 文件结构

```
Hax-Woiden-Notifier-Monitor-Serv00/
├─ notifier/        # 静默模式目录
│  └─ bot.py        # 静默模式脚本（无库存时不推送）
├─ monitor/         # 广播模式目录
│  └─ bot.py        # 广播模式脚本（有无库存都会推送）
├─ run.log          # 自动生成的运行日志（由 cron 写入）
├─ README.md        # 使用说明
```

---

## 🧰 环境要求

* Python 3（可运行在 Serv00）

### 安装依赖

```bash
pip install requests beautifulsoup4
```

---

## ⚙️ 配置说明

在 `bot.py` 中修改以下内容：

```python
BOT_TOKEN = "你的 Telegram Bot Token"
CHAT_ID = "你的频道或用户 ID"
```

* 使用 **@BotFather** 创建机器人以获取 `BOT_TOKEN`
* 使用 **@userinfobot** 获取你的 `CHAT_ID` 或频道 ID

---

## 🕒 Serv00 定时任务设置

在 Serv00 面板中添加 **Cron Job**：

### 示例命令

时间自行配置

```bash
bash /usr/local/bin/python3 /usr/home/yourname/yourdirectory/notifier/bot.py >> /usr/home/yourname/yourdirectory/run.log 2>&1
```

> 将路径替换为你实际的脚本目录。

该任务会每分钟运行一次脚本，并将输出写入 `run.log`。

---

## 🔕 静默与广播模式

* **静默模式**：运行 `notifier/bot.py`（无库存时不推送）
* **广播模式**：运行 `monitor/bot.py`（无论有无库存均推送）

---

## 🧪 推送示例

**有库存：**

```
✅ 有 VPS
- Hax: US-OpenVZ-2
- Woiden: EU-1 - Germany - Hetzner - SSD + Dedicated IPv6
```

**无库存（如启用推送）：**

```
❌ 无 VPS
```
