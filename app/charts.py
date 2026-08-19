# =============================================================================
# CHARTS
# =============================================================================

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from data import (
    trades_df,
    monthly_summary,
    direction_summary
)

from styles import (
    CARD,
    TEXT,
    SUBTEXT,
    GRID,
    PRIMARY,
    SUCCESS,
    DANGER
)


# =============================================================================
# EQUITY CURVE
# =============================================================================

def create_equity_curve():

    df = trades_df.copy()

    df["exit_time"] = pd.to_datetime(
        df["exit_time"],
        errors="coerce"
    )

    df = df.sort_values("exit_time")

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["exit_time"],

            y=df["equity"],

            mode="lines",

            name="Equity",

            line=dict(
                color=PRIMARY,
                width=3
            ),

            fill="tozeroy",

            fillcolor="rgba(59,130,246,0.10)"

        )

    )

    fig.update_layout(

        title="Equity Curve",

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        margin=dict(
            l=50,
            r=30,
            t=60,
            b=40
        ),

        xaxis=dict(
            title="Trade Exit Time",
            gridcolor=GRID
        ),

        yaxis=dict(
            title="Equity",
            gridcolor=GRID
        ),

        hovermode="x unified"

    )

    return fig


# =============================================================================
# P&L BY TRADE
# =============================================================================

def create_pnl_chart():

    df = trades_df.copy()

    df["trade_number"] = range(1, len(df) + 1)

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=df["trade_number"],

            y=df["pnl"],

            name="P&L",

            marker_color=[
                SUCCESS if x >= 0 else DANGER
                for x in df["pnl"]
            ]

        )

    )

    fig.update_layout(

        title="P&L by Trade",

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        margin=dict(
            l=50,
            r=30,
            t=60,
            b=40
        ),

        xaxis=dict(
            title="Trade Number",
            gridcolor=GRID
        ),

        yaxis=dict(
            title="P&L",
            gridcolor=GRID
        )

    )

    return fig


# =============================================================================
# DRAWDOWN
# =============================================================================

def create_drawdown_chart():

    df = trades_df.copy()

    df["exit_time"] = pd.to_datetime(
        df["exit_time"],
        errors="coerce"
    )

    df = df.sort_values("exit_time")

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["exit_time"],

            y=df["drawdown_pct"],

            mode="lines",

            name="Drawdown",

            line=dict(
                color=DANGER,
                width=2
            ),

            fill="tozeroy",

            fillcolor="rgba(239,68,68,0.12)"

        )

    )

    fig.update_layout(

        title="Drawdown",

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        margin=dict(
            l=50,
            r=30,
            t=60,
            b=40
        ),

        xaxis=dict(
            title="Trade Exit Time",
            gridcolor=GRID
        ),

        yaxis=dict(
            title="Drawdown (%)",
            gridcolor=GRID
        )

    )

    return fig


# =============================================================================
# MONTHLY P&L
# =============================================================================

def create_monthly_pnl():

    df = monthly_summary.copy()

    fig = px.bar(

        df,

        x=df.columns[0],

        y=df.columns[-1],

        title="Monthly ending balance"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        xaxis=dict(
            gridcolor=GRID
        ),

        yaxis=dict(
            gridcolor=GRID
        )

    )

    return fig


# =============================================================================
# TRADE DIRECTION
# =============================================================================

def create_direction_chart():

    df = direction_summary.copy()

    fig = px.bar(

        df,

        x=df.columns[0],

        y=df.columns[-1],

        title="Average Holding Time by Direction"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        xaxis=dict(
            gridcolor=GRID
        ),

        yaxis=dict(
            gridcolor=GRID
        )

    )

    return fig


# =============================================================================
# LONG vs SHORT TOTAL P&L
# =============================================================================

def create_direction_pnl_chart():

    df = trades_df.copy()

    df["direction"] = df["trade_type"].astype(str).apply(

        lambda x:
            "Long / Buy"
            if "buy" in x.lower()
            else "Short / Sell"
            if "sell" in x.lower()
            else x

    )

    direction_pnl = (

        df.groupby("direction")["pnl"]
        .sum()
        .reset_index()

    )

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=direction_pnl["direction"],

            y=direction_pnl["pnl"],

            marker_color=[

                SUCCESS if value >= 0 else DANGER

                for value in direction_pnl["pnl"]

            ],

            text=[

                f"{value:,.2f}"

                for value in direction_pnl["pnl"]

            ],

            textposition="outside",

            name="Total P&L"

        )

    )

    fig.update_layout(

        title="Long vs Short Total P&L",

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT
        ),

        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        ),

        xaxis=dict(
            title="Trade Direction",
            gridcolor=GRID
        ),

        yaxis=dict(
            title="Total P&L",
            gridcolor=GRID,

            zeroline=True,

            zerolinecolor=TEXT

        )

    )

    return fig