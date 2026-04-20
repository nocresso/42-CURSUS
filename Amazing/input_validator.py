from pydantic import (BaseModel, Field, model_validator,
                      field_validator)
from typing import Tuple, Optional, Literal, Dict, Any, List, Union
from pathlib import Path
import os


class ConfigurationError(Exception):
    """
    Custom exception for invalid maze configuration errors.
    """
    def __init__(self, extra_info: str = ""):
        self.base_msg = "Invalid configuration"
        if extra_info:
            self.full_msg = f"{self.base_msg}, {extra_info}"
        else:
            self.full_msg = self.base_msg
        super().__init__(self.full_msg)


class MazeConfiguration(BaseModel):
    """
    Pydantic model that validates all the maze parameters.
    """
    width: int = Field(gt=0, alias='WIDTH')
    height: int = Field(gt=0, alias='HEIGHT')
    maze_entry: Tuple[int, int] = Field(default=(0, 0), alias='ENTRY')
    maze_exit: Tuple[int, int] = Field(default=(0, 1), alias='EXIT')
    output_file: str = Field(min_length=3, max_length=20, alias='OUTPUT_FILE')
    perfect: bool = Field(default=True, alias='PERFECT')
    algorithm: Literal["dfs", "kruskal"] = Field(
        default="dfs", alias='ALGORITHM'
    )
    solver: Literal["bfs", "astar"] = Field(
        default="bfs", alias="SOLVER"
    )
    seed: Optional[int] = Field(default=None, alias='SEED')

    @field_validator('maze_entry', 'maze_exit', mode='before')
    @classmethod
    def parse_tuple(cls, value: Union[str, tuple]) -> Union[tuple, None]:
        """
        Function for entry and exit coordinates validation
        """
        if isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError("Needed 2 coordinates")
            try:
                return (int(value[0]), int(value[1]))
            except ValueError:
                raise ValueError("invalid coordinates "
                                 "(must be positive integers)")
        if isinstance(value, str):
            try:
                split_value: List[str] = value.split(",")
                if len(split_value) != 2:
                    raise ValueError("Needed 2 coordinates,"
                                     " separated with a coma")
                return (int(split_value[0].strip()),
                        int(split_value[1].strip()))
            except ValueError:
                raise ValueError("invalid coordinates "
                                 "(must be positive integers)")
        raise ValueError("invalid format")

    @field_validator('algorithm', mode='before')
    @classmethod
    def transform_to_lower(cls, name: str) -> str:
        """
        Normalizes the algorithm name to lowercase before validation.
        """
        return name.lower()

    @model_validator(mode='after')
    def validate_maze_logic(self) -> 'MazeConfiguration':
        """
        Validates cross-field constraints after all fields are set.
        """
        row_in, col_in = self.maze_entry
        row_out, col_out = self.maze_exit

        if not (0 <= row_in < self.height and 0 <= col_in < self.width):
            raise ValueError(
                f"ENTRY {self.maze_entry} is out of the maze "
                f"({self.height} x {self.width})"
            )
        if not (0 <= row_out < self.height and 0 <= col_out < self.width):
            raise ValueError(
                f"EXIT {self.maze_exit} is out of the maze "
                f"({self.height} x {self.width})"
            )
        if self.maze_entry == self.maze_exit:
            raise ValueError(
                "Invalid configuration, ENTRY and EXIT "
                "can not be the same point"
            )

        if self.width >= 9 and self.height >= 7:
            w = self.width
            h = self.height
            i0 = ((h - 5) // 2)
            j0 = ((w - 7) // 2)
            forbidden_coord = [
                (i0, j0), (i0, j0 + 4), (i0, j0 + 5), (i0, j0 + 6),
                (i0 + 1, j0), (i0 + 1, j0 + 6),
                (i0 + 2, j0), (i0 + 2, j0 + 1), (i0 + 2, j0 + 2),
                (i0 + 2, j0 + 4), (i0 + 2, j0 + 5), (i0 + 2, j0 + 6),
                (i0 + 3, j0 + 2), (i0 + 3, j0 + 4),
                (i0 + 4, j0 + 2), (i0 + 4, j0 + 4), (i0 + 4, j0 + 5),
                (i0 + 4, j0 + 6)
            ]
            if self.maze_entry in forbidden_coord:
                raise ValueError(
                    f"Invalid ENTRY {self.maze_entry}. "
                    "Overlaping with the central drawing."
                )
            if self.maze_exit in forbidden_coord:
                raise ValueError(
                    f"Invalid EXIT {self.maze_exit}. "
                    "Overlaping with the central drawing."
                )
        if not self.output_file.endswith(".txt"):
            raise ValueError("Invalid file type: OUTPUT_FILE must be .txt")
        if not check_output_path(self.output_file):
            raise PermissionError(
                f"Do not have permission to WRITE on '{self.output_file}'")
        return self


def key_validation(config: Dict[str, Any]) -> None:
    """
    Checks that all required keys are present in the config dictionary.
    """
    required_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                     "PERFECT"]
    accepted_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                     "PERFECT", "ALGORITHM", "SOLVER", "SEED"]
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(
                f"{key} not found"
            )
    for config_keys in config:
        if config_keys not in accepted_keys:
            raise ConfigurationError(
                f"invalid key found '{config_keys}'"
                f"\nAllowed keys {accepted_keys}"
            )


def check_config_file(file_path: str) -> None:
    """
    Validates the existence and format of the configuration file.
    """
    path = Path(file_path)

    if not path.exists():
        raise ConfigurationError(f"{file_path} does not exist")

    if not path.is_file():
        raise ConfigurationError(f"{file_path} is not a valid file")

    if path.suffix != ".txt":
        raise ConfigurationError("configuration file needs to be .txt")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"do not have permission to READ from '{path}'")

    keys: List[str] = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            elif "=" not in line:
                raise ConfigurationError(
                    f"found an invalid line in config.txt: '{line}'"
                    )
            key, _ = line.split("=", 1)
            clean_key = key.strip().upper()
            keys.append(clean_key)
    if len(keys) != len(set(keys)):
        import collections
        dupes = [k for k, v in collections.Counter(keys).items() if v > 1]
        raise ConfigurationError(f"there are duplicated keys: {dupes}")


def check_output_path(file_path: str) -> bool:
    path = Path(file_path).resolve()
    for parent in path.parents:
        if parent.exists():
            if not os.access(parent, os.X_OK):
                return False
        else:
            return False
    if path.exists():
        return os.access(path, os.W_OK)
    if not path.parent.exists():
        return False
    return os.access(path.parent, os.W_OK)
