# Comparison of the Efficiency of the Greedy Algorithm and Dynamic Programming Algorithm

## Time Complexity

### Greedy Algorithm:

-   Time complexity: O(len(coins)).

-   The algorithm simply iterates through the sorted list of coins once, so its complexity depends only on the number of coins, not on the sum. This makes it very fast even for large sums.

### Dynamic Programming:

-   Time complexity: O(sum \* len(coins)).

-   The algorithm fills a DP array for every possible sum from 0 to sum, making it significantly slower for large sums.

## Performance for Large Sums

### Greedy Algorithm:

Works very quickly even for large sums because its complexity does not depend on the value of sum.
For example, for a sum of 1,000,000 and coins [50, 25, 10, 5, 1], the greedy algorithm will execute almost instantly.

### Dynamic Programming:

For large sums (e.g., 1,000,000), the algorithm becomes impractical due to high time and space complexity.
For example, for a sum of 1,000,000 and coins [50, 25, 10, 5, 1], the DP algorithm will need to process a million elements in the DP array, which will take a lot of time and memory.

## Algorithm efficiency

### Greedy Algorithm:

Efficient for large sums because its complexity does not depend on the value of sum.
However, it only works for "canonical" coin systems (e.g., [50, 25, 10, 5, 1]), where the locally optimal choice always leads to a globally optimal solution.

### Dynamic Programming:

Efficient for small sums or for coin systems where the greedy algorithm does not work (e.g., [10, 6, 1]).
For large sums, the DP algorithm becomes inefficient due to high time and space complexity.

## Conclusion

For large sums: The greedy algorithm is significantly more efficient because its execution time does not depend on the value of sum.

For small sums or non-standard coin systems: Dynamic programming is the better choice because it guarantees an optimal solution.
