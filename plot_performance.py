import time
import matplotlib.pyplot as plt
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def measure_time(algorithm, coins, sum):
    """
    Function for measuring execution time
    """
    start_time = time.time()
    algorithm(coins, sum)
    return time.time() - start_time


def plot_performance(coins, max_sum, step):
    sums = list(range(1, max_sum + 1, step))
    greedy_times = []
    dp_times = []

    for sum in sums:
        greedy_time = measure_time(find_coins_greedy, coins, sum)
        dp_time = measure_time(find_min_coins, coins, sum)
        greedy_times.append(greedy_time)
        dp_times.append(dp_time)

    plt.plot(sums, greedy_times, label="Greedy Algorithm")
    plt.plot(sums, dp_times, label="Dynamic Programming")
    plt.xlabel("Sum")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison: Greedy vs Dynamic Programming")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Parameters for plotting a graph
    coins = [50, 25, 10, 5, 1]
    max_sum = 10000
    step = 10
    plot_performance(coins, max_sum, step)
