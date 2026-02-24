import os
import pandas as pd
import yfinance as yf
import numpy as np  # Keep this for log calculations
from datetime import datetime
from pathlib import Path  # For resolving absolute paths
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

# Ensure the src/__init__.py file exists
with open("src/__init__.py", "a"):
    pass

# Resolve absolute path for cache directory
CACHE_ROOT = (Path(__file__).resolve().parents[1] / "data").as_posix()

def compute_returns(df: pd.DataFrame, method: str = "log") -> pd.Series:
    """
    Given a DataFrame with a 'Close' column, returns a Series of returns.
    :param df: DataFrame with a 'Close' column.
    :param method: "simple" or "log"
    :return: Series of returns.
    """
    if "Close" not in df.columns:
        raise ValueError("Input DataFrame must contain a 'Close' column.")

    close = df["Close"]
    if method == "simple":
        return close.pct_change().dropna()
    elif method == "log":
        # Use vectorized np.log for better performance
        return np.log(close / close.shift(1)).dropna()
    else:
        raise ValueError("method must be 'simple' or 'log'")

def fetch_ohlcv(
    symbol: str,
    start: str,
    end: str,
    interval: str = "1d",
    adjust: bool = True,
    vendor: str = "yfinance",
    cache_dir: str = CACHE_ROOT,
) -> pd.DataFrame:
    """
    Fetch OHLCV for `symbol` between start/end dates at given interval.
    Caches results to CSV to avoid re‑downloading.

    :param symbol: ticker, e.g. "AAPL"
    :param start:  "YYYY-MM-DD"
    :param end:    "YYYY-MM-DD"
    :param interval: "1d", "1m", "5m", etc.
    :param adjust: auto_adjust=True applies splits/divs
    :param vendor: only "yfinance" implemented here
    :param cache_dir: where to store CSVs
    :return: DataFrame indexed by Timestamp, columns [Open, High, Low, Close, Volume]
    """
    os.makedirs(cache_dir, exist_ok=True)
    # filename encodes all parameters → unique cache per config
    fn = f"{symbol}_{start}_{end}_{interval}_{'adj' if adjust else 'raw'}.csv"
    path = os.path.join(cache_dir, fn)

    # 1) Cache hit?
    if os.path.exists(path):
        try:
            df = pd.read_csv(path, parse_dates=["Datetime"], index_col="Datetime")
            return df
        except Exception as e:
            print(f"Error loading cached file {path}: {e}")
            print("Re-downloading data...")

    # 2) Download from yfinance
    if vendor.lower() == "yfinance":
        df = yf.download(
            symbol,
            start=start,
            end=end,
            interval=interval,
            auto_adjust=adjust,
            progress=False,    # disable progress bar
        )
        # yfinance uses "Date" as index name for daily, "Datetime" for intraday
        if "Date" in df.index.names:
            df.index.name = "Datetime"
    else:
        raise ValueError(f"Unsupported vendor: {vendor}")

    # Guard against empty DataFrame
    if df.empty:
        raise ValueError(f"No data returned for {symbol} from {start} to {end}")

    # 2.1) Rename columns to match expected format
    df.rename(
        columns={
            "Open": "Open",
            "High": "High",
            "Low": "Low",
            "Close": "Close",
            "Volume": "Volume",
        },
        inplace=True,
    )
    # 2.2) Add adjusted columns if not present
    if "Adj Close" not in df.columns:
        df["Adj Close"] = df["Close"]
    if "Adj Volume" not in df.columns:
        df["Adj Volume"] = df["Volume"]
    # 2.3) Add returns columns
    df["Returns"] = compute_returns(df, method="log")
    df["Returns (Adj)"] = compute_returns(df, method="log")
    df["Returns (Raw)"] = compute_returns(df, method="simple")
    df["Returns (Adj Raw)"] = compute_returns(df, method="simple")
    # 2.4) Add date columns
    df["Date"] = df.index.date
    df["Year"] = df.index.year
    df["Month"] = df.index.month
    df["Day"] = df.index.day
    df["Weekday"] = df.index.weekday
    df["Week"] = df.index.isocalendar().week
    df["Quarter"] = df.index.quarter
    df["Year-Month"] = df.index.to_period("M")
    df["Year-Quarter"] = df.index.to_period("Q")
    df["Year-Week"] = df.index.to_period("W")
    df["Year-Day"] = df.index.to_period("D")
    df["Year-Weekday"] = df.index.to_period("W")

    # 3) Save and return
    df.to_csv(path)
    return df