from typing import Tuple, Set, List, Optional


def print_maze(hex_maze: str, path: str, entry: Tuple[int, int],
               exit: Tuple[int, int], maze_color: str = "WHITE",
               explored: Optional[Set[Tuple[int, int]]] = None) -> None:
    """
    Prints a maze from its hexadecimal output as ASCII art in the terminal.
    Prints also the maze entry, exit and the solution.
    """
    WALL = 0
    EMPTY = 1
    ENTRY = 2
    EXIT = 3
    PATH = 4
    EXPLORED = 5

    if explored is None:
        explored = set()
    wall_colors = {
        "RED": '\033[91m',
        "GREEN": '\033[92m',
        "BLUE": '\033[94m',
        "YELLOW": '\033[33m',
        "WHITE": '\033[37m',
        "RESET": '\033[0m'
    }
    if maze_color.upper() not in wall_colors.keys():
        raise ValueError("Invalid color")
    reset = wall_colors["RESET"]
    maze_colors = {
        WALL: wall_colors[maze_color.upper()],
        EMPTY: reset,
        ENTRY: '\033[35m',
        EXIT: '\033[35m',
        PATH: '\033[36m',
        EXPLORED: '\033[33m'
    }

    hex_lines = hex_maze.splitlines()
    if not hex_lines:
        print("[Error]: Empty maze.")
        return
    height = len(hex_lines)
    width = len(hex_lines[0])

    grid = []
    for row in hex_lines:
        grid.append([int(c, 16) for c in row])
    canvas_h = 2 * height + 1
    canvas_w = 2 * width + 1
    canvas: List[List[int]] = [[EMPTY] * canvas_w for _ in range(canvas_h)]

    # Paint walls
    for i in range(height):
        for j in range(width):
            val = grid[i][j]
            if val & 1:
                canvas[2 * i][2 * j + 1] = WALL
                canvas[2*i][2*j] = WALL
                canvas[2*i][2*j+2] = WALL
            if val & 4:
                canvas[2 * i + 2][2 * j + 1] = WALL
                canvas[2*i+2][2*j] = WALL
                canvas[2*i+2][2*j+2] = WALL
            if val & 2:
                canvas[2 * i + 1][2 * j + 2] = WALL
                canvas[2*i][2*j+2] = WALL
                canvas[2*i+2][2*j+2] = WALL
            if val & 8:
                canvas[2 * i + 1][2 * j] = WALL
                canvas[2*i][2*j] = WALL
                canvas[2*i+2][2*j] = WALL

    # Paint explored cells
    for (ei, ej) in explored:
        if 0 <= ei < height and 0 <= ej < width:
            canvas[2*ei+1][2*ej+1] = EXPLORED

    # Paint path
    directions = {
         'N': (-1, 0),
         'S': (1, 0),
         'E': (0, 1),
         'W': (0, -1)
        }
    i, j = entry
    for step in path:
        di, dj = directions[step]
        canvas[2*i+1 + di][2*j+1 + dj] = PATH
        i += di
        j += dj
        canvas[2*i+1][2*j+1] = PATH

    # Paint entry and exit
    if 0 <= entry[0] < height and 0 <= entry[1] < width:
        canvas[2*entry[0]+1][2*entry[1]+1] = ENTRY
    if 0 <= exit[0] < height and 0 <= exit[1] < width:
        canvas[2*exit[0]+1][2*exit[1]+1] = EXIT

    C = '\u2588'
    for canvas_row in canvas:
        line: str = ""
        for cell in canvas_row:
            char: str = ' ' * 2 if cell == EMPTY else C * 2
            line += maze_colors[cell] + char
        print(line + reset)
