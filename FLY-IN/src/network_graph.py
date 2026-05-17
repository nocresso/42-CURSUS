from src.input_validation import NetworkConfiguration, HubType, Hub
from typing import Dict, Any


class NetworkGraph:
    """
    Represents the drone network as an adjacency graph.
    Initialize the graph from a network configuration.
    """
    def __init__(self, config: NetworkConfiguration):
        self.config = config
        self._update_max_drones()
        self.graph = self._build_graph()
        self.hub_map = self._hub_map()

    def _build_graph(self) -> Dict[str, Any]:
        """
        Build an adjacent dict representation from configuration.
        """
        graph: Dict[str, Any] = {}
        for connection in self.config.connections:
            link = {"max_link_capacity": connection.max_link_capacity}
            graph.setdefault(connection.zone1.name, {})
            graph[connection.zone1.name][connection.zone2.name] = link
            graph.setdefault(connection.zone2.name, {})
            graph[connection.zone2.name][connection.zone1.name] = link
        return graph

    def _update_max_drones(self) -> None:
        """
        Set start/end hubs capability to allow all drones at initialization.
        """
        for hub in self.config.hubs:
            if hub.hub_type == HubType.start:
                hub.max_drones = self.config.drone_nb
            elif hub.hub_type == HubType.end:
                hub.max_drones = self.config.drone_nb

    def _hub_map(self) -> Dict[str, Hub]:
        """
        Return a dict mapping hub name to the Hub instance.
        """
        hub_map = {}
        for hub in self.config.hubs:
            hub_map[hub.name] = hub
        return hub_map
