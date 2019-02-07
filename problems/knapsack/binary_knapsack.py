def knapsack(weights, values, capacity, n):
    """Naive Recursive Approach"""
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)

    else:
        return max(knapsack(weights, values, capacity - weights[n - 1], n - 1) + values[n - 1],
                   knapsack(weights, values, capacity, n - 1))


print(knapsack([10, 20, 30], [60, 100, 120], 50, 3))


def knapsack_dp(capacity, weights, values, items):
    lookup = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]
    for i in range(items + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                lookup[i][w] = 0
            elif weights[i - 1] <= w:
                lookup[i][w] = max(values[i - 1] + lookup[i - 1][w - weights[i - 1]], lookup[i - 1][w])
            else:
                lookup[i][w] = lookup[i - 1][w]
    return lookup[items][capacity]


print(knapsack_dp(55, [10, 20, 30], [60, 100, 120], 3))
