# # Standard library imports
# import datetime

# # Third party imports
# import matplotlib.pyplot as plt
# from pandas_datareader import data as wb
# import yfinance as yf

# import pandas as pd
# import numpy as np


# class Ticker:
#     """Class for fetcing data from yahoo finance."""
    
#     @staticmethod
#     def get_historical_data(ticker):
#         try:
#             data = yf.download(ticker, period="1y")  # Default to last 1 year of data

#             if data.empty:
#                 raise ValueError(f"No data returned for ticker '{ticker}'.")

#             return data
#         except Exception as e:
#             print(f"Error fetching data for ticker '{ticker}': {e}")
#             return None

#     @staticmethod
#     def get_columns(data):
#         """
#         Gets dataframe columns from previously fetched stock data.
        
#         Params:
#         data: dataframe representing fetched data
#         """
#         if data is None:
#             return None
#         return [column for column in data.columns]

#     @staticmethod
#     def get_last_price(data, column_name):
        
#         last_price = data[column_name].iloc[-1]
#         if isinstance(last_price, (pd.Series, np.ndarray)):
#             last_price = last_price.values[0]

#         return last_price
        

#         if data is None or column_name is None:
#             return None
#         if column_name not in Ticker.get_columns(data):
#             return None
#         # return float(data[column_name].iloc[-1].values[0])
        


#     @staticmethod
#     def plot_data(data, ticker, column_name):
#         try:
#             if data is None:
#                 return

#             fig, ax = plt.subplots()

#             ax.plot(data.index, data[column_name], label=column_name)
#             ax.set_ylabel(column_name)
#             ax.set_xlabel('Date')
#             ax.set_title(f'Historical data for {ticker} - {column_name}')
#             ax.legend(loc='best')

#             return fig

#         except Exception as e:
#             print(e)
#             return

import datetime

# Third-party imports
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
import yfinance as yf

import pandas as pd
import numpy as np

class Ticker:
    """
    A utility class for retrieving and analyzing historical stock data from Yahoo Finance.
    """

    @staticmethod
    def get_historical_data(ticker):
        """
        Retrieves historical stock data for the given ticker from Yahoo Finance.

        Parameters:
            ticker (str): The ticker symbol of the stock.

        Returns:
            pd.DataFrame: Historical stock data as a DataFrame.
        """
        try:
            stock_data = yf.download(ticker, period="1y")  # Default to 1 year of historical data

            if stock_data.empty:
                raise ValueError(f"No data available for the ticker symbol: '{ticker}'.")

            return stock_data
        except Exception as error:
            print(f"Failed to fetch data for '{ticker}': {error}")
            return None

    @staticmethod
    def get_columns(data):
        """
        Extracts and returns the column names from the given DataFrame.

        Parameters:
            data (pd.DataFrame): The DataFrame containing stock data.

        Returns:
            list: A list of column names from the DataFrame.
        """
        if data is None:
            return None
        return data.columns.tolist()

    @staticmethod
    def get_last_price(data, column_name):
        """
        Retrieves the most recent value from the specified column of the DataFrame.

        Parameters:
            data (pd.DataFrame): The DataFrame containing stock data.
            column_name (str): The column name from which to fetch the latest value.

        Returns:
            float: The latest value from the specified column.
        """
        try:
            last_price = data[column_name].iloc[-1]

            if isinstance(last_price, (pd.Series, np.ndarray)):
                last_price = last_price[0]

            return last_price
        except Exception as error:
            print(f"Error retrieving the latest price from '{column_name}': {error}")
            return None

    @staticmethod
    def plot_data(data, ticker, column_name):
        """
        Generates a plot for the specified column of historical stock data.

        Parameters:
            data (pd.DataFrame): The DataFrame containing stock data.
            ticker (str): The ticker symbol of the stock.
            column_name (str): The column name to be visualized.

        Returns:
            matplotlib.figure.Figure: The plot figure object.
        """
        try:
            if data is None:
                return None

            fig, ax = plt.subplots()

            ax.plot(data.index, data[column_name], label=column_name, color='blue')
            ax.set_title(f"{ticker} - Historical {column_name}")
            ax.set_xlabel("Date")
            ax.set_ylabel(column_name)
            ax.legend(loc="best")

            return fig
        except Exception as error:
            print(f"Error generating plot for '{ticker}': {error}")
            return None
