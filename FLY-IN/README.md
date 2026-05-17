*This project has been created as part of the 42 curriculum by nocrespo.*
 
## Description
 
**Fly-in** is a drone routing simulation system. The goal is to navigate a fleet of drones from a single start zone to a target end zone through a network of interconnected hubs, in the fewest possible simulation turns.
 
The network is represented as a weighted graph where each hub (zone) has properties such as zone type, capacity, and movement cost. The system must respect strict constraints on zone occupancy and connection capacity while optimizing drone throughput.
 
Key features:
- Input file parser with full validation
- Pathfinding engine based on a modified Dijkstra algorithm
- Turn-based simulation engine with conflict resolution
- Graphical visualization using Pygame

 
## Instructions
 
### Requirements
 
- Python 3.10 or later
- pip or any compatible package manager
 
### Installation
 
Clone the repository and install dependencies:
 
```bash
make install
```
 
Or manually:
 
```bash
pip install -r requirements.txt
```
 
Dependencies include: `pygame`, `pydantic`, `mypy`, `flake8`.
 
### Running the project
 
```bash
make run
```
 
Runs the simulation with the default map (`test.txt`).
 
To use a different map, pass it as an argument:
 
```bash
make run MAP=maps/medium/01_dead_end_trap.txt
```
 
Or run the script directly:
 
```bash
python3 fly_in.py maps/medium/01_dead_end_trap.txt
```
 
### Debug mode
 
```bash
make debug
```
 
Runs the project using Python's built-in debugger (`pdb`) with the default map.
To debug a specific map:
 
```bash
make debug MAP=maps/medium/01_dead_end_trap.txt
```
 
### Lint
 
```bash
make lint
```
 
Runs `flake8` and `mypy` with the required flags.
 
### Clean
 
```bash
make clean
```
 
Removes `__pycache__`, `.mypy_cache`, and other temporary files.
 
### Map file format
 
Map files are plain `.txt` files structured as follows:
 
```
nb_drones: 3
 
start_hub: A 0 0
hub: B 1 0 [zone=restricted max_drones=2]
hub: C 1 1 [zone=priority]
end_hub: D 2 0
 
connection: A-B [max_link_capacity=2]
connection: B-D
connection: A-C
connection: C-D
```
 
Lines starting with `#` and blank lines are ignored.
 

## Algorithm
 
### Pathfinding — Modified Dijkstra
 
The pathfinding is implemented in `pathfinding.py` using a **priority queue (min-heap)** with two levels of priority:
 
- **Cost** (primary): the accumulated movement cost to reach each hub. Normal and priority zones cost 1; restricted zones cost 2; blocked zones are skipped entirely.
- **Zone priority** (secondary): priority zones are pushed to the front of the queue (priority value `0`) over normal zones (priority value `1`), so the algorithm naturally favors faster routes through priority hubs.
 
The path is reconstructed backwards using a `came_from` dictionary, then reversed to return it in start-to-end order.
 
### Simulation engine — `SimulationManager`
 
The simulation runs turn by turn in `turn_mechanics()`. Each turn follows this order:
 
1. **Transit resolution**: drones that were mid-flight toward a restricted zone (which takes 2 turns) have their remaining transit decremented. If it reaches 0, they land at their destination.
 
2. **Path planning**: for each idle drone, `find_path` is called to get the optimal route. The next hub is selected from `path[1]`. A `reserved_occupancy` dict tracks planned moves within the same turn to avoid overcrowding before the turn is committed.
 
3. **Conflict resolution**: if multiple drones target the same hub and it would exceed capacity, excess drones are re-routed. If no valid alternative exists or the alternative is longer, the drone waits.
 
4. **Link capacity enforcement**: before committing a move, the link's `max_link_capacity` is checked. If the link is saturated, the drone stays put.
 
5. **Movement commit**: drones move. If the destination is a restricted zone, the drone enters transit (`in_transit = True`, `transit_remaining = 1`). Otherwise it moves immediately.
 
6. **Link occupancy reset**: link counters are reset at the end of each turn, then recomputed for drones still in transit.
 
7. **Drone removal**: drones that have reached the end hub are removed from the active list.
 
### Design decisions
 
- **Pydantic models** are used throughout `input_validation.py` for parsing, type enforcement, and validation of the map configuration. This catches malformed input early with clear error messages.
- **`frozenset` keys** are used for link occupancy tracking, making link lookups bidirectional without duplicating entries.
- **`hub_map`** in `NetworkGraph` provides O(1) hub lookup by name, avoiding repeated linear searches through the hub list during simulation.
- **`reserved_occupancy`** is a shallow copy of hub occupancy used within a single turn to plan moves without committing them, preventing race conditions between drones choosing the same destination.
 
---
 
## Visual Representation
 
The graphical interface is built with **Pygame** and launched automatically when running the project.
 
### What is displayed
 
- **White lines** between hubs represent connections in the network.
- **Colored circles** represent hubs. If a hub has a `color` property defined in the map file, it uses that color; otherwise it defaults to white. The special value `rainbow` generates a random color each frame.
- **★ (yellow star)** icon marks priority zones.
- **✖ (red cross)** icon marks blocked zones.
- **Drone sprites** (40×40px image loaded from `assets/drone.png`) move smoothly between hubs using linear interpolation based on a `t` value that goes from 0.0 to 1.0 each turn.
- **Turn counter** is displayed in the top-left corner.
 
### How it enhances the user experience
 
The animation makes it easy to visualize bottlenecks: you can see drones queuing at high-traffic hubs, being rerouted, or stalling when links are saturated. This gives immediate intuition about how the pathfinding algorithm behaves on different map topologies, which would be much harder to infer from terminal output alone.
 
Drones that reach the end zone remain visible at that position for the rest of the simulation, rather than disappearing abruptly, making it clear how many have arrived.
 
---
 
## Resources
 
### Pathfinding & graph algorithms

- [Python `heapq` module documentation](https://docs.python.org/3/library/heapq.html)
- [Pygame documentation](https://www.pygame.org/docs/)
- AI was used to understand algorithm concepts, debug errors, docstrings and learn unfamiliar libraries such as pygame and heapq.
