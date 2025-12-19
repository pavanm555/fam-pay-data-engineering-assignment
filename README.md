# FAM Pay – Data Engineering Intern Assignment

## Overview
This project transforms daily stock price data into monthly aggregates and computes technical indicators (SMA & EMA) using Python and Pandas.

## Dataset
- 2 years of daily stock data
- 10 tickers: AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA

## Transformations
- Open: First trading day of the month
- Close: Last trading day of the month
- High: Monthly maximum
- Low: Monthly minimum

## Technical Indicators
Calculated on monthly closing prices:
- SMA 10, SMA 20
- EMA 10, EMA 20

## Output
- 10 CSV files (one per ticker)
- 24 rows per file
- Naming format: `result_<TICKER>.csv`

# Assumptions
- Dataset contains continuous data per each ticker within the 2-year period.
- There are no duplicated dates within a given ticker’s time series.
- Dataset has no missing dates per ticker
- Pandas `ewm()` is used for EMA as it follows the standard formula
- Final 24 months are selected per ticker

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
