from input_validator import (
    ConfigurationError, MazeConfiguration,
    key_validation, check_config_file
)
from pydantic import ValidationError
from maze_generator import MazeGenerator
from print_maze import print_maze
from typing import Set, Tuple, Any, Dict
import sys
import os
import time
import random
import curses
import traceback


def play_maze(stdscr: curses.window, maze_obj: MazeGenerator) -> None:
    """
    Runs an interactive maze game in the terminal using curses.
    """
    curses.curs_set(0)
    stdscr.nodelay(False)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    py, px = maze_obj.maze_entry
    visited_count = {(py, px): 1}
    total_steps = 0
    if maze_obj.width >= 9 and maze_obj.height >= 7:
        forbidden = set(maze_obj.get_42_coord())
    else:
        forbidden = set()

    while True:
        stdscr.erase()
        h, w = stdscr.getmaxyx()

        if maze_obj.height * 2 + 2 > h or maze_obj.width * 4 + 1 > w:
            stdscr.addstr(0, 0, "⚠️ SCREEN IS TOO SMALL", curses.A_BOLD)
            stdscr.addstr(1, 0, "You need at least"
                          f"{maze_obj.width * 4 + 1}x{maze_obj.height * 2 + 3}"
                          )
            stdscr.addstr(2, 0, "Make window bigger or press 'Q' to quit.")
        else:
            for r in range(maze_obj.height):
                for c in range(maze_obj.width):
                    ty, tx = r * 2, c * 4
                    if not (0 <= ty < h - 2 and 0 <= tx < w - 4):
                        continue

                    bits = maze_obj.grid[r][c]
                    char = " "
                    color = curses.color_pair(0)
                    num_visited = visited_count.get((r, c), 0)

                    if (r, c) == (py, px):
                        char = "▼"
                        color = curses.color_pair(1) | curses.A_BOLD
                    elif (r, c) == maze_obj.maze_exit:
                        char = "X"
                        color = curses.color_pair(3) | curses.A_BOLD
                    elif (r, c) in forbidden:
                        char = "░"
                        color = curses.color_pair(4)
                    elif num_visited > 0:
                        char = "●"
                        color = curses.color_pair(6 if num_visited > 1 else 2)

                    try:
                        stdscr.addch(ty, tx, "+", curses.color_pair(5))
                        if bits & 1:
                            stdscr.addstr(ty, tx + 1, "---",
                                          curses.color_pair(5))
                        if bits & 8:
                            stdscr.addch(ty + 1, tx, "|", curses.color_pair(5))
                        stdscr.addstr(ty + 1, tx + 1, f" {char} ", color)
                        if c == maze_obj.width - 1 and (bits & 2):
                            stdscr.addch(ty + 1, tx + 4, "|",
                                         curses.color_pair(5))
                        if r == maze_obj.height - 1 and (bits & 4):
                            stdscr.addstr(ty + 2, tx + 1, "---",
                                          curses.color_pair(5))
                            stdscr.addch(ty + 2, tx, "+", curses.color_pair(5))
                            if c == maze_obj.width - 1:
                                stdscr.addch(ty + 2, tx + 4, "+",
                                             curses.color_pair(5))
                    except curses.error:
                        pass

        status = maze_obj.height * 2 + 1
        try:
            stdscr.addstr(status, 0, f" Steps: {total_steps} | Pos: {py, px} ",
                          curses.A_REVERSE)
            stdscr.addstr(status + 1, 0, "WASD/Arrows to move | Q to quit")
        except curses.error:
            pass

        stdscr.refresh()

        if (py, px) == maze_obj.maze_exit:
            try:
                stdscr.addstr(maze_obj.height * 2 + 2, 0,
                              "🏆 VICTORY! Press any key ...")
            except curses.error:
                pass
            stdscr.getch()
            break

        key = stdscr.getch()
        if key in [ord('q'), ord('Q')]:
            break

        new_py, new_px = py, px
        if key in [curses.KEY_UP, ord('w'), ord('W')]:
            if not (maze_obj.grid[py][px] & 1):
                new_py -= 1
        elif key in [curses.KEY_RIGHT, ord('d'), ord('D')]:
            if not (maze_obj.grid[py][px] & 2):
                new_px += 1
        elif key in [curses.KEY_DOWN, ord('s'), ord('S')]:
            if not (maze_obj.grid[py][px] & 4):
                new_py += 1
        elif key in [curses.KEY_LEFT, ord('a'), ord('A')]:
            if not (maze_obj.grid[py][px] & 8):
                new_px -= 1

        if (new_py, new_px) not in forbidden:
            if (new_py, new_px) != (py, px):
                total_steps += 1
                py, px = new_py, new_px
                visited_count[(py, px)] = visited_count.get((py, px), 0) + 1


def main() -> None:
    """
    Entry point of the application. Reads and validates a configuration
    file, generates the maze, and saves it to the output file. Then runs
    an interactive menu to re-generate, toggle the path, change colors,
    animate generation or solving, and play the maze in the terminal.
    """
    try:
        data: Dict[str, Any] = {}
        if len(sys.argv) == 1:
            config_file = "config.txt"
        elif len(sys.argv) == 2:
            config_file = sys.argv[1]
        elif len(sys.argv) > 2:
            raise ConfigurationError("too many arguments!")
        check_config_file(config_file)
        with open(config_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                elif "=" not in line:
                    raise ConfigurationError(
                        f"found an invalid line in config.txt: '{line}'"
                        )
                key, value = line.split("=", 1)
                data[key] = value
        key_validation(data)
        maze_data = MazeConfiguration(**data)
        maze = MazeGenerator(**maze_data.model_dump())
        maze.generate()
        output = maze.output_info()

        filename = maze.output_file
        with open(filename, "w") as file:
            entry_str = ",".join(map(str, output['entry']))
            exit_str = ",".join(map(str, output['exit']))
            content = (f"{output['hex_maze']}\n{entry_str}\n"
                       f"{exit_str}\n{output['path']}")
            file.write(content)

    except FileNotFoundError:
        sys.stderr.write(
            "config.txt not found, please make sure "
            "that the file exists.\n"
        )
        return
    except ValidationError as e:
        for error in e.errors():
            loc = error['loc'][0] if error['loc'] else "Validation Error"
            sys.stderr.write(f"{loc}: {error['msg']}\n")
            return
    except ConfigurationError as e:
        sys.stderr.write(f"Error: {e}\n")
        return
    except PermissionError as e:
        sys.stderr.write(f"Error: {e}\n")
        return
    show_path = True
    colors = ["WHITE", "RED", "YELLOW", "GREEN", "BLUE"]
    color_index = 0
    error_msg = ""

    while True:
        os.system('clear')
        curr_p = output['path'] if show_path else ""
        try:
            print_maze(output['hex_maze'], curr_p, output['entry'],
                       output['exit'], colors[color_index])
        except ValueError as e:
            sys.stderr.write(f"Error: {e}")
            return
        if error_msg:
            sys.stderr.write(f"\n{error_msg}\n")
            error_msg = ""

        print("\n=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Dynamic path")
        print("5. Dynamic maze")
        print("6. Playing mode")
        print("7. Quit")
        choice = input("\nChoice (1-7): ")

        if not choice.isdigit() or not (1 <= int(choice) <= 7):
            error_msg = f"Error: '{choice}' is not a valid option (1-7)"
            continue

        try:
            if choice == "1":
                params = maze_data.model_dump()
                params["seed"] = random.randint(0, 999999)
                maze = MazeGenerator(**params)
                maze.generate()
                output = maze.output_info()
                os.system('clear')
                current_path = output['path'] if show_path else ""
                print_maze(output['hex_maze'], current_path, output['entry'],
                           output['exit'], colors[color_index])
            elif choice == "2":
                if show_path is True:
                    print_maze(output['hex_maze'], "", output['entry'],
                               output['exit'], colors[color_index])
                    show_path = False
                elif show_path is False:
                    print_maze(output['hex_maze'], output['path'],
                               output['entry'], output['exit'],
                               colors[color_index])
                    show_path = True
            elif choice == "3":
                color_index = (color_index + 1) % len(colors)
                current_path = output['path'] if show_path else ""
                print_maze(output['hex_maze'], current_path, output['entry'],
                           output['exit'], colors[color_index])
            elif choice == "4":
                explored_cells: Set[Tuple[int, int]] = set()

                def render_step(current_maze: MazeGenerator, temp_path: str,
                                current_pos: Tuple[int, int]) -> None:
                    explored_cells.add(current_pos)
                    os.system('clear')
                    output = current_maze.output_info()
                    print_maze(output['hex_maze'], temp_path, output['entry'],
                               output['exit'], colors[color_index],
                               explored_cells)
                    time.sleep(0.08)
                print("\nSearching the path...")
                time.sleep(1)
                if maze.solver == "astar":
                    maze.astar(step_callback=render_step)
                else:
                    maze.bfs(step_callback=render_step)
                os.system('clear')
                output = maze.output_info()
                print_maze(output['hex_maze'], output['path'], output['entry'],
                           output['exit'], colors[color_index])
                show_path = True
            elif choice == "5":
                params = maze_data.model_dump()
                params["seed"] = maze.seed
                maze = MazeGenerator(**params)

                def render_frame(current_maze: MazeGenerator) -> None:
                    os.system('clear')
                    output = current_maze.output_info()
                    print_maze(output['hex_maze'], "", output['entry'],
                               output['exit'], colors[color_index])
                    time.sleep(0.05)

                maze.generate(step_callback=render_frame)
                output = maze.output_info()
                os.system('clear')
                current_path = output['path'] if show_path else ""
                print_maze(output['hex_maze'], current_path, output['entry'],
                           output['exit'], colors[color_index])

            elif choice == "6":
                curses.wrapper(play_maze, maze)
            elif choice == "7":
                print("Goodbye!\n")
                time.sleep(0.5)
                os.system('clear')
                break
        except ValueError as e:
            sys.stderr.write(f"Error: {e}")
        except (OSError, curses.error) as e:
            sys.stderr.write(f"System/Terminal error: {e}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\nProgram was manually stopped: Ctrl C detected\n")
    except Exception:
        traceback.print_exc()
        sys.exit(1)
