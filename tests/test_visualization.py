import pytest
import pandas as pd
from src.my_package.visualization import create_candlestick_chart


@pytest.fixture
def mock_data():
    """
    Fixture that provides mock data for testing create_candlestick_chart function.

    Returns:
    - dict: Dictionary containing mock data for Date, AAPL.Open, AAPL.High, AAPL.Low, AAPL.Close.
    """
    mock_data = {
        "Date": pd.date_range("2023-01-01", periods=2),
        "AAPL.Open": [100, 102],
        "AAPL.High": [105, 107],
        "AAPL.Low": [99, 101],
        "AAPL.Close": [102, 105],
    }
    return mock_data


def test_create_candlestick_chart(mock_data):
    """
    Test case for create_candlestick_chart function.

    Parameters:
    - mock_data (dict): Fixture providing mock data for testing.

    Asserts:
    - Checks that the returned figure object is not None.
    """
    fig = create_candlestick_chart(mock_data)
    assert fig is not None
