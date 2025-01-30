def find_min_coins(coins: list[int], sum: int) -> tuple[int, dict]:
    """
    Implements a dynamic programming algorithm to find the minimum number of coins required to make up a given sum.

    Args:
        coins (list[int]): A list of available coin denominations.
        sum (int): The target sum to be achieved using the coins.

    Returns:
        tuple[int, dict]: A tuple containing:
            - The remaining sum that could not be achieved with the given coins (0 if the sum is fully achieved).
            - A dictionary where keys are coin denominations and values are the counts of each coin used.
    """
    # Sort coins in descending order
    coins.sort(reverse=True)
    # Initialize a array to store the minimum number of coins required for each sum
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make sum 0

    # Initialize a list to store the last coin used for each sum
    last_coin_used = [-1] * (sum + 1)

    # Fill the array
    for coin in coins:
        for i in range(coin, sum + 1):
            # print("PPPPP", coin, i, dp)
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin_used[i] = coin

    # If the sum cannot be achieved, return the remaining sum and an empty dictionary
    # print("SSSSSSSs", sum, dp)
    if dp[sum] == float('inf'):
        return (sum, {})

    # Reconstruct the coins used
    coin_counts = {}
    rest = sum
    while rest > 0:
        coin = last_coin_used[rest]
        if coin in coin_counts:
            coin_counts[coin] += 1
        else:
            coin_counts[coin] = 1
        rest -= coin

    return (0, coin_counts)


if __name__ == "__main__":
    # Testing
    from print_result import print_result

    sum = 113
    coins = [50, 25, 10, 5, 2, 1]

    results = find_min_coins(coins, sum)
    print_result(coins, sum, results)

    coins = [50, 25, 10, 5]

    results = find_min_coins(coins, sum)
    print_result(coins, sum, results)

    sum = 12
    coins = [10, 6, 1]

    results = find_min_coins(coins, sum)
    print_result(coins, sum, results)
