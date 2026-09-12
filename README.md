Here is the translated English version of the `README.md` file, followed by a step-by-step setup guide to get this project running on your own GitHub repository.

---

# English Translation of `README.md`

# 📈 AI Stock Analysis System



> 🤖 An AI Large Language Model-driven stock analysis system covering A-shares, Hong Kong, US, Japanese, Korean, and Taiwan stocks. Automatically analyzes your watchlist daily and sends a "Decision Dashboard" to WeChat Work, Feishu, Telegram, Discord, Slack, or Email.
> 
> 

**[Product Preview](https://www.google.com/search?q=%23-product-preview)** · **[Features](https://www.google.com/search?q=%23-features)** · **[Quick Start](https://www.google.com/search?q=%23-quick-start)** · **[Notification Preview](https://www.google.com/search?q=%23-notification-preview)** · **[Documentation Center](https://www.google.com/search?q=docs/INDEX.md)** · **[Full Guide](https://www.google.com/search?q=docs/full-guide.md)**

[简体中文](https://www.google.com/search?q=README.md) | **English** | [繁體中文](https://www.google.com/search?q=docs/README_CHT.md)

---

## ✨ Features



| Capability | Coverage Details |
| --- | --- |
| **AI Decision Report** | Core conclusions, overall rating, trend analysis, buy/sell price targets, risk alerts, catalysts, and execution checklists.

 |
| **Multi-Market Data Aggregation** | Covers A-shares, HK, US, JP, KR, TW stocks, and ETFs. Includes real-time quotes, K-lines, technical indicators, news, announcements, and fundamentals.

 |
| **Web / Desktop Workbench** | Manual trigger, task progress tracking, historical reports, full Markdown view, backtesting, portfolio management, light/dark mode.

 |
| **Agent Strategy Queries** | Multi-turn conversational Q&A with 15 built-in strategies (Moving Averages, Chan Theory, Wave Theory, Trend, Hot Themes, Event-Driven, Growth, etc.).

 |
| **Smart Import & Autocomplete** | Import via Images, CSV/Excel, or Clipboard; Auto-completes tickers, company names, Pinyin, and aliases.

 |
| **Automation & Push Alerts** | GitHub Actions, Docker, Local Cron, FastAPI service, and direct alerts to WeChat Work, Feishu, Telegram, Discord, Slack, and Email.

 |

---

## 🚀 Quick Start Guide for Your Repository



Below is the step-by-step procedure to set up this system on your GitHub repository using **GitHub Actions** (No server needed, zero cost, 5-minute setup).

### Step 1: Fork or Mirror the Repository



1. Go to the original project repository on GitHub.


2. Click the **Fork** button in the top-right corner to copy the project to your own GitHub account.



---

### Step 2: Configure Environment Secrets



In your newly created repository, navigate to:
`Settings` ➔ `Secrets and variables` ➔ `Actions` ➔ `New repository secret`

You need to add secrets across the following categories:

#### A. AI Model Configuration (At least 1 required)



Add an API Key for your preferred LLM provider:

* `GEMINI_API_KEY`: Google Gemini API Key


* `OPENAI_API_KEY`: OpenAI API Key (or OpenAI-compatible providers like DeepSeek, Qwen)


* `OPENAI_BASE_URL` / `OPENAI_MODEL`: Set these if you are using an OpenAI-compatible endpoint or custom model name.


* `ANTHROPIC_API_KEY`: Anthropic Claude API Key


* `ANSPIRE_API_KEYS` / `AIHUBMIX_KEY`: Supported multi-model aggregator keys.



#### B. Watchlist Configuration (Required)



* Secret Name: **`STOCK_LIST`**

* Value: Comma-separated ticker symbols for the stocks you want to analyze daily.


* *Example:* `AAPL,600519,hk00700,2330.TW,7203.T`




#### C. Notification Channel Configuration (At least 1 required)



Select where you want your daily reports sent:

* **Telegram:** `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`

* **Discord:** `DISCORD_WEBHOOK_URL`

* **Slack:** `SLACK_BOT_TOKEN` and `SLACK_CHANNEL_ID`

* **WeChat Work:** `WECHAT_WEBHOOK_URL`

* **Feishu:** `FEISHU_WEBHOOK_URL`

* **Email:** `EMAIL_SENDER` and `EMAIL_PASSWORD`


#### D. Search & News Sources (Recommended)



To enhance news sentiment and catalyst analysis, add at least one search key:

* `SERPAPI_API_KEYS`, `TAVILY_API_KEYS`, `BRAVE_API_KEYS`, or `BOCHA_API_KEYS`.



---

### Step 3: Enable GitHub Actions



1. Go to the **Actions** tab in your repository.


2. Click the button: **"I understand my workflows, go ahead and enable them"**.



---

### Step 4: Run a Manual Test Execution



1. Under the **Actions** tab, click **"每日股票分析"** (Daily Stock Analysis) on the left sidebar.


2. Click **Run workflow** ➔ **Run workflow**.


3. Wait 1–3 minutes for the run to complete and verify that you receive a notification on your configured channel.



---

### Schedule & Execution Rules



* **Automatic Runs:** The workflow automatically runs every trading day at **18:00 (UTC+8 / Beijing Time)**.


* **Non-Trading Days:** The script automatically checks market schedules (US, HK, A-shares, etc.) and skips analysis on non-trading days/weekends.



---

### Alternative: Local or Docker Setup



If you prefer to run this locally on your machine or inside a Docker container rather than GitHub Actions:

```bash
# 1. Clone your repository
git clone https://github.com/YOUR_USERNAME/daily_stock_analysis.git
cd daily_stock_analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your environment file from the template
cp .env.example .env

# 4. Open .env and insert your API keys and STOCK_LIST
nano .env   # or open in any editor

# 5. Run the stock analysis manually
python main.py

# 6. (Optional) Launch the Web UI Workbench
python main.py --webui

```

Once launched with `--webui`, open `[http://127.0.0.1:8000](http://127.0.0.1:8000)` in your browser to access the interactive web workbench.
