
def print_result(coins: list[int], sum: int, result: tuple[int, dict]):
    """
    Prints the result of the coin change algorithm in a readable format.

    Args:
        coins (list[int]): The list of available coin denominations.
        sum (int): The target sum that was attempted to be achieved.
        result (tuple[int, dict]): The result from the `find_coins_greedy` function, containing:
            - The remaining sum that could not be achieved (if any).
            - A dictionary of coin denominations and their counts used to achieve the sum.
    """
    rest_sum, coin_counts = result

    print(f"Available coins: {coins}")
    print(f"Target sum: {sum}")
    print("Coins used:")
    for coin, count in coin_counts.items():
        print(f"  {coin} cents: {count} coin(s)")

    if rest_sum > 0:
        print(
            f"Warning: Could not achieve the full sum. Remaining amount: {rest_sum} cents\n")
    else:
        print("Success: The full sum was achieved!\n")
