from pydantic import (BaseModel, Field, field_validator,
                      model_validator, ConfigDict)
from typing import Tuple, List, Dict, Any, Optional
from enum import Enum
from pathlib import Path
import os


class MapParsingError(Exception):
    """
    Custom exception for invalid map configuration errors.
    """
    def __init__(self, extra_info: str = ""):
        self.base_msg = "Map parsing error"
        if extra_info:
            self.full_msg = f"{self.base_msg}, {extra_info}"
        else:
            self.full_msg = self.base_msg
        super().__init__(self.full_msg)


class ZoneType(Enum):
    """
    Defines the possible zone types for a hub in the network.
    """
    normal = "normal"
    blocked = "blocked"
    restricted = "restricted"
    priority = "priority"


class HubType(Enum):
    """
    Defines the role of a hub in the network.
    """
    start = "start"
    end = "end"
    normal = "normal"


class Hub(BaseModel):
    """
    Represents a node in the drone network.
    """
    model_config = ConfigDict(frozen=False)
    name: str
    coordinates: Tuple[int, int]
    zone: ZoneType = Field(default=ZoneType.normal)
    color: Optional[str] = Field(default=None)
    max_drones: int = Field(ge=1, default=1)
    hub_type: HubType = Field(default=HubType.normal)

    @property
    def cost(self) -> int:
        """
        Set movement cost to enter this hub.
        """
        if self.zone == ZoneType.normal or self.zone == ZoneType.priority:
            return 1
        elif self.zone == ZoneType.restricted:
            return 2
        else:
            raise ValueError(f"Zone {self.name} is blocked")

    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        """
        Validate that the hub name is non-empty and contains no dashes.
        """
        if not value:
            raise ValueError("hub name cannot be empty")
        if '-' in value:
            raise ValueError("hub name cannot contain dashes")
        return value


class Connection(BaseModel):
    """
    Represents a bidirectional link between two hubs.
    """
    zone1: Hub
    zone2: Hub
    max_link_capacity: int = Field(ge=1, default=1)


class NetworkConfiguration(BaseModel):
    """
    Represents the full network configuration parsed from a map file.
    """
    drone_nb: int = Field(ge=1)
    hubs: List[Hub]
    connections: List[Connection]

    @model_validator(mode='after')
    def validate_map(self) -> 'NetworkConfiguration':
        """
        Validate the overall network configuration.
        Ensures exactly one start and one end hub exist,
        hub names are unique, and connections are not duplicated.
        Returns the validated configuration instance.
        """
        start_hub = 0
        end_hub = 0
        names = []
        coord_check = []
        for hub in self.hubs:
            names.append(hub.name)
            coord_check.append(hub.coordinates)
            if hub.hub_type == HubType.start:
                start_hub += 1
            elif hub.hub_type == HubType.end:
                end_hub += 1
        if len(coord_check) != len(set(coord_check)):
            raise MapParsingError("map with duplicate coordinates")
        if start_hub != 1 or end_hub != 1:
            raise MapParsingError("map must have one start and one end zones")
        if len(names) != len(set(names)):
            raise MapParsingError("duplicate hub names found")
        connections = [frozenset([c.zone1.name, c.zone2.name])
                       for c in self.connections]
        if len(connections) < 1:
            raise MapParsingError("map without connections")
        if len(connections) != len(set(connections)):
            raise ValueError("duplicate connections found")
        return self


def parse_hub(line: str, hub_type: HubType) -> 'Hub':
    """
    Parse a hub definition line and return a Hub instance.
    """
    try:
        data = line.split("[")
        zone_info = data[0].split()
        if not zone_info or len(zone_info) < 3:
            raise MapParsingError("missing hub information in"
                                  f" line 'hub: {line}'")
        name = zone_info[0]
        coordinates = (int(zone_info[1]), int(zone_info[2]))
        zone = ZoneType.normal
        color: Optional[str] = None
        max_drones = 1

        if len(data) > 1:
            metadata = data[1].split()
            for info in metadata:
                clean_data = info.split("=")[1].strip("] ")
                if info.startswith("zone"):
                    zone = ZoneType(clean_data)
                elif info.startswith("color"):
                    color = clean_data
                elif info.startswith("max_drones"):
                    max_drones = int(clean_data)
    except MapParsingError:
        raise
    except Exception:
        raise MapParsingError(f"invalid hub input data 'hub: {line}'")
    return Hub(name=name,
               coordinates=coordinates,
               zone=zone,
               color=color,
               max_drones=max_drones,
               hub_type=hub_type)


def parse_connection(line: str, hub_list: List[Hub]) -> 'Connection':
    """
    Parse a connection line and return a Connection instance.
    """
    try:
        data = line.split("[")
        zones = data[0].split("-")
        if len(zones) != 2:
            raise ValueError
        zone1 = next((h for h in hub_list if h.name == zones[0].strip()), None)
        zone2 = next((h for h in hub_list if h.name == zones[1].strip()), None)
        if zone1 is None or zone2 is None:
            raise MapParsingError("invalid connection zones")
        max_link_capacity = 1
        if len(data) > 1:
            if data[1].startswith("max_link_capacity"):
                data = data[1].split("=")
                clean_data = data[1].strip("]\n")
                max_link_capacity = int(clean_data)
        else:
            max_link_capacity = 1
    except (ValueError, IndexError):
        raise MapParsingError("invalid connection input data")

    return Connection(zone1=zone1, zone2=zone2,
                      max_link_capacity=max_link_capacity)


def check_input_file(file_path: str) -> Dict[str, Any]:
    """
    Read and validate a map configuration file.
    Returns a dictionary suitable for constructing a class NetworkConfiguration
    """

    drone_nb: int = 0
    hubs: List[Hub] = []
    connections: List[Connection] = []
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")

    if not path.is_file():
        raise FileNotFoundError(f"{file_path} is not a valid file")

    if path.suffix != ".txt":
        raise MapParsingError("configuration file needs to be .txt")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"do not have permission to READ from '{path}'")

    with open(path, "r") as file:
        lines = file.readlines()
        if not lines or not any(line.strip() for line in lines):
            raise MapParsingError("empty file")
        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            if "nb_drones" not in line:
                raise MapParsingError("First valid line"
                                      " should be drone number.")
            else:
                drones, num = line.split(":")
                drone_nb = int(num.strip())
                break

        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            elif ":" not in line:
                raise MapParsingError("found an invalid line in input file:"
                                      f" '{line}'")
            elif line.startswith("hub"):
                hub_line = line.split(":")
                hub = parse_hub(hub_line[1], HubType.normal)
                hubs.append(hub)
            elif line.startswith("start_hub"):
                start_line = line.split(":")
                start_hub = parse_hub(start_line[1], HubType.start)
                hubs.append(start_hub)
            elif line.startswith("end_hub"):
                end_line = line.split(":")
                end_hub = parse_hub(end_line[1], HubType.end)
                hubs.append(end_hub)
            elif line.startswith("connection") or line.startswith("nb_drones"):
                pass
            else:
                raise MapParsingError("found an invalid line in input file:"
                                      f" '{line}'")
        for line in lines[1:]:
            if line.startswith("connection"):
                connection_line = line.split(":")
                connection = parse_connection(connection_line[1], hubs)
                connections.append(connection)
        return {"drone_nb": drone_nb, "hubs": hubs, "connections": connections}
