from src.network_graph import NetworkGraph
from src.input_validation import ZoneType
import heapq
from typing import Dict, List, Optional, Set, Tuple


class PathFinding:
    """
    Path finding class helper using a priority queue.
    """
    def __init__(self, graph: NetworkGraph):
        self.graph = graph

    def find_path(self, start: str, end: str,
                  excluded: Optional[Set[str]] = None) -> Optional[List[str]]:
        """
        Finds a least-cost path from start to
        end using a modified Dijkstra's algorithm.
        Returns a list of hub names path if a path exists, otherwise None.
        """
        priority_queue: List[Tuple[float, int, str]] = []
        visited = set()
        came_from: Dict[str, str] = {}
        costs: Dict[str, float] = {start: 0}
        heapq.heappush(priority_queue, (0, 1, start))
        while priority_queue:
            cost, priority, hub = heapq.heappop(priority_queue)
            if hub in visited:
                continue
            elif hub == end:
                return self._reconstruct_path(came_from, end)
            visited.add(hub)

            for neighbor in self.graph.graph[hub]:
                next_hub = next((h for h in self.graph.config.hubs
                                 if h.name == neighbor), None)
                if next_hub is None or next_hub.name in visited:
                    continue
                elif next_hub.zone == ZoneType.blocked:
                    continue
                elif excluded and next_hub.name in excluded:
                    continue

                else:
                    new_cost = cost + next_hub.cost
                    if new_cost < costs.get(next_hub.name, float('inf')):
                        costs[next_hub.name] = new_cost
                        came_from[next_hub.name] = hub
                        if next_hub.zone == ZoneType.priority:
                            priority = 0
                        else:
                            priority = 1
                        heapq.heappush(priority_queue,
                                       (new_cost, priority, next_hub.name))
        return None

    def _reconstruct_path(self, came_from: Dict[str, str],
                          end: str) -> List[str]:
        """
        Reconstruct the path from came_from mapping ending at end.
        Returns the path as a list of hub names from start to end.
        """
        path = [end]
        current = end
        while current in came_from:
            path.append(came_from[current])
            current = came_from[current]
        return path[::-1]
