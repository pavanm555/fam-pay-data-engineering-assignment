import pandas as pd

def daily_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    df = df.set_index("date")

    monthly = (
        df.groupby("ticker")
        .resample("M")
        .agg(
            open=("open", "first"),
            high=("high", "max"),
            low=("low", "min"),
            close=("close", "last"),
        )
        .reset_index()
    )

    return monthly
