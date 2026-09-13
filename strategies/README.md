# Trading Strategies Directory / Trading Strategies

This directory stores **natural language trading strategy files** (YAML format). The system automatically loads all .yaml files in this directory at startup.

For users and documentation, we continue to refer to these capabilities as "strategies"; in code, configuration, and API fields, they are uniformly named as `skill`, which you can understand as a "reusable strategy capability package".

## How to Write Custom Strategies (Strategy Skill)

Simply create a `.yaml` file and describe your trading strategy in Chinese (or any language) — **no coding required**.

### Minimal Template

```yaml
name: my_strategy          # Unique identifier (English, underscore-connected)
display_name: 我的策略      # Display name (Chinese)
description: Brief description of strategy purpose

instructions: |
  Your strategy description...
  Write judgment criteria, entry conditions, exit conditions in natural language.
  You can reference tool names (like get_daily_history, analyze_trend) to guide AI on which data to use.
```

### Complete Template

```yaml
name: my_strategy
display_name: 我的策略
description: Brief description of applicable market scenarios for the strategy

# Strategy category: trend（trend）、pattern（shape）、reversal（reversal）、framework（framework）
category: trend

# Associated core trading concept numbers (1-7), optional
core_rules: [1, 2]

# List of tools required by the strategy, optional
# Available tools: get_daily_history, analyze_trend, get_realtime_quote,
#           get_sector_rankings, search_stock_news, get_stock_info
required_tools:
  - get_daily_history
  - analyze_trend

# Optional aliases (used for /ask and other natural language skill selection)
aliases: [我的战法, 我的模型]

# The following metadata drives default behavior (optional)
# default_active: Whether belongs to default active skill set
# default_router: Whether belongs to routing fallback skill set
# default_priority: Default display/sorting priority, smaller value means higher priority
# market_regimes: Market state labels this strategy preferentially adapts to
default_active: true
default_router: false
default_priority: 100
market_regimes: [trending_up]

# Strategy detailed description (natural language, supports Markdown format)
instructions: |
  **My Strategy Name**

  Judgment Criteria:

  1. **Condition One**:
     - Use `analyze_trend` to check moving average alignment.
     - Describe the trend characteristics you expect to see...

  2. **Condition Two**:
     - Describe volume requirements...

  Score Adjustment:
  - Recommended sentiment_score adjustment when conditions are met
  - Note strategy name in `buy_reason`
```

### Core Trading Concepts Reference

| Number | Concept |
|--------|---------|
| 1 | Strict Entry Strategy: Consider entry only when deviation rate < 5% |
| 2 | Trend Trading: MA5 > MA10 > MA20 bullish alignment |
| 3 | Efficiency First: Volume confirms trend validity |
| 4 | Entry Point Preference: Prioritize pullback to moving average support |
| 5 | Risk Screening: Negative news veto |
| 6 | Volume-Price Matching: Trading volume validates price movement |
| 7 | Uptrend Stock Relaxation: Leading stocks can relax standards appropriately |

## Custom Strategy Directory

In addition to this directory (built-in strategies), you can specify additional custom strategy directories via environment variables:

```env
AGENT_SKILL_DIR=./my_skills
```

The system will load both built-in strategies and custom strategies. If names conflict, custom strategies override built-in ones.

The environment variable name remains `AGENT_SKILL_DIR`, which is the internal unified naming configuration entry; in product semantics, it still represents "custom strategy directory".