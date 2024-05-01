import matplotlib.pyplot as plt

def calculate_moving_average(stock_data, window_size=20, column='Close'):
    """Calculate moving averages for the given window size."""
    return stock_data[column].rolling(window=window_size).mean()

def plot_moving_averages(stock_data, window_sizes=None, column='Close'):
    """Plot stock prices with moving averages."""
    if window_sizes is None:
        window_sizes = [20, 50, 200]

    plt.figure(figsize=(10, 5))
    plt.plot(stock_data.index, stock_data[column], label='Stock Price')
    for window in window_sizes:
        moving_avg = calculate_moving_average(stock_data, window, column)
        plt.plot(stock_data.index, moving_avg, label=f'{window}-day MA')
    plt.title('Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()