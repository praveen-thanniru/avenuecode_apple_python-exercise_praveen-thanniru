import plotly.graph_objects as go
import pandas as pd


class StockVisualizer:
    """
    A class to create visualizations for Apple stock data using Plotly.

    Attributes:
        data (pd.DataFrame): DataFrame containing Apple stock data.

    Methods:
        create_candlestick_chart(): Creates a candlestick chart for Apple stock data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize with the data for visualization.

        Args:
            data (pd.DataFrame): DataFrame containing Apple stock data.
        """
        self.data = data

    def create_candlestick_chart(self) -> go.Figure:
        """
        Creates a candlestick chart for Apple stock data using Plotly.

        Returns:
            fig (plotly.graph_objects.Figure): Candlestick chart figure.
        """
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=self.data["Date"],
                    open=self.data["AAPL.Open"],
                    high=self.data["AAPL.High"],
                    low=self.data["AAPL.Low"],
                    close=self.data["AAPL.Close"],
                )
            ]
        )

        fig.update_layout(
            title="Apple Stock Candlestick Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False,
        )

        return fig
