# =============================================================================
# DATA LAYER
# =============================================================================
# This module is responsible for loading all exported data
# produced by the backtesting engine.
#
# Every other module imports data from here instead of reading
# CSV files multiple times.
# =============================================================================

# =============================================================================
# IMPORTS
# =============================================================================

import json
from pathlib import Path

import pandas as pd

# =============================================================================
# PROJECT PATHS
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "outputs"

# =============================================================================
# LOAD DATA
# =============================================================================

trades_df = pd.read_csv(
    OUTPUT_DIR / "trades.csv"
)

monthly_summary = pd.read_csv(
    OUTPUT_DIR / "monthly_summary.csv"
)

direction_summary = pd.read_csv(
    OUTPUT_DIR / "direction_summary.csv"
)

with open(
    OUTPUT_DIR / "dashboard_kpis.json",
    "r"
) as file:

    dashboard_kpis = json.load(file)
