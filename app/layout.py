# =============================================================================
# DASHBOARD LAYOUT
# =============================================================================

from dash import html, dcc
import dash_bootstrap_components as dbc

from styles import (
    PAGE_STYLE,
    CARD_STYLE,
    TEXT,
    SUBTEXT
)

from data import (
    dashboard_kpis,
    trades_df
)

from charts import (
    create_equity_curve,
    create_pnl_chart,
    create_drawdown_chart,
    create_monthly_pnl,
    create_direction_chart,
    create_direction_pnl_chart
)


# =============================================================================
# KPI CARD
# =============================================================================

def create_kpi_card(title, value):

    return html.Div(

        style=CARD_STYLE,

        children=[

            html.H5(

                title,

                style={
                    "color": SUBTEXT,
                    "fontWeight": "500",
                    "fontSize": "18px",
                    "marginBottom": "15px"
                }

            ),

            html.H2(

                value,

                style={
                    "color": TEXT,
                    "fontWeight": "700",
                    "fontSize": "38px",
                    "margin": "0px"
                }

            )

        ]

    )


# =============================================================================
# CHART CARD
# =============================================================================

def create_chart_card(figure):

    return html.Div(

        style={
            "backgroundColor": "#1E293B",
            "border": "1px solid #334155",
            "borderRadius": "18px",
            "padding": "10px",
            "boxShadow": "0px 8px 20px rgba(0,0,0,0.35)"
        },

        children=[

            dcc.Graph(

                figure=figure,

                config={
                    "displayModeBar": True,
                    "displaylogo": False
                }

            )

        ]

    )


# =============================================================================
# DIRECTIONAL ANALYSIS
# =============================================================================

def calculate_direction_stats(direction):

    df = trades_df.copy()

    direction_lower = direction.lower()

    df["trade_direction"] = df["trade_type"].astype(str).str.lower()

    if direction_lower == "long":

        df = df[
            df["trade_direction"].str.contains(
                "buy",
                na=False
            )
        ]

    else:

        df = df[
            df["trade_direction"].str.contains(
                "sell",
                na=False
            )
        ]

    total_trades = len(df)

    profitable_trades = int(
        (df["pnl"] > 0).sum()
    )

    losing_trades = int(
        (df["pnl"] < 0).sum()
    )

    win_rate = (

        profitable_trades / total_trades * 100

        if total_trades > 0

        else 0

    )

    total_pnl = df["pnl"].sum()

    total_losses = df.loc[
        df["pnl"] < 0,
        "pnl"
    ].sum()

    winning_trades = df.loc[
        df["pnl"] > 0,
        "pnl"
    ]

    losing_trade_values = df.loc[
        df["pnl"] < 0,
        "pnl"
    ]

    average_winner = (

        winning_trades.mean()

        if len(winning_trades) > 0

        else 0

    )

    average_loser = (

        losing_trade_values.mean()

        if len(losing_trade_values) > 0

        else 0

    )

    best_trade = (

        df["pnl"].max()

        if total_trades > 0

        else 0

    )

    worst_trade = (

        df["pnl"].min()

        if total_trades > 0

        else 0

    )

    return {

        "total_trades": total_trades,

        "profitable_trades": profitable_trades,

        "losing_trades": losing_trades,

        "win_rate": win_rate,

        "total_pnl": total_pnl,

        "total_losses": total_losses,

        "average_winner": average_winner,

        "average_loser": average_loser,

        "best_trade": best_trade,

        "worst_trade": worst_trade

    }


# =============================================================================
# DIRECTION STAT CARD
# =============================================================================

def create_direction_card(title, stats):

    return html.Div(

        style={
            "backgroundColor": "#1E293B",
            "border": "1px solid #334155",
            "borderRadius": "18px",
            "padding": "25px",
            "boxShadow": "0px 8px 20px rgba(0,0,0,0.35)"
        },

        children=[

            html.H3(

                title,

                style={
                    "color": TEXT,
                    "textAlign": "center",
                    "marginBottom": "25px"
                }

            ),

            dbc.Row(

                [

                    dbc.Col(

                        [

                            html.Div(
                                "Total Trades",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                str(stats["total_trades"]),
                                style={
                                    "color": TEXT
                                }
                            )

                        ],

                        width=6

                    ),

                    dbc.Col(

                        [

                            html.Div(
                                "Profitable",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                str(stats["profitable_trades"]),
                                style={
                                    "color": "#10B981"
                                }
                            )

                        ],

                        width=6

                    )

                ]

            ),

            dbc.Row(

                [

                    dbc.Col(

                        [

                            html.Div(
                                "Losing",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                str(stats["losing_trades"]),
                                style={
                                    "color": "#EF4444"
                                }
                            )

                        ],

                        width=6

                    ),

                    dbc.Col(

                        [

                            html.Div(
                                "Win Rate",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['win_rate']:.2f}%",
                                style={
                                    "color": TEXT
                                }
                            )

                        ],

                        width=6

                    )

                ]

            ),

            html.Hr(
                style={
                    "borderColor": "#334155"
                }
            ),

            dbc.Row(

                [

                    dbc.Col(

                        [

                            html.Div(
                                "Total P&L",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['total_pnl']:,.2f}",
                                style={
                                    "color": (
                                        "#10B981"
                                        if stats["total_pnl"] >= 0
                                        else "#EF4444"
                                    )
                                }
                            )

                        ],

                        width=6

                    ),

                    dbc.Col(

                        [

                            html.Div(
                                "Total Losses",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['total_losses']:,.2f}",
                                style={
                                    "color": "#EF4444"
                                }
                            )

                        ],

                        width=6

                    )

                ]

            ),

            dbc.Row(

                [

                    dbc.Col(

                        [

                            html.Div(
                                "Avg Winner",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['average_winner']:,.2f}",
                                style={
                                    "color": "#10B981"
                                }
                            )

                        ],

                        width=6

                    ),

                    dbc.Col(

                        [

                            html.Div(
                                "Avg Loser",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['average_loser']:,.2f}",
                                style={
                                    "color": "#EF4444"
                                }
                            )

                        ],

                        width=6

                    )

                ]

            ),

            html.Hr(
                style={
                    "borderColor": "#334155"
                }
            ),

            dbc.Row(

                [

                    dbc.Col(

                        [

                            html.Div(
                                "Best Trade",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['best_trade']:,.2f}",
                                style={
                                    "color": "#10B981"
                                }
                            )

                        ],

                        width=6

                    ),

                    dbc.Col(

                        [

                            html.Div(
                                "Worst Trade",
                                style={
                                    "color": SUBTEXT
                                }
                            ),

                            html.H4(
                                f"{stats['worst_trade']:,.2f}",
                                style={
                                    "color": "#EF4444"
                                }
                            )

                        ],

                        width=6

                    )

                ]

            )

        ]

    )


# =============================================================================
# MAIN DASHBOARD
# =============================================================================

def create_layout():

    long_stats = calculate_direction_stats("long")

    short_stats = calculate_direction_stats("short")

    return html.Div(

        style=PAGE_STYLE,

        children=[

            # ==============================================================
            # HEADER
            # ==============================================================

            html.H1(

                "Quantitative Trading Analytics Dashboard",

                style={
                    "color": TEXT,
                    "textAlign": "center",
                    "fontWeight": "700",
                    "marginBottom": "8px"
                }

            ),

            html.H4(

                "Asian Session Breakout Strategy — Performance & Risk Analysis",

                style={
                    "color": SUBTEXT,
                    "textAlign": "center",
                    "marginBottom": "45px"
                }

            ),


            # ==============================================================
            # MAIN KPIs
            # ==============================================================

            dbc.Row(

                [

                    dbc.Col(
                        create_kpi_card(
                            "Ending Balance",
                            f"₹{dashboard_kpis['Ending Balance']:,.2f}"
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Return",
                            f"{dashboard_kpis['Return (%)']:.2f}%"
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Win Rate",
                            f"{dashboard_kpis['Win Rate (%)']:.2f}%"
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Profit Factor",
                            f"{dashboard_kpis['Profit Factor']:.2f}"
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Max Drawdown",
                            f"{dashboard_kpis['Max Drawdown (%)']:.2f}%"
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Trades",
                            str(dashboard_kpis["Total Trades"])
                        ),
                        lg=2,
                        md=4,
                        sm=6,
                        xs=12
                    )

                ],

                className="g-4",

                style={
                    "marginBottom": "40px"
                }

            ),


            # ==============================================================
            # LONG vs SHORT ANALYSIS
            # ==============================================================

            html.H2(

                "Long vs Short Performance",

                style={
                    "color": TEXT,
                    "textAlign": "center",
                    "marginBottom": "25px"
                }

            ),

            html.P(

                "Which trade direction contributes to performance — and which one causes the losses?",

                style={
                    "color": SUBTEXT,
                    "textAlign": "center",
                    "marginBottom": "30px"
                }

            ),

            dbc.Row(

                [

                    dbc.Col(

                        create_direction_card(
                            "LONG / BUY",
                            long_stats
                        ),

                        lg=6,
                        md=12

                    ),

                    dbc.Col(

                        create_direction_card(
                            "SHORT / SELL",
                            short_stats
                        ),

                        lg=6,
                        md=12

                    )

                ],

                className="g-4",

                style={
                    "marginBottom": "30px"
                }

            ),


            # ==============================================================
            # LONG vs SHORT P&L CHART
            # ==============================================================

            dbc.Row(

                [

                    dbc.Col(

                        create_chart_card(
                            create_direction_pnl_chart()
                        ),

                        width=12

                    )

                ],

                style={
                    "marginBottom": "35px"
                }

            ),


            # ==============================================================
            # EQUITY CURVE
            # ==============================================================

            dbc.Row(

                [

                    dbc.Col(

                        create_chart_card(
                            create_equity_curve()
                        ),

                        width=12

                    )

                ],

                style={
                    "marginBottom": "30px"
                }

            ),


            # ==============================================================
            # P&L + DRAWDOWN
            # ==============================================================

            dbc.Row(

                [

                    dbc.Col(

                        create_chart_card(
                            create_pnl_chart()
                        ),

                        lg=6,
                        md=12

                    ),

                    dbc.Col(

                        create_chart_card(
                            create_drawdown_chart()
                        ),

                        lg=6,
                        md=12

                    )

                ],

                className="g-4",

                style={
                    "marginBottom": "30px"
                }

            ),


            # ==============================================================
            # MONTHLY PERFORMANCE + TRADE DIRECTION
            # ==============================================================

            dbc.Row(

                [

                    dbc.Col(

                        create_chart_card(
                            create_monthly_pnl()
                        ),

                        lg=6,
                        md=12

                    ),

                    dbc.Col(

                        create_chart_card(
                            create_direction_chart()
                        ),

                        lg=6,
                        md=12

                    )

                ],

                className="g-4",

                style={
                    "marginBottom": "30px"
                }

            )

        ]

    )