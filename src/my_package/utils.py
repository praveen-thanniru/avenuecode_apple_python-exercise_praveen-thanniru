import pandas as pd


def aggregate_weekly_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates Apple stock data to a weekly level.

    Args:
        data (pd.DataFrame): DataFrame containing the Apple stock data.

    Returns:
        weekly_data (pd.DataFrame): Weekly aggregated DataFrame with columns:
            - 'Week_Start_Date': Start date of the week.
            - 'Average_Close_Price': Mean closing price of AAPL stock for the week.
            - 'Total_Volume': Total volume of AAPL stock traded for the week.
    """
    weekly_data = (
        data.resample("W")
        .agg({"AAPL.Close": "mean", "AAPL.Volume": "sum"})
        .reset_index()
    )

    weekly_data.rename(
        columns={
            "Date": "Week_Start_Date",
            "AAPL.Close": "Average_Close_Price",
            "AAPL.Volume": "Total_Volume",
        },
        inplace=True,
    )

    return weekly_data
