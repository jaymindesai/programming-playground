STRING1 = 'PXYPA'
STRING2 = 'PP'
STRING3 = 'PXYAZXP'
STRING4 = 'XYAYX'
STRING5 = 'ALKJDBWIC'
STRING6 = 'MISSISSIPI'
STRING7 = 'ABCDE'
#
#
# def lps_recursive(s):
#     if len(s) == 0:
#         return 0
#     elif len(s) == 1:
#         return 1
#     elif s[0] == s[-1]:
#         return lps_recursive(s[1:-1]) + 2
#     else:
#         return max(lps_recursive(s[:-1]), lps_recursive(s[1:]))
#
# print('\t')
# print('MPSP Recursive:')
# print('Length of Longest Palindromic Subsequence of', STRING1, 'is', lps_recursive(STRING1))
# print('Length of Longest Palindromic Subsequence of', STRING2, 'is', lps_recursive(STRING2))
# print('Length of Longest Palindromic Subsequence of', STRING3, 'is', lps_recursive(STRING3))
# print('Length of Longest Palindromic Subsequence of', STRING4, 'is', lps_recursive(STRING4))
# print('Length of Longest Palindromic Subsequence of', STRING5, 'is', lps_recursive(STRING5))
# print('Length of Longest Palindromic Subsequence of', STRING6, 'is', lps_recursive(STRING6))
# print('Length of Longest Palindromic Subsequence of', STRING7, 'is', lps_recursive(STRING7))


def lps_dynamic_memoize(s, lookup):
    if len(s) == 0:
        return 0
    if not lookup.get(s, None):
        if len(s) == 1:
            lookup[s] = 1
        elif s[0] == s[-1]:
            lookup[s] = lps_dynamic_memoize(s[1:-1], lookup) + 2
        else:
            lookup[s] = max(lps_dynamic_memoize(s[:-1], lookup),
                            lps_dynamic_memoize(s[1:], lookup))
    return lookup[s]

print('\t')
print('MPSP Recursive - Dynamic Memoized:')
print('Length of Longest Palindromic Subsequence of', STRING1, 'is', lps_dynamic_memoize(STRING1, {}))
print('Length of Longest Palindromic Subsequence of', STRING2, 'is', lps_dynamic_memoize(STRING2, {}))
print('Length of Longest Palindromic Subsequence of', STRING3, 'is', lps_dynamic_memoize(STRING3, {}))
print('Length of Longest Palindromic Subsequence of', STRING4, 'is', lps_dynamic_memoize(STRING4, {}))
print('Length of Longest Palindromic Subsequence of', STRING5, 'is', lps_dynamic_memoize(STRING5, {}))
print('Length of Longest Palindromic Subsequence of', STRING6, 'is', lps_dynamic_memoize(STRING6, {}))
print('Length of Longest Palindromic Subsequence of', STRING7, 'is', lps_dynamic_memoize(STRING7, {}))
print('\t')



