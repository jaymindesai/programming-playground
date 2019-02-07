# def get_denominations_iterative(v, a=0, b=0, c=0, d=0, e=0, i=0):
#     while v > 0:
#         i += 1
#         if v >= 50:
#             a += int(v/50)
#             v = v % 50
#         elif v >= 25:
#             b += int(v/25)
#             v = v % 25
#         elif v >= 10:
#             c += int(v/10)
#             v = v % 10
#         elif v >= 5:
#             d += int(v/5)
#             v = v % 5
#         else:
#             e += v
#             v = 0
#     return a + b + c + d + e, i
#
#
# def get_denominations_recursive(v, a=0, b=0, c=0, d=0, e=0, i=0):
#     i += 1
#     if v == 0:
#         return a, b, c, d, e, i
#     if v >= 50:
#         a += int(v/50)
#         return get_denominations_recursive(v % 50, a, b, c, d, e, i)
#     elif v >= 25:
#         b += int(v/25)v
#         return get_denominations_recursive(v % 25, a, b, c, d, e, i)
#     elif v >= 10:
#         c += int(v/10)
#         return get_denominations_recursive(v % 10, a, b, c, d, e, i)
#     elif v >= 5:
#         d += int(v/5)
#         return get_denominations_recursive(v % 5, a, b, c, d, e, i)
#     else:
#         e += v
#     return a, b, c, d, e, i
#
# i = 0
# n = 876339
#
# print('iterative n, i = ' + str(get_denominations_iterative(n, i=i)))
# print('recursive a, b, c, d, e, i = ' + str(get_denominations_recursive(n, i=i)))


# def findMaxGoalsProbability(teamGoals):
#     if len(teamGoals) > 0:
#         scores = []
#         if len(teamGoals) > 0:
#             for i in range(0, len(teamGoals)):
#                 for j in range(i+1, len(teamGoals)):
#                     scores.append(teamGoals[i] + teamGoals[j])
#         x = max(scores)
#         prob = scores.count(x) / len(scores)
#         return '%.2f' % prob
#     return '%.2f' % 0
#
# print(findMaxGoalsProbability(teamGoals))


# import math
#
# def worstPerformingStock(prices):
#     if len(prices) > 0:
#         wps = [math.inf,
#                math.inf]  # list of worst performing stock with wps[0] = stockID and wps[1] = gain for that stock.
#         for s in prices:
#             gain = (s[2] - s[1]) / s[1]
#             if gain < wps[1]:
#                 wps[0] = s[0]
#                 wps[1] = gain
#         return wps[0]
#     return 0
#
# prices = [
#     [1200, 100, 105],
#     [1400, 50, 55]
# ]
#
# print(worstPerformingStock(prices))


# def tree(d, a):
#     res = []
#     for i, _ in enumerate(a):
#         count = d
#         val = None
#         idx = i
#         while count > 0 and idx >= 0:
#             val = a[idx]
#             idx = val
#             count -= 1
#         if val >= 0:
#             res.append(val)
#         else:
#             res.append(-1)
#     return res
#
# print(tree(3, [-1, 0, 4, 2, 1]))


# import math
#
# def houses_stores(stores, houses):
#     stores = sorted(stores)
#
#     res = []
#
#     for h in houses:
#         dist = math.inf
#         store = None
#         for s in stores:
#             if abs(h - s) < dist:
#                 dist = abs(h - s)
#                 store = s
#         res.append(store)
#     return res
#
# print(houses_stores(stores=[3, 1, 10, 18, 16, 20, 4, 3, 20, 65, 82, 93, 87],
#                     houses=[1, 2, 90, 22, 11, 17]))


# def license_key(s, k):
#     count = k
#     l = [''] * (2 * len(s) - 1)
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] != '-' and count != 0:
#             l[i] = s[i].upper()
#             count -= 1
#         else:
#             if s[i] != '-' and count == 0:
#                 l[i] = s[i].upper() + '-'
#                 count = k - 1
#     return ''.join(l)
#
# def _license_key(s, k):
#     count = k
#     l = list(s)
#     for i in range(len(l) - 1, -1, -1):
#         if l[i] != '-' and count == 0:
#             l[i] = '-{}'.format(l[i])
#             count = k - 1
#         else:
#             count -= 1
#
# print(license_key(s='2-4A0r7-4k', k=4))


# def get_unallocated_bidders(bids, shares):
#     bid_map = {}
#
#     for bid in bids:
#         if bid_map.get(bid[2], None) is not None:
#             bid_map[bid[2]].append(bid)
#             bid_map[bid[2]].sort(key=lambda x: x[3])
#         else:
#             bid_map[bid[2]] = [bid]
#
#     unallocated = []
#
#     for k in sorted(bid_map.keys(), reverse=True):
#         if shares > 0:
#             if len(bid_map[k]) == 1:
#                 shares -= bid_map[k][0][1]
#             else:
#                 finished = False
#                 c = 0
#                 while len(bid_map[k]) > 0 and not finished:
#                     for bid in bid_map[k]:
#                         if bid[1] > 0:
#                             if shares > 0:
#                                 bid[1] -= 1
#                                 shares -= 1
#                             else:
#                                 finished = True
#                                 if c == 0:
#                                     unallocated.append(bid[0])
#                                 bid_map[k].clear()
#                         else:
#                             bid_map[k].remove(bid)
#                     c += 1
#         else:
#             if len(bid_map[k]) == 1:
#                 unallocated.append(bid_map[k][0][0])
#             else:
#                 for bid in bid_map[k]:
#                     unallocated.append(bid[0])
#
#     return sorted(unallocated)
#
# print(get_unallocated_bidders([[1, 2, 5, 0], [2, 1, 4, 2], [3, 5, 4, 6]], 3))
# print(get_unallocated_bidders([[1, 3, 1, 9866], [2, 1, 2, 5258], [3, 2, 4, 5788], [4, 2, 4, 6536]], 2))
# print(get_unallocated_bidders([[1, 2, 4, 6208]], 2))


# def get_most_visited(n, sprints):
#     counts = [0]*(n+1)
#     for i in range(len(sprints) - 1):
#         if sprints[i] < sprints[i + 1]:
#             for j in range(sprints[i], sprints[i+1] + 1):
#                 counts[j] += 1
#         else:
#             for j in range(sprints[i+1], sprints[i] + 1):
#                 counts[j] += 1
#     res = 0
#     mx = -1
#     for i in range(1, len(counts)):
#         if counts[i] > mx:
#             mx = counts[i]
#             res = i
#     return res
#
# print(get_most_visited(10, [1, 5, 10, 3]))


# def missing_words(s, t):
#     if len(s) > len(t):
#         s = s.split()
#         t = t.split()
#         result = []
#         j = 0
#         for word in s:
#             if word == t[j]:
#                 j = j + 1 if j < (len(t) - 1) else j
#             else:
#                 result.append(word)
#         return result
#     return []
#
# s = 'I am using HackerRank to improve programming'
# t = 'am HackerRank to improve'
#
# print(missing_words(s, t))


# def distinct_odd_subsets(a, k):
#     """No of distinct subsets with at most k odd numbers """
#     res = []
#     lookup = [['']*len(a) for _ in range(len(a))]
#     for i in range(len(a)):
#         for j in range(i, len(a)):
#             if a[i] == a[j]:
#                 if a[j] % 2 == 0:
#                     lookup[i][j] = 0
#                 else:
#                     lookup[i][j] = 1
#                 if lookup[i][j] <= k:
#                     temp = sorted([a[p] for p in range(i, j+1)])
#                     if temp not in res:
#                         res.append(temp)
#             else:
#                 if a[j] % 2 == 0:
#                     lookup[i][j] = lookup[i][j-1]
#                 else:
#                     lookup[i][j] = lookup[i][j - 1] + 1
#                 if lookup[i][j] <= k:
#                     temp = sorted([a[p] for p in range(i, j + 1)])
#                     if temp not in res:
#                         res.append(temp)
#     return len(res)
#
# a = [2, 1, 2, 1, 3]
# k = 3
# print(distinct_odd_subsets(a, k))


# def min_ops(words):
#     result = []
#     for word in words:
#         i = 1
#         r = 0
#         while i < len(word):
#             if word[i] == word[i-1]:
#                 count = 1
#                 j = i
#                 done = False
#                 while not done and word[j] == word[j-1]:
#                     count += 1
#                     j += 1
#                     if j == len(word):
#                         done = True
#                 i = j
#                 r += count//2
#             i += 1
#         result.append(r)
#     return result
#
# print(min_ops(['ab','aab', 'abb', 'abab', 'abaaaba', 'aabcc']))


# from collections import defaultdict
#
# def vote_count(votes):
#     counts = defaultdict(int)
#     mx = 0
#     for vote in votes:
#         counts[vote] += 1
#         if counts[vote] > mx:
#             mx = counts[vote]
#     winners = []
#     for vote, count in counts.items():
#         if count == mx:
#             winners.append(vote)
#     return sorted(winners)[-1]
#
# print(vote_count(['ab', 'ba', 'ba', 'ab']))

# from math import inf
#
# def jumps(A):
#     possible = 0
#     last = len(A) - 1
#     for i in range(len(A)):
#         jump = 1
#         j = i
#         while j < len(A):
#             if jump % 2 != 0:
#                 mx = j
#                 diff = inf
#                 for k in range(j + 1, len(A)):
#                     d = abs(A[k] - A[j])
#                     if (A[k] > A[j]) and d < diff:
#                         mx = k
#                         diff = d
#                 if mx == last:
#                     possible += 1
#                     break
#                 else:
#                     if mx == j:
#                         break
#                     j = mx
#                 jump += 1
#             else:
#                 mn = j
#                 diff = inf
#                 for k in range(j + 1, len(A)):
#                     d = abs(A[k] - A[j])
#                     if (A[k] < A[j]) and d < diff:
#                         mn = k
#                         diff = d
#                 if mn == last:
#                     possible += 1
#                     break
#                 else:
#                     if mn == j:
#                         break
#                     j = mn
#                 jump += 1
#     return possible


# from collections import defaultdict
#
# def sub(s):
#     d = defaultdict(int)
#     prev = 'a'
#     for c in s:
#         if ord(c) - ord(prev) >= 0:
#             d[c] += 1
#             prev = c
#     return 0 if len(d) < 5 else sum(d.values())
#
# print(sub('aeiaaioooaauuaeiou'))
# print(sub('iuo'))
# print(sub('aeiou'))
# print(sub('aaioeoaauu'))


# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# def removeNodes(head, x):
#     result = ListNode(0)
#     result.next = head
#     prev = result
#     while head:
#         if head.val > x:
#             prev.next = head.next
#         else:
#             prev = prev.next
#         head = head.next
#     return result.next
#
# l = ListNode(45)
# l.next = ListNode(20)
# l.next.next = ListNode(30)
# l.next.next.next = ListNode(40)
# l.next.next.next.next = ListNode(15)
# l.next.next.next.next.next = ListNode(50)
# l.next.next.next.next.next.next = ListNode(5)
# l.next.next.next.next.next.next.next = ListNode(45)
#
# x = removeNodes(l, 35)


#
# def linked_list_length(alist):
#     val = alist[0]
#     count = 1
#     while val > 0 and count <= len(alist):
#         count += 1
#         val = alist[val]
#     return count if count <= len(alist) else 0
#
# # print(length_of_list([1, 4, -1, 3, 2]))
# # print(length_of_list([-1]))
#
#
# def get_max_diff(alist):
#     if len(alist) == 1:
#         return 0
#     i = 0
#     j = len(alist) - 1
#     d = abs(alist[i] - alist[j])
#     while i < j and d < 5000000:
#         # Case 1
#         if alist[i + 1] > alist[i]:
#             # Case 2
#             if alist[j - 1] < alist[j]:
#                 i += 1
#                 j -= 1
#             # Case 3
#             else:
#                 diff = abs(alist[i + 1] - alist[j])
#                 if diff > d:
#                     d = diff
#                 j -= 1
#         # Case 4
#         else:
#             d = abs(alist[i + 1] - alist[j])
#             i += 1
#     return d
#
# print(get_max_diff([10, 2, 44, 15, 39, 20]))
#
# l = [1, 6, 5]
# m = [1, 3, 5]
# print(min([l, m]))


# def missingNumber(nums):
#     length = len(nums)
#     rsum = (length / 2) * (length + 1)
#
#     left = 0
#     right = length - 1
#
#     while left <= right:
#         if left == right:
#             rsum -= nums[right]
#             break
#         rsum -= nums[left]
#         left += 1
#         rsum -= nums[right]
#         right -= 1
#
#     return int(rsum)
#
#
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


# from math import inf
#
# def maxProfit(prices):
#     n = len(prices)
#     if n < 2:
#         return 0
#     profit = 0
#     mn = inf
#     mx = 0
#     i = 0
#     while i < n:
#         while i < n and prices[i] < mn:
#             mn = prices[i]
#             i += 1
#         while i < n and prices[i] > mx:
#             mx = prices[i]
#             i += 1
#         if mx - mn > profit:
#             profit = mx - mn
#         if i < n and prices[i] < mn:
#             mn = prices[i]
#         mx = 0
#         i += 1
#
#     return profit
#
# print(maxProfit([2,1,2,1,0,0,1]))


# def numIslands(grid):
#     RMAX = len(grid)
#     CMAX = len(grid[0])
#     visited = [[False] * CMAX for _ in range(RMAX)]
#
#     def findRegion(row, col, region, visited):
#         if RMAX > row > -1 and CMAX > col > -1 and not visited[row][col]:
#             if grid[row][col] == '0':
#                 return region
#             visited[row][col] = True
#             findRegion(row - 1, col, region, visited)  # Top
#             findRegion(row + 1, col, region, visited)  # Bottom
#             findRegion(row, col - 1, region, visited)  # Left
#             findRegion(row, col + 1, region, visited)  # Right
#             region += 1
#         return region
#
#     regions = 0
#
#     for r in range(RMAX):
#         for c in range(CMAX):
#             if not visited[r][c]:
#                 regions += findRegion(r, c, 0, visited)
#
#     print(regions)
#
# numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])


# def threeSum(nums):
#     if len(nums) < 3:
#         return []
#     nums.sort()
#     res = set()
#     for i, v in enumerate(nums[:-2]):
#         if i >= 1 and v == nums[i - 1]:
#             continue
#         d = set()
#         for x in nums[i + 1:]:
#             if x not in d:
#                 d.add(-(v + x))
#             else:
#                 res.add((v, -(v + x), x))
#     return list(map(list, res))
#
# print(threeSum([-5,1,-3,-1,-4,-2,4,-1,-1]))


# def threeSum(nums):
#     res = []
#     nums.sort()
#     for i, v in enumerate(nums[:-2]):
#         if i > 0 and v == nums[i-1]:
#             continue
#         l, r = i+1, len(nums)-1
#         while l < r:
#             s = v + nums[l] + nums[r]
#             if s < 0:
#                 l += 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 res.append([v, nums[l], nums[r]])
#                 while l < r and nums[l] == nums[l+1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r-1]:
#                     r -= 1
#                 l += 1
#                 r -= 1
#     return res
#
# print(threeSum([-5,1,-3,-1,-4,-2,4,-1,-1]))


# def multiply(num1, num2):
#     ans = 0
#     for i in range(len(num1)):
#         for j in range(len(num2)):
#             ans += ((ord(num1[-i - 1]) - ord('0')) * 10 ** i) * ((ord(num2[-j - 1]) - ord('0')) * 10 ** j)
#     return str(ans)
#
# print(multiply('12', '6'))


# def wordSearch(board, word):
#     RMAX = len(board)
#     CMAX = len(board[0])
#
#     def search(row, col, idx, found, prev):
#         if not found:
#             if idx >= len(word):
#                 found = True
#                 return found
#             if RMAX > row > -1 and CMAX > col > -1:
#                 if board[row][col] is not word[idx]:
#                     return found
#                 directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
#                 for d in directions:
#                     if d not in prev:
#                         prev.add((row, col))
#                         found = search(d[0], d[1], idx + 1, found, prev)
#                         prev.remove(((row, col)))
#         return found
#
#     found = False
#     for r in range(RMAX):
#         for c in range(CMAX):
#             if found:
#                 break
#             found = search(r, c, 0, found, {(-1, -1)})
#         if found:
#             break
#
#     return found
#
# print(wordSearch([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))


# def treeToDoublyList(root):
#     def traverse(root, prev):
#         if not root:
#             return prev
#         prev = traverse(root.left, prev)
#         root.left = prev
#         prev.right = root
#         prev = root
#         prev = traverse(root.right, prev)
#         return prev
#
#     dummy = Node(None, None, None)
#     prev = dummy
#     prev = traverse(root, prev)
#     prev.right = dummy.right
#     dummy.right.left = prev
#     return dummy.right
#
# class Node(object):
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right
#
# root = Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(5, None, None))
#
# treeToDoublyList(root)


# class TrieNode:
#     def __init__(self, c):
#         self.char = c
#         self.children = {}
#
#
# def trie(words):
#     root = TrieNode('')
#     seen = {''}
#     for word in words:
#         # if len(word) > len(words):
#         #     continue
#         seen.add(word)
#         curr = root
#         for i in range(len(word)):
#             if word[i] not in curr.children:
#                 curr.children[word[i]] = TrieNode(word[i])
#             curr = curr.children[word[i]]
#     return root, seen
#
#
# def dfs(root, seen, acc, lookup):
#     if acc not in seen:
#         return lookup
#     for c in root.children:
#         acc += c
#         if acc in seen:
#             lookup = dfs(root.children[c], seen, acc, lookup)
#             if len(acc) > len(lookup[0]):
#                 lookup.clear()
#                 lookup.append(acc)
#             elif len(acc) == len(lookup[0]):
#                 lookup.append(acc)
#             acc = acc[:-1]
#         else:
#             acc = acc[:-1]
#     return lookup
#
#
# def longestWord(words):
#     root, seen = trie(words)
#     lookup = dfs(root, seen, '', [''])
#     print(min(lookup))
#
# # longestWord(["w","wo","wor","worl","world"])
# # longestWord(["a","banana","app","appl","ap","apply","apple"])
# longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"])


# def love_letter(letter):
#     result = []
#     for word in letter:
#         count = 0
#         l = 0
#         r = len(word) - 1
#         while l <= r:
#             if l == r:
#                 break
#             else:
#                 count += abs(ord(word[l]) - ord(word[r]))
#                 l += 1
#                 r -= 1
#         result.append(count)
#     print(result)
#
# love_letter(['abc', 'abcba', 'abcd'])


# from collections import defaultdict
#
# def findOrder(numCourses, prerequisites):
#     def topSort(graph, vertex, color, topStack):
#         color[vertex] = 1
#         for nbr in graph[vertex]:
#             if color[nbr] == 1:
#                 raise Exception
#             if color[nbr] == 0:
#                 topSort(graph, nbr, color, topStack)
#         color[vertex] = 2
#         topStack.append(vertex)
#
#     graph = defaultdict(list)
#
#     for u, v in prerequisites:
#         graph[v].append(u)
#
#     color = [0] * numCourses
#
#     topStack = []
#
#     for v in range(numCourses):
#         if color[v] == 0:
#             try:
#                 topSort(graph, v, color, topStack)
#             except:
#                 return []
#
#     return list(reversed(topStack))
#
# print(findOrder(2, [[0, 1], [1, 0]]))


# def threeSum(nums):
#     nums.sort()
#
#     result = []
#
#     i = 0
#     while i < (len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             i += 1
#             continue
#         left = i + 1
#         right = len(nums) - 1
#         while left < right:
#             three_sum = nums[i] + nums[left] + nums[right]
#             if three_sum < 0:
#                 left += 1
#             elif three_sum > 0:
#                 right -= 1
#             else:
#                 result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#         i += 1
#     return result
#
# print(threeSum([-1,0,1,2,-1,-4]))
