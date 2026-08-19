# Quantitative FX Strategy Research Framework

A reusable quantitative trading research and backtesting framework for
systematically testing FX trading strategies and analyzing their performance
through an interactive Dash dashboard.

The current implementation evaluates an **Asian Session Breakout strategy on
EUR/USD**.

The framework is intentionally designed so that the **strategy-specific trading
logic can be changed without rebuilding the surrounding backtesting,
performance-analysis, and visualization framework**.

---

## Overview

This project was developed as a research framework rather than a dashboard
built around a single trading strategy.

The workflow separates:

- Market data
- Data processing
- Strategy logic
- Trade generation
- Backtesting
- Portfolio and equity calculations
- Performance analytics
- Interactive visualization

This allows different systematic trading hypotheses to be tested using the
same research and analytics infrastructure.

### Current Strategy

The current implementation uses an:

**Asian Session Breakout Strategy**

applied to:

**EUR/USD**

The strategy identifies the relevant Asian trading range and evaluates
subsequent price movement for breakout opportunities.

Trades are classified as:

- **LONG / BUY**
- **SHORT / SELL**

The resulting trades are evaluated using profitability, drawdown, win rate,
profit factor, holding time, and other performance metrics.

---

# Research Workflow

The project follows a modular research pipeline:

```text
                 MARKET DATA
                      │
                      ▼
              DATA PROCESSING
                      │
                      ▼
              STRATEGY LOGIC
                      │
                      ▼
              TRADE GENERATION
                      │
                      ▼
                BACKTESTING
                      │
                      ▼
           PORTFOLIO / EQUITY
               CALCULATION
                      │
                      ▼
          PERFORMANCE ANALYTICS
                      │
                      ▼
          INTERACTIVE DASHBOARD
```

The important design principle is that the **strategy logic is separated from
the rest of the research workflow**.

This means the same analytics framework can be reused when testing another
strategy.

---

# What Is Actually Adjustable?

The **strategy-specific Python logic** is the main configurable component of
this project.

In the current `TRADING TEST.ipynb` notebook, the strategy configuration and
logic begins at approximately **line 50**.

This section is where the trading hypothesis is translated into systematic
rules.

The adjustable logic can include:

```text
┌─────────────────────────────────────────┐
│         ADJUSTABLE STRATEGY LOGIC       │
│                                         │
│  Entry conditions                       │
│  Exit conditions                        │
│  BUY / SELL conditions                  │
│  Session definitions                    │
│  Breakout conditions                    │
│  Stop-loss rules                        │
│  Take-profit rules                      │
│  Risk/reward parameters                 │
│  Position sizing                        │
│  Trade timing restrictions              │
│  Signal filters                         │
│  Position direction rules               │
│  Trade rejection conditions             │
└────────────────────┬────────────────────┘
                     │
                     ▼
              Backtesting Engine
                     │
                     ▼
                Trade Results
                     │
                     ▼
            Performance Analytics
                     │
                     ▼
              Dash Dashboard
```

### Changing the Strategy

The surrounding framework does not need to be rebuilt when testing a different
strategy.

For example, the strategy logic could be changed from:

```text
Asian Session Breakout
        ↓
Moving Average Crossover
        ↓
London Session Breakout
        ↓
Momentum Strategy
        ↓
Mean Reversion Strategy
        ↓
Machine Learning Signal Strategy
```

The objective is to make the research framework **strategy-agnostic**, while
allowing the trading hypothesis itself to be changed.

---

# Current Strategy: Asian Session Breakout

The current research implementation evaluates an Asian Session Breakout
strategy on EUR/USD.

The strategy identifies the Asian trading range and evaluates subsequent price
movement for breakout opportunities.

Trades are separated into two directions:

- LONG / BUY
- SHORT / SELL

The backtesting process then evaluates each trade based on its entry,
exit, risk, result, P&L, and effect on portfolio equity.

---

# Research Questions

The framework is designed to investigate questions such as:

- Does the strategy generate positive returns?
- How consistent are returns across different periods?
- What is the maximum drawdown?
- How many trades are profitable?
- How large are the average winning and losing trades?
- Does LONG outperform SHORT?
- Which trade direction contributes most to losses?
- How long are positions typically held?
- How does performance change over time?
- Which months produced stronger or weaker performance?
- Is the strategy sufficiently robust to justify further research?

The dashboard is therefore used not only to display results, but also to support
**strategy diagnosis and decision-making**.

---

# Interactive Dashboard

The project includes an interactive analytics dashboard built with:

- Python
- Dash
- Plotly
- Dash Bootstrap Components
- Pandas

The dashboard consumes the processed outputs generated by the backtesting
workflow and presents them through interactive visualizations.

---

## Dashboard Components

### 1. Strategy Performance KPIs

The dashboard provides a high-level summary of the backtest:

- Ending Balance
- Return
- Win Rate
- Profit Factor
- Maximum Drawdown
- Total Trades

These metrics provide a quick assessment of the strategy's overall
performance.

---

### 2. Long vs Short Performance

The dashboard separately evaluates LONG and SHORT trades.

For each direction, it displays:

- Total Trades
- Profitable Trades
- Losing Trades
- Win Rate
- Total P&L
- Total Losses
- Average Winning Trade
- Average Losing Trade
- Best Trade
- Worst Trade

This allows the strategy to be evaluated beyond its aggregate performance.

For example, a strategy may appear profitable overall while one trade direction
is actually responsible for most of the losses.

---

### 3. Long vs Short Total P&L

A direct comparison of total P&L generated by:

- LONG / BUY trades
- SHORT / SELL trades

This provides a simple view of which direction contributes positively to the
strategy and which direction may be reducing overall performance.

---

### 4. Equity Curve

The equity curve shows how portfolio equity changes throughout the backtest.

It helps visualize:

- Capital growth
- Periods of losses
- Volatility
- Drawdowns
- Recovery periods
- Overall equity progression

---

### 5. P&L by Trade

The P&L-by-trade visualization shows the result of individual trades across
the backtest.

Profitable and losing trades can be compared across the sequence of trades to
identify patterns in trade-level performance.

---

### 6. Drawdown

The drawdown chart shows the percentage decline in equity from a previous
equity peak.

This helps evaluate the risk experienced by the strategy and identify periods
of significant portfolio stress.

---

### 7. Monthly Performance

The monthly performance view shows how ending portfolio balance changes across
the backtest period.

This helps identify:

- Stronger periods
- Weaker periods
- Recovery periods
- Changes in strategy performance over time

---

### 8. Average Holding Time by Direction

The dashboard compares the average holding duration of:

- BUY trades
- SELL trades

This provides additional insight into the behavior of each trade direction.

---

# Current Backtest Results

The current implementation produces the following headline results:

| Metric | Result |
|---|---:|
| Ending Balance | ₹11,934.70 |
| Return | 19.35% |
| Win Rate | 36.32% |
| Profit Factor | 1.13 |
| Maximum Drawdown | -10.52% |
| Total Trades | 223 |

> These results represent the current backtest configuration and should not be
> interpreted as evidence of future trading performance.

---

# Long vs Short Results

The current backtest provides the following directional comparison:

| Metric | LONG / BUY | SHORT / SELL |
|---|---:|---:|
| Total Trades | 110 | 113 |
| Profitable Trades | 45 | 36 |
| Losing Trades | 65 | 77 |
| Win Rate | 40.91% | 31.86% |
| Total P&L | 2,599.37 | -664.57 |
| Total Losses | -6,999.79 | -8,362.67 |
| Average Winner | 213.31 | 213.84 |
| Average Loser | -107.69 | -108.61 |
| Best Trade | 237.22 | 236.38 |
| Worst Trade | -120.98 | -120.55 |

The current results indicate that:

- LONG trades generated positive aggregate P&L.
- SHORT trades generated negative aggregate P&L.
- LONG trades had a higher win rate.
- SHORT trades produced more losing trades.
- The average winning trade was similar for both directions.
- The average losing trade was also similar for both directions.

This makes directional analysis an important part of the research process.

---

# Data Layer

The dashboard uses processed backtesting outputs rather than repeatedly loading
and transforming raw market data throughout the application.

The centralized data layer loads:

- Trade-level results
- Monthly performance summaries
- Directional performance summaries
- Dashboard KPI values

This allows the dashboard components to consume a consistent set of processed
results.

---

# Trade-Level Data

The trade-level output contains information including:

- Trade ID
- Entry time
- Exit time
- Trade type
- Entry price
- Stop loss
- Take profit
- Exit price
- Exit reason
- Result
- P&L
- P&L in pips
- Balance before trade
- Balance after trade
- Risk amount
- R multiple
- Equity
- Equity peak
- Drawdown
- Drawdown percentage
- Holding hours
- Holding days
- Trade month

This trade-level dataset forms the basis of several dashboard
visualizations and performance calculations.

---

# Project Structure

```text
quantitative-fx-strategy-research/
│
├── app/
│   ├── dashboard.py
│   ├── layout.py
│   ├── charts.py
│   ├── styles.py
│   └── data.py
│
├── assets/
│   ├── EURUSD_1H.csv
│   ├── EURUSD_1m.csv
│   ├── EURUSD_3m.csv
│   └── EURUSD_5m.csv
│
├── notebooks/
│   └── TRADING TEST.ipynb
│
├── outputs/
│   ├── trades.csv
│   ├── monthly_summary.csv
│   ├── direction_summary.csv
│   └── dashboard_kpis.json
│
├── calculator.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Reproducible Research Workflow

The intended workflow is:

```text
1. Load market data
        ↓
2. Configure strategy logic
        ↓
3. Run backtest
        ↓
4. Generate trade-level results
        ↓
5. Generate performance summaries
        ↓
6. Export dashboard data
        ↓
7. Launch interactive dashboard
```

This separation allows the research notebook to focus on strategy development
and backtesting while the Dash application focuses on analysis and
visualization.

---

# Technologies

The project uses:

- **Python** — research and backtesting
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical computation
- **Plotly** — interactive visualization
- **Dash** — interactive web dashboard
- **Dash Bootstrap Components** — dashboard layout and UI components
- **Jupyter Notebook** — strategy research and experimentation
- **Matplotlib** — research visualization
- **Git** — version control
- **GitHub** — project versioning and portfolio presentation

---

# Future Research

The framework can be extended to investigate:

- Alternative breakout definitions
- Different trading sessions
- Different stop-loss and take-profit structures
- Risk/reward optimization
- Position-sizing methods
- Additional market filters
- Volatility-based filters
- Time-based trade exits
- Parameter sensitivity
- Walk-forward testing
- Out-of-sample testing
- Transaction costs and spread assumptions
- Multiple FX pairs
- Alternative systematic strategies
- Machine-learning-based signal generation

The purpose of these extensions would be to determine whether observed
performance is robust rather than simply the result of a particular parameter
configuration.

---

# Important Note

This project is a **research and educational framework**, not a financial
advisory system or a guarantee of trading performance.

Historical backtest results do not guarantee future results.

Further research would be required before considering deployment in a live
trading environment, including robustness testing, transaction-cost analysis,
out-of-sample validation, and appropriate risk controls.