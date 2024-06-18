import pandas as pd
from typing import Tuple


class DataProcessor:
    """
    A class to handle data processing tasks for Apple stock data.

    Attributes:
        data_file_path (str): Path to the data file.
        data (pd.DataFrame): DataFrame to store loaded data.

    Methods:
        load_data(): Load data from the specified CSV file.
        compute_statistics(): Compute max, min, and average closing prices.
        filter_by_average_volume(): Filter data by average volume.
        add_day_of_week(): Add a day of the week column based on 'Date'.
        aggregate_weekly_data(): Aggregate data into weekly intervals.
    """

    def __init__(self, data_file_path: str):
        """
        Initialize with the path to the data file.

        Args:
            data_file_path (str): Path to the CSV data file.
        """
        self.data_file_path = data_file_path
        self.data = None

    def load_data(self) -> None:
        """
        Load data from the specified CSV file and ensure 'Date' column is datetime.
        """
        self.data = pd.read_csv(self.data_file_path)
        self.data["Date"] = pd.to_datetime(self.data["Date"])

    def compute_statistics(self) -> Tuple[float, float, float]:
        """
        Compute statistics (max, min, average) of closing prices.

        Returns:
            Tuple[float, float, float]: Max value, min value, average value of 'AAPL.Close'.
        """
        if self.data is None:
            raise Exception(
                "Data has not been loaded. Call load_data() first."
            )

        max_value = self.data["AAPL.Close"].max()
        min_value = self.data["AAPL.Close"].min()
        average_value = self.data["AAPL.Close"].mean()
        return max_value, min_value, average_value

    def filter_by_average_volume(self) -> pd.DataFrame:
        """
        Filter data where 'AAPL.Volume' is greater than or equal to average volume.

        Returns:
            pd.DataFrame: Filtered DataFrame based on average volume.
        """
        if self.data is None:
            raise Exception(
                "Data has not been loaded. Call load_data() first."
            )

        average_volume = self.data["AAPL.Volume"].mean()
        filtered_data = self.data[self.data["AAPL.Volume"] >= average_volume]
        return filtered_data

    def add_day_of_week(self) -> pd.DataFrame:
        """
        Add a 'Day' column representing the day of the week for each date.

        Returns:
            pd.DataFrame: DataFrame with an added 'Day' column.
        """
        if self.data is None:
            raise Exception(
                "Data has not been loaded. Call load_data() first."
            )

        self.data["Day"] = self.data["Date"].dt.day_name()
        return self.data

    def aggregate_weekly_data(self) -> pd.DataFrame:
        """
        Aggregate data into weekly intervals, computing mean close price and sum volume.

        Returns:
            pd.DataFrame: DataFrame with weekly aggregated data.
        """
        if self.data is None:
            raise Exception(
                "Data has not been loaded. Call load_data() first."
            )

        weekly_df = (
            self.data.set_index("Date")
            .resample("W")
            .agg({"AAPL.Close": "mean", "AAPL.Volume": "sum"})
            .reset_index()
        )

        return weekly_df
