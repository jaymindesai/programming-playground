import random


def _give_random_grid(row, col):
    grid = []
    for no_rows in range(row):
        string = ''
        for no_cols in range(col):
            string = '%s%s' % (string, random.randint(0, 1))
        grid.append(string)
    return grid


random_rows1, random_rows2 = random.randint(5000, 5000), random.randint(5000, 5000)
random_cols1, random_cols2 = random.randint(5000, 5000), random.randint(5000, 5000)
grid1 = str(_give_random_grid(random_rows1, random_cols1))
grid2 = str(_give_random_grid(random_rows2, random_cols2))

pranav = """

LAND = '1'
WATER = '0'

def _init_visited(grid):
    no_rows = len(grid)
    no_cols = len(grid[0])
    return [[False]*no_cols for _ in range(no_rows)]

def _find_region(grid, row, col, current_region, visited):
    if (row >= len(grid)) or (row < 0) or (col < 0) or (col >= len(grid[0])):
        return current_region
    if grid[row][col] == WATER or visited[row][col]:
        return current_region
    else:
        visited[row][col] = True
        current_region.append(str(row)+str(col))
        _find_region(grid, row + 1, col, current_region, visited)
        _find_region(grid, row, col + 1, current_region, visited)
        _find_region(grid, row - 1, col, current_region, visited)
        _find_region(grid, row, col - 1, current_region, visited)
        return current_region

def _find_regions(grid):
    regions = []
    visited = _init_visited(grid)
    r = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (not visited[r][c]) and (grid[r][c] == LAND):
                regions.append(_find_region(grid, r, c, [], visited))
            c += 1
        r += 1
    return regions

def run(grid1, grid2):
    regions1 = _find_regions(grid1)
    regions2 = _find_regions(grid2)

    count = 0
    for r1 in regions1:
        for r2 in regions2:
            if set(r1) == set(r2):
                count += 1
    return count

grid1 = %s
grid2 = %s

run(grid1, grid2)

""" % (grid1, grid2)

jaymin = """

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
                left = int(grid[i][j - 1]) if (j - 1) >= 0 else -1
                top = int(grid[i - 1][j]) if (i - 1) >= 0 else -1
                right = int(grid[i][j + 1]) if (j + 1) < len(grid[i]) else -1
                cross_right = int(grid[i - 1][j + 1]) if (i - 1 >= 0 and j + 1 < len(grid[i-1])) else -1
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

grid1 = %s
grid2 = %s

get_connected_regions(grid1, grid2)

""" % (grid1, grid2)

import timeit

n = 10

# p = round(timeit.timeit(pranav, number=n) / n, 4)
j = round(timeit.timeit(jaymin, number=n) / n, 4)

# print('Pranav', p)
print('Jaymin', j)

# print(p / j)
