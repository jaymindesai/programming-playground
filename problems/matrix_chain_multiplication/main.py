"""Dynamic Programming - Parenthesize the Matrix Chain Multiplication"""

from math import inf

N = int(input())
P = [int(x) for x in input().split()]

def find_matrix_chain_order(num, dims):
    """Find the Minimum Number and Optimal Order of Multiplications"""
    muls = [[0] * num for _ in range(num)]
    parens = [[0] * num for _ in range(num - 1)]
    for i in range(1, num):
        for row in range(num - i):
            col = row + i
            muls[row][col] = inf
            for k in range(row, col):
                temp = muls[row][k] + muls[k+1][col] + (dims[row] * dims[k+1] * dims[col+1])
                if temp < muls[row][col]:
                    muls[row][col] = temp
                    parens[row][col] = k
    return muls, parens

def get_optimal_parens(parens, row, col, acc_list):
    """Prepare the Parenthesized String"""
    if row == col:
        acc_list.append(str(row + 1))
    else:
        acc_list.append('(')
        get_optimal_parens(parens, row, parens[row][col], acc_list)
        get_optimal_parens(parens, parens[row][col] + 1, col, acc_list)
        acc_list.append(')')
    return acc_list

MULS, PARENS = find_matrix_chain_order(N, P)
PAR_STRING = ''.join(get_optimal_parens(PARENS, 0, N - 1, []))

print(MULS[0][N - 1])
print(PAR_STRING)
