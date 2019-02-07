"""Dynamic Programming - Coin Change Problem"""

from math import inf

input1 = input().split()
input2 = input().split()
V, _ = int(input1[0]), int(input1[1])
COINS = [int(x) for x in input2]


def minimum_coin_dynamic(coins, v):
    """Minimum Coins Dynamic Top-Down"""
    lookup = [inf for _ in range(v + 1)]
    lookup[0] = 0
    for i in range(1, v + 1):
        for c in coins:
            if c <= i:
                temp = lookup[i - c]
                if temp != inf and temp + 1 < lookup[i]:
                    lookup[i] = temp + 1
    return lookup[v]


print(minimum_coin_dynamic(COINS, V))
