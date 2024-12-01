from ticker import Ticker
data = Ticker.get_historical_data('AAPL', start_date='2023-01-01', end_date='2023-10-25')
print(data)