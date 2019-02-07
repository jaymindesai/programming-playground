def numIslands(grid):
    if len(grid) == 0:
        return 0

    R = len(grid)
    C = len(grid[0])

    def _findRegion(grid, row, col):
        if R > row > -1 and C > col > -1 and grid[row][col] != '0':
            grid[row][col] = '0'
            _findRegion(grid, row - 1, col)  # Top
            _findRegion(grid, row + 1, col)  # Bottom
            _findRegion(grid, row, col - 1)  # Left
            _findRegion(grid, row, col + 1)  # Right

    regions = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1':
                regions += 1
                _findRegion(grid, r, c)

    return regions


print(numIslands([["1", "1", "1", "1", "0"],
                  ["1", "1", "0", "1", "0"],
                  ["1", "1", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"]]))
