import random
from typing import Dict, Tuple, List, Any, Optional, Callable
from collections import deque
import heapq


class MazeGenerator:
    """
    Class responsible for generating mazes
    """
    def __init__(self, width: int, height: int, maze_entry: tuple[int, int],
                 maze_exit: tuple[int, int], perfect: bool, output_file: str,
                 algorithm: str = "dfs", solver: str = "bfs",
                 seed: int | None = None):
        self.width = width
        self.height = height
        self.maze_entry = maze_entry
        self.maze_exit = maze_exit
        self.perfect = perfect
        self.algorithm = algorithm
        self.solver = solver
        self.output_file = output_file
        self.grid = [[15 for _ in range(width)] for _ in range(height)]
        if seed is not None:
            self.seed = seed
        else:
            self.seed = random.randint(0, 999999)
        random.seed(self.seed)

    def break_walls(self, row: int, col: int, direction: str) -> None:
        """
        Helper function to break walls during maze creation
        """
        if direction == "NORTH":
            self.grid[row][col] &= ~1
            self.grid[row - 1][col] &= ~4
        elif direction == "SOUTH":
            self.grid[row][col] &= ~4
            self.grid[row + 1][col] &= ~1
        elif direction == "EAST":
            self.grid[row][col] &= ~2
            self.grid[row][col + 1] &= ~8
        elif direction == "WEST":
            self.grid[row][col] &= ~8
            self.grid[row][col - 1] &= ~2
        if hasattr(self, 'step_callback') and self.step_callback:
            self.step_callback(self)

    def output_info(self) -> Dict[str, Any]:
        hex_matrix = [[str(hex(i)[2:].upper()) for i in row]
                      for row in self.grid]
        hex_list = ["".join(val_row) for val_row in hex_matrix]
        result = "\n".join(hex_list) + "\n"
        if hasattr(self, 'solver') and self.solver == 'astar':
            path = self.astar()
        else:
            path = self.bfs()
        return {
            "hex_maze": result,
            "path": path,
            "entry": self.maze_entry,
            "exit": self.maze_exit
        }

    def get_42_coord(self) -> List[Tuple[int, int]]:
        w = self.width
        h = self.height
        i0 = ((h - 5) // 2)
        j0 = ((w - 7) // 2)
        result = [
            (i0, j0), (i0, j0 + 4), (i0, j0 + 5), (i0, j0 + 6),
            (i0 + 1, j0), (i0 + 1, j0 + 6),
            (i0 + 2, j0), (i0 + 2, j0 + 1), (i0 + 2, j0 + 2),
            (i0 + 2, j0 + 4), (i0 + 2, j0 + 5), (i0 + 2, j0 + 6),
            (i0 + 3, j0 + 2), (i0 + 3, j0 + 4),
            (i0 + 4, j0 + 2), (i0 + 4, j0 + 4), (i0 + 4, j0 + 5),
            (i0 + 4, j0 + 6)
        ]
        return result

    def dfs(self, start_i: int, start_j: int) -> None:
        if not (0 <= start_i < self.height and 0 <= start_j < self.width):
            return
        visited = [
            [False for _ in range(self.width)] for _ in range(self.height)
        ]
        if self.width >= 9 and self.height >= 7:
            get_42_pattern = self.get_42_coord()
            for i, j in get_42_pattern:
                visited[i][j] = True
        stack = [(start_i, start_j)]
        visited[start_i][start_j] = True

        while stack:
            i, j = stack[-1]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            coord: Dict[Tuple[int, int], str] = {
                (-1, 0): "NORTH",
                (0, 1): "EAST",
                (1, 0): "SOUTH",
                (0, -1): "WEST"
            }
            random.shuffle(directions)
            moved = False

            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                if (
                    0 <= new_i < self.height
                    and 0 <= new_j < self.width
                    and not visited[new_i][new_j]
                ):
                    visited[new_i][new_j] = True
                    stack.append((new_i, new_j))
                    mov_dir = coord[(dx, dy)]
                    self.break_walls(i, j, mov_dir)
                    moved = True
                    break
            if not moved:
                stack.pop()

    def bfs(self, step_callback: Optional[Callable] = None) -> str:
        """
        Finds shortest path using BFS algorithm.
        Returns Path as string of N, E, S, W characters
        """
        start = self.maze_entry
        goal = self.maze_exit
        directions = [
            (-1, 0, 1, 'N'),
            (0, 1, 2, 'E'),
            (1, 0, 4, 'S'),
            (0, -1, 8, 'W'),
        ]
        parent: Dict[Tuple[int, int], Any] = {start: (None, "")}
        queue = deque([start])
        while queue:
            current_r, current_c = queue.popleft()
            if step_callback:
                temp_path = []
                temp_pos = (current_r, current_c)
                while parent[temp_pos][0] is not None:
                    parent_coord, letter = parent[temp_pos]
                    temp_path.append(letter)
                    temp_pos = parent_coord
                temp_path_str = "".join(reversed(temp_path))
                step_callback(self, temp_path_str, (current_r, current_c))

            if (current_r, current_c) == goal:
                path = []
                current_pos = (current_r, current_c)
                while parent[current_pos][0] is not None:
                    parent_coord, letter = parent[current_pos]
                    path.append(letter)
                    current_pos = parent_coord
                return "".join(reversed(path))

            for dr, dc, bit, dir_letter in directions:
                new_r = current_r + dr
                new_c = current_c + dc
                if 0 <= new_r < self.height and 0 <= new_c < self.width:
                    if not (self.grid[current_r][current_c] & bit):
                        if (new_r, new_c) not in parent:
                            parent[(new_r, new_c)] = (
                                (current_r, current_c), dir_letter)
                            queue.append((new_r, new_c))
        return "Unsolvable maze"

    def make_braid(self) -> None:
        coords_42 = (
            set(self.get_42_coord())
            if (self.width >= 9 and self.height >= 7)
            else set()
        )
        maze = self.grid
        WALL_INFO = {
            1: (-1, 0, "NORTH"),
            2: (0, 1, "EAST"),
            4: (1, 0, "SOUTH"),
            8: (0, -1, "WEST")
        }
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (maze[i][j].bit_count() == 3):
                    valid_walls_to_break = []
                    for bit, (di, dj, dir) in WALL_INFO.items():
                        if maze[i][j] & bit:
                            ni, nj = i + di, j + dj
                            in_bounds = (
                                0 <= ni < self.height
                                and 0 <= nj < self.width
                            )
                            not_42 = (ni, nj) not in coords_42
                            if in_bounds and not_42:
                                valid_walls_to_break.append(dir)
                    if valid_walls_to_break:
                        mov_dir = random.choice(valid_walls_to_break)
                        self.break_walls(i, j, mov_dir)

    def find_parent(self, parent: Dict[Tuple[int, int], Tuple[int, int]],
                    cell: Tuple[int, int]) -> Tuple[int, int]:
        root = cell
        while parent[root] != root:
            root = parent[root]
        curr = cell
        while parent[curr] != root:
            next_node = parent[curr]
            parent[curr] = root
            curr = next_node
        return root

    def _kruskal(self) -> None:
        parent = {
            (r, c): (r, c)
            for r in range(self.height)
            for c in range(self.width)
        }
        forbidden = (
            set(self.get_42_coord())
            if self.width >= 9 and self.height >= 7
            else set()
        )
        walls_list = []
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) in forbidden:
                    continue
                if c + 1 < self.width and (r, c + 1) not in forbidden:
                    walls_list.append((r, c, r, c + 1, "EAST"))
                if r + 1 < self.height and (r + 1, c) not in forbidden:
                    walls_list.append((r, c, r + 1, c, "SOUTH"))

        random.shuffle(walls_list)
        for r, c, nr, nc, direction in walls_list:
            parent1 = self.find_parent(parent, (r, c))
            parent2 = self.find_parent(parent, (nr, nc))
            if parent1 != parent2:
                self.break_walls(r, c, direction)
                parent[parent1] = parent2

    def generate(self, step_callback: Optional[Callable] = None) -> None:
        self.step_callback = step_callback
        if self.algorithm == "dfs":
            self.dfs(0, 0)
        else:
            self._kruskal()
        if not self.perfect:
            self.make_braid()

    def astar(self, step_callback: Optional[Callable] = None) -> str:
        """
        Finds shortest path using A* algorithm.
        Returns Path as string of N, E, S, W characters
        """
        start = self.maze_entry
        goal = self.maze_exit
        directions = [
            (-1, 0, 1, 'N'),
            (0, 1, 2, 'E'),
            (1, 0, 4, 'S'),
            (0, -1, 8, 'W'),
        ]
        forbidden = (
            set(self.get_42_coord())
            if self.width >= 9 and self.height >= 7
            else set()
        )

        def heuristic(pos: Tuple[int, int]) -> float:
            """
            Manhattan distance from pos to exit.
            """
            h = abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
            """
            Tie-breaker: priorizes stright lines
            """
            dx1, dy1 = pos[1] - goal[1], pos[0] - goal[0]
            dx2, dy2 = start[1] - goal[1], start[0] - goal[0]
            diff = abs(dx1 * dy2 - dx2 * dy1)
            return h + diff * 0.01

        weight = 1.7
        heap = [(heuristic(start) * weight, 0, start)]
        parent: Dict[Tuple[int, int], Any] = {start: (None, "")}
        g_score = {start: 0}

        while heap:
            f, neg_g, (current_r, current_c) = heapq.heappop(heap)
            g = -neg_g
            if g > g_score.get((current_r, current_c), float('inf')):
                continue
            if step_callback:
                temp_path = []
                temp_pos = (current_r, current_c)
                while parent[temp_pos][0] is not None:
                    parent_coord, letter = parent[temp_pos]
                    temp_path.append(letter)
                    temp_pos = parent_coord
                temp_path_str = "".join(reversed(temp_path))
                step_callback(self, temp_path_str, (current_r, current_c))

            if (current_r, current_c) == goal:
                path = []
                current_pos = goal
                while parent[current_pos][0] is not None:
                    parent_coord, letter = parent[current_pos]
                    path.append(letter)
                    current_pos = parent_coord
                return "".join(reversed(path))

            for dr, dc, bit, dir_letter in directions:
                new_r = current_r + dr
                new_c = current_c + dc
                if 0 <= new_r < self.height and 0 <= new_c < self.width:
                    cell = self.grid[current_r][current_c]
                    if not (cell & bit) and (new_r, new_c) not in forbidden:
                        new_g = g + 1
                        if new_g < g_score.get((new_r, new_c), float('inf')):
                            g_score[(new_r, new_c)] = new_g
                            wh = weight * heuristic((new_r, new_c))
                            f_priority = new_g + wh
                            parent[(new_r, new_c)] = ((current_r, current_c),
                                                      dir_letter)
                            heapq.heappush(heap, (f_priority, -new_g,
                                           (new_r, new_c)))
        return "Unsolvable maze"
