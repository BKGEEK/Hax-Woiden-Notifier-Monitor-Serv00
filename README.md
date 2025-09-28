# 📦Hax & Woiden VPS库存监控脚本

## 🦊 项目简介
这是一个用于监控 Hax 和 Woiden 免费 VPS 库存的轻量级 Python 脚本。 脚本每分钟自动抓取 /create-vps 页面，解析数据中心库存，并通过 Telegram 推送库存状态。

✅ 有库存时：发送数据中心名称

❌ 无库存时：可选是否静默不提示

支持部署在 Serv00 免费主机



## 📋 功能概览
抓取 Hax 和 Woiden 的 VPS 创建页面

解析 <select id="datacenter"> 中的有效选项

判断是否有库存（排除 -select- 占位项）

合并结果为一条 Telegram 消息推送

可配置自定义时长监控一次

支持静默模式（无库存时不推送）



## 📁 文件结构
代码
hax-woiden/
├─ bot.py           # 主脚本：抓取库存并推送 Telegram
├─ run.log          # 自动生成的运行日志（由 cron 写入）
├─ README.md        # 使用说明



## 🧰 环境要求
Python 3（Sev00 这次）

### 安装依赖：

pip install requests beautifulsoup4



## ⚙️ 配置说明
在 bot.py 中设置以下内容：

BOT_TOKEN = "你的 Telegram Bot Token"
CHAT_ID = "你的频道或用户 ID"
你可以通过 @BotFather 创建机器人，并获取 BOT_TOKEN。 使用 @userinfobot 获取你的 CHAT_ID 或频道 ID。



## 🕒 Serv00 定时任务设置（FreeBSD）
在 Serv00 面板中添加 Cron Job：

### 时间设置：

自行看面板设置

## 命令填写：

bash /usr/local/bin/python3 /usr/home/yourname/yourdirectory/bot.py >> /usr/home/yourname/yourdirectory/run.log 2>&1
这将每分钟运行一次脚本，并将输出写入 run.log。



## 🔕 静默或广播模式

### 静默模式：

下载notifier目录下的bot.py

### 广播模式：

下载monitor目录下的bot.py



## 🧪 示例推送格式
有库存：

✅ 有VPS
- Hax: US-OpenVZ-2
- Woiden: EU-1-Germany OpenVZ Hetzner SSD Dedicated IPv6

无库存（如启用）：

❌ 无VPS
