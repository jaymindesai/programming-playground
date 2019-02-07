def sudoku(puzzle):
    # count = 0
    # for i in range(9):
    #     for j in range(9):
    #         if puzzle[i][j] == 0:
    #             count += 1
    # if count == 0:
    #     return puzzle
    return fill_sudoku(puzzle, 0, [])
    # puzzle = fill_sudoku(puzzle, 0, [])
    # for i in range(9):
    #     for j in range(9):
    #         values = find_possible_values(puzzle, i, j)
    #         if len(values) > 1:
    #             return []
    # return puzzle


def fill_sudoku(puzzle, count, lookup):
    if count > 1:
        if 1 not in lookup:
            return []
    if count == 81:
        return puzzle
    lookup = []
    for i in range(9):
        for j in range(9):
            values = find_possible_values(puzzle, i, j)
            lookup.append(len(values))
            if len(values) < 1:
                return []
            elif len(values) == 1:
                puzzle[i][j] = values[0]
    return fill_sudoku(puzzle, count + 1, lookup)


# noinspection PyBroadException
def find_possible_values(puzzle, row, col):
    m = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if puzzle[row][col] != 0:
        return puzzle[row][col]
    for i in m[row // 3]:
        for j in m[col // 3]:
            try:
                values.remove(puzzle[i][j])
            except:
                pass
    for i in range(9):
        try:
            values.remove(puzzle[row][i])
        except:
            pass
        try:
            values.remove(puzzle[i][col])
        except:
            pass
    return values
