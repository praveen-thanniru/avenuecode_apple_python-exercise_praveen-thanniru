from src.my_package.data_processing import DataProcessor
from src.my_package.visualization import StockVisualizer
import pandas as pd

DATA_FILE_PATH = (
    "/Users/praveenkumarthanniru/Downloads/finance-charts-apple.csv"
)


def main():
    """
    Main function to demonstrate data processing, visualization, and error handling.

    Raises:
        Exception: If any error occurs during data processing, statistics computation, data filtering,
            day of week addition, weekly data aggregation, or visualization.
    """
    # Create instance of DataProcessor
    processor = DataProcessor(DATA_FILE_PATH)

    # Load data
    try:
        processor.load_data()
    except Exception as e:
        raise Exception(f"Error loading data: {e}")

    # Compute statistics
    try:
        max_value, min_value, average_value = processor.compute_statistics()
        print(
            f"Max value: {max_value}, Min value: {min_value}, Average value: {average_value}"
        )
    except Exception as e:
        raise Exception(f"Error computing statistics: {e}")

    # Filter by average volume
    try:
        filtered_data = processor.filter_by_average_volume()
        filtered_data.to_csv("filtered_data.csv", index=False)
        print("Filtered data saved to filtered_data.csv")
    except Exception as e:
        raise Exception(f"Error filtering data: {e}")

    # Add day of the week
    try:
        data_with_day = processor.add_day_of_week()
        data_with_day.to_csv("data_with_day.csv", index=False)
        print("Data with day of week saved to data_with_day.csv")
    except Exception as e:
        raise Exception(f"Error adding day of week: {e}")

    # Aggregate weekly data
    try:
        weekly_data = processor.aggregate_weekly_data()
        weekly_data.to_csv("weekly_data.csv", index=False)
        print("Weekly aggregated data saved to weekly_data.csv")
    except Exception as e:
        raise Exception(f"Error aggregating weekly data: {e}")

    # Visualize data using StockVisualizer
    try:
        visualizer = StockVisualizer(
            filtered_data
        )  # Assuming filtered_data is used for visualization
        fig = visualizer.create_candlestick_chart()
        fig.show()
    except Exception as e:
        raise Exception(f"Error visualizing data: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
