*This package has been created as part of the 42 curriculum by yaqliu and nocrespo.*

# mazegen

## Description

`mazegen` is a reusable Python package that provides a maze generator and solver.
It exposes a single `MazeGenerator` class that can be imported into any Python
project to generate, solve, and inspect mazes.


## Instructions

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

## Usage

### Basic example

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
> **Note:** If invalid values are provided, undefined behaviour will occur. Correct types and format can be found in `Custom Parameters` (see bellow). 

Inspect the generated maze:

```python
output = maze.output_info()

print(output["hex_maze"])
print(output["path"])
print(output["entry"])
print(output["exit"])
```

### Custom parameters
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

### Accessing the maze structure and solution

```python
output = maze.output_info()

print(output['hex_maze'])  # hexadecimal grid, one row per line
print(output['path'])      # solution as a string of N, E, S, W characters
print(output['entry'])     # entry coordinates as tuple
print(output['exit'])      # exit coordinates as tuple
```

**Author**
yaqliu and nocrespso - 42students