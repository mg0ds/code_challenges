import numpy as np

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    visited = []
    visited_number = [1]
    direction_list = ["start"]
    
    def neighbour_check(grid, start_i, start_j, direction = None):
        visited.append([start_i, start_j])
        available_moves = []
        available_moves_poz = []
        moves = ((0, 1, RIGHT), (1, 0, DOWN), (-1, 0, UP), (0, -1, LEFT))
        for x, y, direction in moves:
            if [int(start_i) + x, int(start_j) + y] not in visited and \
                    ((int(start_i) + x) < len(grid) and (int(start_j) + y) < len(grid)) and \
                    ((int(start_i) + x) > -1 and (int(start_j) + y) > -1):
                available_moves.append([grid[int(start_i) + x][int(start_j) + y], direction])
                available_moves_poz.append([int(start_i) + x, int(start_j) + y, direction])
        if available_moves == []:
            return None
        else:
            next_step = available_moves_poz[available_moves.index(min(available_moves))]
            direction_list.append(next_step[2])
            if len(direction_list) > 2 and str(direction_list[-2]) != str(next_step[2]):
                visited_number.append(next_step[2])
                visited_number.append("\n")
                visited_number.append(grid[next_step[0]][next_step[1]])
            else:
                visited_number.append(grid[next_step[0]][next_step[1]])
            neighbour_check(grid, next_step[0], next_step[1], next_step[2])


    new_grid = grid.split("\n")
    clean_grid = []
    a = 0
    for i in new_grid:
        clean_grid.append([])
        for j in i.split():
            try:
                clean_grid[a].append(int(j))
            except:
                continue
        a += 1
    clean_grid = [element for element in clean_grid if element != []]
    # 1 location in grid:
    np_clean_grid = np.array(clean_grid)
    i, j = np.where(np_clean_grid == 1)
    neighbour_check(clean_grid, i[0], j[0])
    print(*visited_number)
