from pathlib import Path
import os
from data_loader import load_data
from transformations import daily_to_monthly
from indicators import add_technical_indicators

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "output_file.csv"
OUTPUT_DIR = BASE_DIR / "output"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load
    df = load_data(DATA_PATH)

    # Transform to monthly
    monthly_df = daily_to_monthly(df)

    # Process each ticker separately
    for ticker in monthly_df["ticker"].unique():
        ticker_df = monthly_df[monthly_df["ticker"] == ticker].copy()

        # Add indicators
        ticker_df = add_technical_indicators(ticker_df)

        # Keep exactly 24 rows
        ticker_df = ticker_df.tail(24)

        # Save
        output_path = f"{OUTPUT_DIR}/result_{ticker}.csv"
        ticker_df.to_csv(output_path, index=False)

        print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
