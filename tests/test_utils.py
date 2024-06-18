import pytest
import pandas as pd
from src.my_package import utils


@pytest.fixture
def sample_data():
    """
    Fixture that provides sample data for testing aggregate_weekly_data function.

    Returns:
    - pd.DataFrame: DataFrame containing sample data for Date, AAPL.Close, AAPL.Volume.
    """
    return pd.DataFrame(
        {
            "Date": pd.date_range("2023-01-01", periods=10),
            "AAPL.Close": [100, 102, 105, 99, 97, 98, 103, 101, 104, 106],
            "AAPL.Volume": [
                1000000,
                950000,
                1100000,
                1050000,
                980000,
                1020000,
                1150000,
                1080000,
                1120000,
                1200000,
            ],
        }
    )


def test_aggregate_weekly_data(sample_data):
    """
    Test case for aggregate_weekly_data function.

    Parameters:
    - sample_data (pd.DataFrame): Fixture providing sample data for testing.

    Asserts:
    - Checks that the length of the aggregated weekly data is as expected (2 weeks).
    """
    weekly_data = utils.aggregate_weekly_data(sample_data)
    assert len(weekly_data) == 2  # Assuming 2 weeks of data in the sample_data
