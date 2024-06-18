
# Apple Stock Data Processor and Visualizer

This Python package processes and visualizes Apple stock data from a CSV file.

## Installation

1. Ensure you have Python 3.7 or later installed.

2. Install the package using pip:
pip install dist/my_package-0.1.0-py3-none-any.whl


## Usage

### Data Processing

Initialize the DataProcessor and load data:
```python
from my_package.data_processing import DataProcessor

DATA_FILE_PATH = 'path/to/your/data.csv'
processor = DataProcessor(DATA_FILE_PATH)
processor.load_data()
```
### Compute Statistics
max_value, min_value, average_value = processor.compute_statistics()

### filter data by average volume:
filtered_data = processor.filter_by_average_volume()

### Add the day of the week
data_with_day = processor.add_day_of_week()

## Data Visualization
### Visualize data using StockVisualizer:

from my_package.visualization import StockVisualizer

visualizer = StockVisualizer(filtered_data)  # Use filtered_data or another DataFrame
fig = visualizer.create_candlestick_chart()
fig.show()


## Running Tests
### Install pytest if you haven't already:

pip install pytest

### Run tests

pytest tests/


# Code Style
### Check for PEP 8 compliance:


flake8 src/ tests/

### Format code using black:

black src/ tests/
