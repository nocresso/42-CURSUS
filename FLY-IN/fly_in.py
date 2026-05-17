from src.input_validation import (check_input_file, NetworkConfiguration,
                                  HubType)
from src.network_graph import NetworkGraph
from src.visual_representation import visual_representation
from pydantic import ValidationError
from src.pathfinding import PathFinding
import sys


def main() -> None:
    """
    Entry point for the FLY-IN simulation.
    Parse args, validate the map file and launch the visualization.
    """

    if len(sys.argv) > 2:
        sys.stderr.write("Error: too many arguments\nUsage:"
                         "python fly_in.py <map.txt>")
        return
    elif len(sys.argv) < 2:
        map = "test.txt"
    else:
        map = sys.argv[1]

    try:
        data = check_input_file(map)
        config = NetworkConfiguration(**data)
        net_graph = NetworkGraph(config)
        pathfinding = PathFinding(net_graph)
        start = next(h.name for h in net_graph.config.hubs
                     if h.hub_type == HubType.start)
        end = next(h.name for h in net_graph.config.hubs
                   if h.hub_type == HubType.end)
        if (pathfinding.find_path(start, end) is None):
            raise ValueError("No route available for drones")
        visual_representation(net_graph)
    except ValidationError as e:
        for error in e.errors():
            if error['loc']:
                sys.stderr.write(f"Error: {error['loc'][0]}: {error['msg']}\n")
            else:
                sys.stderr.write(f"Error: {error['msg']}\n")
        return
    except KeyboardInterrupt:
        sys.stderr.write("\nSimulation interrupted")
        return
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}")
