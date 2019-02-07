from math import inf

# V, _ = [int(x) for x in input().split()]
# D = list(map(int, input().split()))

V = 17
D = [1, 6, 10]

def minimum_coin_dynamic(v, deno, lookup):
    if not lookup.get(v, None):
        x = []
        for d in deno:
            if v >= d:
                x.append(minimum_coin_dynamic(v % d, deno, lookup) + (v // d))
        lookup[v] = (len(x) > 0) and min(x) or 0
    return lookup[v]

print(minimum_coin_dynamic(V, D, {0: 0}))
