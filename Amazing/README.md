*This project was created as part of the 42 curriculum by yaqliu and nocrespo.*

# A-Maze-ing

## Description - Overview

A-Maze-ing is a Python maze generator and solver. It reads a text configuration file, builds a random maze, prints it as ASCII art in the terminal, and computes the shortest path from entry to exit.

The maze can also preserve a visible `42` pattern in the center when the maze is large enough, and the generation logic is available as a reusable `MazeGenerator` class in the `mazegen` package.

## INSTRUCTIONS
### Requirements

- Python 3.10 or later
- Dependencies listed in `requirements.txt`

## Setup

Create the virtual environment and install dependencies with:

```bash
make install
```

If you want to clean everything later, use:

```bash
make clean
```

## Run

The application reads `config.txt` by default.

```bash
make run
```

You can also run it manually and pass a different configuration file:

```bash
python3 a_maze_ing.py config.txt
python3 a_maze_ing.py my_config.txt
```

Other useful Makefile targets:

```bash
make all    # install dependencies and run the project
make lint   # run flake8 and mypy
make debug  # run the program under pdb
```

## Configuration File

The configuration file is a plain text file with one `KEY=VALUE` pair per line. Empty lines and lines starting with `#` are ignored.

Required keys:

| Key | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `WIDTH` | `int` | Maze width in cells | `WIDTH=20` |
| `HEIGHT` | `int` | Maze height in cells | `HEIGHT=15` |
| `ENTRY` | `tuple[int, int]` | Entry coordinates as `i, j` | `ENTRY=0,0` |
| `EXIT` | `tuple[int, int]` | Exit coordinates as `i, j` | `EXIT=14,19` |
| `OUTPUT_FILE` | `str` | Output filename ending in `.txt` | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | `bool` | `true` for a perfect maze, `false` to braid it | `PERFECT=true` |

Optional keys:

| Key | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `ALGORITHM` | `str` | Maze generator: `dfs` or `kruskal` | `ALGORITHM=kruskal` |
| `SOLVER` | `str` | Path solver: `bfs` or `astar` | `SOLVER=astar` |
| `SEED` | `int \| None` | Random seed for reproducible mazes | `SEED=42` |

Example configuration:

```txt
WIDTH=20
HEIGHT=20
ENTRY=9,9
EXIT=10,15
OUTPUT_FILE=maze.txt
ALGORITHM=dfs
PERFECT=true
SOLVER=astar
SEED=42
```

## Output Format

After generation, the program writes the maze to the configured output file using four sections:

```text
<hex maze>
<entry x,y>
<exit x,y>
<path as N/E/S/W letters>
```

The `hex maze` is the grid encoded as hexadecimal wall values, one row per line.

## Maze Generation

Two generation algorithms are available:

- `dfs` is the default algorithm. It uses a depth-first backtracker, starts from the entry point, and produces a perfect maze.
- `kruskal` is the bonus algorithm. It removes walls while maintaining connectivity with a union-find style approach, producing a different maze layout.

If `PERFECT=false`, the maze is braided after generation by opening additional walls where possible.

## Solving

Two solvers are implemented:

- `bfs` is the default solver and guarantees the shortest path.
- `astar` uses Manhattan distance as a heuristic and often explores fewer cells.

## Interactive Menu

After the maze is generated, the terminal menu lets you:

1. Re-generate a new maze
2. Show or hide the solution path
3. Rotate the display color
4. Animate the solving process
5. Animate maze generation
6. Play the maze interactively with WASD or arrow keys
7. Quit

## Reusable Package

The repository also includes a reusable package in `mazegen/` exposing `MazeGenerator`.
The `MazeGenerator` class is packaged as a standalone pip-installable module.
See the `mazegen` package at the root of the repository for installation and
usage instructions.

Build the package:
```bash
pip install build
python3 -m build
```

Install the package from the provided `.whl` file:
```bash
pip install mazegen-1.0.0-py3-none-any.whl
```
To uninstall:
```bash
pip uninstall mazegen
```

Basic usage:

```python
from mazegen import MazeGenerator

maze = MazeGenerator(
    width=20,
    height=15,
    maze_entry=(0, 0),
    maze_exit=(14, 19),
    perfect=True,
    output_file="maze.txt"
)

maze.generate()
```

Inspect the generated maze:

```python
output = maze.output_info()

print(output["hex_maze"])
print(output["path"])
print(output["entry"])
print(output["exit"])
```

## Project Notes

### Bonuses

- **Kruskal algorithm** — alternative maze generation algorithm selectable via `ALGORITHM=kruskal` in the config file.
- **A\* algorithm** — alternative solver, selectable via `SOLVER=astar`. Tends to explore fewer cells than BFS on large mazes.
- **Animated generation** — option 5 in the menu renders the maze being built step by step in the terminal.
- **Animated solving** — option 4 in the menu animates the solver exploring the maze in real time, showing visited cells as it searches for the exit.
- **Interactive game** — option 6 launches a curses-based game where the player navigates the maze manually using WASD or arrow keys, with a step counter and revisit tracking.

### Team and project management

#### Member Responsibilities
- `nocrespo`: input validation support, output file handling, maze rendering, A* solver, and the `mazegen` package
- `yaqliu`: config parsing and validation, DFS, BFS, Kruskal, and the interactive game bonus

What worked well was the parallel workflow — splitting responsibilities meant
we could progress on multiple fronts at once. The main thing we would improve
is defining shared interfaces and data structures more precisely at the start:
some parts had to be reworked when we merged our code because we had made
different assumptions independently.

## Resources

- AI was used to understand algorithm concepts, debug errors, and learn unfamiliar libraries such as 
curses and heapq.
- Algorisme's subject notes from UPC university.

## Authors

yaqliu and nocrespo