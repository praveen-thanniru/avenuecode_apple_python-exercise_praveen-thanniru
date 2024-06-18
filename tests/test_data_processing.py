import pandas as pd
import pytest
from src.my_package.data_processing import DataProcessor


# Define sample data for testing
@pytest.fixture
def sample_data_processor():
    """
    Fixture that creates a DataProcessor instance with sample data for testing.

    Returns:
    - DataProcessor: Initialized DataProcessor instance with sample data.
    """
    # Create a DataProcessor instance with sample data
    processor = DataProcessor("sample_data.csv")

    # Sample data creation
    processor.data = pd.DataFrame(
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

    # Ensure Date is in datetime format
    processor.data["Date"] = pd.to_datetime(processor.data["Date"])

    return processor


# Test function for compute_statistics method
def test_compute_statistics(sample_data_processor):
    """
    Test case for compute_statistics method of DataProcessor.

    Parameters:
    - sample_data_processor (DataProcessor): Fixture providing sample DataProcessor instance.

    Asserts:
    - Check correctness of max_value, min_value, and average_value calculations.
    """
    max_value, min_value, average_value = (
        sample_data_processor.compute_statistics()
    )
    assert max_value == pytest.approx(106, rel=1e-2)
    assert min_value == 97
    assert average_value == pytest.approx(101.5, rel=1e-2)


# Test function for filter_by_average_volume method
def test_filter_by_average_volume(sample_data_processor):
    """
    Test case for filter_by_average_volume method of DataProcessor.

    Parameters:
    - sample_data_processor (DataProcessor): Fixture providing sample DataProcessor instance.

    Asserts:
    - Check that all values in filtered_data["AAPL.Volume"] are greater than or equal to the original average_volume.
    """
    original_average_volume = sample_data_processor.data["AAPL.Volume"].mean()
    filtered_data = sample_data_processor.filter_by_average_volume()
    assert (filtered_data["AAPL.Volume"] >= original_average_volume).all()


# Test function for aggregate_weekly_data method
def test_aggregate_weekly_data(sample_data_processor):
    """
    Test case for aggregate_weekly_data method of DataProcessor.

    Parameters:
    - sample_data_processor (DataProcessor): Fixture providing sample DataProcessor instance.

    Asserts:
    - Check that weekly_df is not empty and contains expected columns ('Date', 'AAPL.Close', 'AAPL.Volume').
    """
    sample_data_processor.add_day_of_week()
    weekly_df = sample_data_processor.aggregate_weekly_data()
    assert not weekly_df.empty
    assert "Date" in weekly_df.columns
    assert "AAPL.Close" in weekly_df.columns
    assert "AAPL.Volume" in weekly_df.columns
