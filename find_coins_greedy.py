def find_coins_greedy(coins: list[int], sum: int) -> tuple[int, dict]:
    """
    Implements a greedy algorithm to find the minimum number of coins required to make up a given sum.

    The function iteratively selects the largest possible coin that does not exceed the remaining sum.
    It continues this process until the remaining sum is reduced to zero or no further coins can be used.

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
    rest = sum
    results = {}

    while rest > 0:
        if rest < coins[-1]:
            return (rest, results)

        for coin in coins:
            if coin <= rest:
                if not coin in results:
                    results[coin] = 0
                results[coin] += 1
                rest -= coin
                break

    return (rest, results)


if __name__ == "__main__":
    # Testing
    from print_result import print_result

    sum = 113
    coins = [50, 25, 10, 5, 2, 1]

    results = find_coins_greedy(coins, sum)
    print_result(coins, sum, results)

    coins = [50, 25, 10, 5]

    results = find_coins_greedy(coins, sum)
    print_result(coins, sum, results)

    sum = 12
    coins = [10, 6, 1]

    results = find_coins_greedy(coins, sum)
    print_result(coins, sum, results)
