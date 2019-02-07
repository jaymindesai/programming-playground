# Constrained 0-1 Knapsack

from itertools import combinations


def knapsack_dynamic(values, weights, capacity, items):
    v = []
    w = []
    n = len(weights)
    result = 0
    for i in range(1, items + 1):
        for g in combinations(range(n), i):
            val = 0
            wt = 0
            for idx in g:
                val += values[idx]
                wt += weights[idx]
            v.append(val)
            w.append(wt)
            if wt <= capacity and val > result:
                result = val
    return result


# C, I = [int(x) for x in input().strip().split()]
# W = []
# V = []

# for _ in range(I):
#     ip = input().strip().split()
#     V.append(int(ip[0]))
#     W.append(int(ip[1]))

# print(knapsack_dynamic(V, W, C, I))
# print(knapsack_dynamic([4, 10, 5, 3], [3, 8, 4, 2], 10, 4))
print(knapsack_dynamic([60, 100, 120], [10, 20, 30], 50, 3))
