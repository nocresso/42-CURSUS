from src.network_graph import NetworkGraph
from src.input_validation import HubType, ZoneType
from typing import Dict, List
from src.drone import Drone
from src.pathfinding import PathFinding


class SimulationManager:
    """
    Simulation manager class coordinating drone movement and occupancy.
    Manage the simulation state and advance discrete turns.
    Responsibilities include creating drones, tracking hub and link occupancy,
    computing movements each turn and printing turn output.
    """

    def __init__(self, network_graph: NetworkGraph):
        self.network_graph = network_graph
        self.hub_occupancy = self._initial_hub_state()
        self.link_occupancy = self._initial_link_state()
        self.drones = self._create_drones()

    def _initial_hub_state(self) -> Dict[str, int]:
        """
        Create initial occupancy mapping for all hubs.
        """
        occupancy = {}
        for hub in self.network_graph.config.hubs:
            if hub.hub_type == HubType.start:
                occupancy[hub.name] = self.network_graph.config.drone_nb
            else:
                occupancy[hub.name] = 0
        return occupancy

    def _initial_link_state(self) -> Dict[frozenset, int]:
        """
        Return a mapping of link keys to current in-transit counts.
        """
        link_occupancy = {}
        for connection in self.network_graph.config.connections:
            key = frozenset({connection.zone1.name, connection.zone2.name})
            link_occupancy[key] = 0
        return link_occupancy

    def _create_drones(self) -> List[Drone]:
        """
        Instantiate the configured drones and place them at the start hub.
        """
        drones_list = []
        for hub in self.network_graph.config.hubs:
            if hub.hub_type == HubType.start:
                current_hub = hub.name
        for i in range(1, self.network_graph.config.drone_nb + 1):
            drone_id = i
            new_drone = Drone(id=drone_id, current_hub=current_hub)
            drones_list.append(new_drone)
        return drones_list

    def run_turn(self) -> None:
        """
        Run turns until all drones have arrived at the end hub.
        """
        turn_nb = 0
        while self.drones:
            self.turn_mechanics()
            turn_nb += 1
        print(turn_nb)

    def turn_mechanics(self) -> None:
        """
        Advance the simulation by one turn.
        This method updates drones that finish transit, computes new
        paths, enforces hub and link capacities and prints simulation output.
        """
        output = []
        pathfinding = PathFinding(self.network_graph)
        reserved_occupancy = dict(self.hub_occupancy)
        was_in_transit = {drone.id for drone in self.drones
                          if drone.in_transit}
        for drone in self.drones:
            if drone.in_transit is True:
                drone.transit_remaining -= 1
                if (drone.transit_remaining == 0 and
                        drone.transit_destination is not None):
                    self.hub_occupancy[drone.transit_destination] += 1
                    drone.current_hub = drone.transit_destination
                    output.append(f"D{drone.id}-{drone.transit_destination}")
                    drone.in_transit = False
        end = next((h.name for h in self.network_graph.config.hubs
                    if h.hub_type == HubType.end), None)
        if end is None:
            raise ValueError("No end hub found in network configuration")
        paths = {}
        for drone in self.drones:
            if drone.in_transit is False and drone.id not in was_in_transit:
                path = pathfinding.find_path(drone.current_hub, end)
                if path is None:
                    drone.next_hub = None
                elif len(path) >= 2:
                    next_hub = path[1]
                    max_drone = self.network_graph.hub_map[next_hub].max_drones
                    if reserved_occupancy[next_hub] < max_drone:
                        drone.next_hub = next_hub
                        reserved_occupancy[drone.next_hub] += 1
                        reserved_occupancy[drone.current_hub] -= 1
                        paths[drone.id] = path
                    else:
                        alt_path = pathfinding.find_path(
                            drone.current_hub, end, excluded={next_hub})
                        if alt_path is not None and len(alt_path) >= 2:
                            alt_next = alt_path[1]
                            max_alt = (self.network_graph
                                       .hub_map[alt_next].max_drones)
                            if reserved_occupancy[alt_next] < max_alt:
                                drone.next_hub = alt_next
                                reserved_occupancy[alt_next] += 1
                                reserved_occupancy[drone.current_hub] -= 1
                                paths[drone.id] = alt_path
                            else:
                                drone.next_hub = None
                        else:
                            drone.next_hub = None
        destinies: Dict[str, List[Drone]] = {}
        for drone in self.drones:
            if drone.next_hub is not None:
                destinies.setdefault(drone.next_hub, []).append(drone)
        for h, drones in destinies.items():
            drones_leaving = sum(1 for d in self.drones
                                 if d.current_hub == h and d.next_hub
                                 is not None)
            capacity = (self.network_graph.hub_map[h].max_drones
                        - self.hub_occupancy[h] + drones_leaving)
            if len(drones) > capacity:
                for d in drones[capacity:]:
                    original_occupancy = self.hub_occupancy[h]
                    max_drones = (self.network_graph.hub_map[h]
                                  .max_drones)
                    self.hub_occupancy[h] = max_drones
                    alternative_path = pathfinding.find_path(d.current_hub,
                                                             end)
                    if (alternative_path is None or
                            len(alternative_path) > len(paths[d.id])):
                        d.next_hub = None
                    else:
                        next_hub = alternative_path[1]
                        d.next_hub = next_hub
                    self.hub_occupancy[h] = original_occupancy
        for drone in self.drones:
            if drone.next_hub is not None:
                link_key = frozenset({drone.current_hub, drone.next_hub})
                link_cap = (self.network_graph.graph[drone.current_hub]
                            [drone.next_hub]["max_link_capacity"])
                if self.link_occupancy[link_key] >= link_cap:
                    drone.next_hub = None
                    continue
                self.hub_occupancy[drone.current_hub] -= 1
                self.link_occupancy[link_key] += 1
                hub_zone = self.network_graph.hub_map[drone.next_hub].zone
                if hub_zone == ZoneType.restricted:
                    drone.in_transit = True
                    drone.transit_remaining = 1
                    drone.transit_destination = drone.next_hub
                    msg = (f"D{drone.id}-{drone.current_hub}-"
                           f"{drone.next_hub}")
                    output.append(msg)
                else:
                    self.hub_occupancy[drone.next_hub] += 1
                    output.append(f"D{drone.id}-{drone.next_hub}")
                    drone.current_hub = drone.next_hub
                drone.next_hub = None
        for key in self.link_occupancy:
            self.link_occupancy[key] = 0
        for drone in self.drones:
            if drone.in_transit and drone.transit_destination is not None:
                link_key = frozenset({drone.current_hub,
                                      drone.transit_destination})
                self.link_occupancy[link_key] += 1
        if output:
            print(" ".join(output))
        self.drones = [drone for drone in self.drones if
                       drone.current_hub != end]
