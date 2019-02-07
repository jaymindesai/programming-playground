def get_connected_regions(grid1, grid2):
    regions1 = find_regions(grid1)
    regions2 = find_regions(grid2)
    count = 0
    for region in regions1.keys():
        try:
            if regions1[region] == regions2[region]:
                count += 1
        except KeyError:
            pass
    return count


def find_regions(image):
    grid = []
    for k in image:
        grid.append(list(k))
    marker = 1
    regions = {}
    marker_mapping = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                idx = str(i) + '#' + str(j)
                top, left, right, cross_right = get_neighbours(grid, i, j)
                if top > 1 or left > 1:
                    later = max(top, left)
                    previous = min(top, left)
                    regions[marker_mapping[later]].add(idx)
                    grid[i][j] = str(later)
                    if 1 < previous < later:
                        for region in regions[marker_mapping[later]]:
                            ix, jx = region.split('#')
                            grid[int(ix)][int(jx)] = str(previous)
                            regions[marker_mapping[previous]].add(region)
                        del regions[marker_mapping[later]]
                        del marker_mapping[later]
                elif cross_right > 1 and right == 1:
                    regions[marker_mapping[cross_right]].add(idx)
                    grid[i][j] = str(cross_right)
                else:
                    marker += 1
                    regions[idx] = set()
                    marker_mapping[marker] = idx
                    regions[idx].add(idx)
                    grid[i][j] = str(marker)
    return regions


def get_neighbours(grid, i, j):
    top = int(grid[i - 1][j]) if (i - 1) >= 0 else -1
    left = int(grid[i][j - 1]) if (j - 1) >= 0 else -1
    right = int(grid[i][j + 1]) if (j + 1) < len(grid[i]) else -1
    cross_right = int(grid[i - 1][j + 1]) if (i - 1 >= 0 and j + 1 < len(grid[i - 1])) else -1
    return top, left, right, cross_right

# import random
#
# def _give_random_grid(row, col):
#     grid = []
#     for no_rows in range(row):
#         string = ''
#         for no_cols in range(col):
#             string = '%s%s'%(string, random.randint(0,1))
#         grid.append(string)
#     return grid

# grid6 = ['001', '011', '101']

# def _pretty_print_me(grid):
#     for string in grid:
#         pretty_babes = ''
#         for character in string:
#             pretty_babes = '%-3s %-3s'%(pretty_babes, character)
#         print(pretty_babes)

# for i in range(5000):
#     random_rows1, random_rows2 = random.randint(5, 15), random.randint(5, 15)
#     random_cols1, random_cols2 = random.randint(5, 15), random.randint(5, 15)
#     q1 = _give_random_grid(random_rows1, random_cols1)
#     q2 = _give_random_grid(random_rows2, random_cols2)
#     _pretty_print_me(q1)
#     print('------')
#     _pretty_print_me(q2)
#     print('------')
#     print('ANS', get_connected_regions(q1, q2))
#     print('-------------------')
