from typing import Optional


class Drone:
    """
    Initialize a drone with its ID, starting hub, and optional
    restricted-zone transit state.
    """
    def __init__(self, id: int, current_hub: str,
                 next_hub: Optional[str] = None,
                 in_transit: bool = False, transit_remaining: int = 0,
                 transit_destination: Optional[str] = None):
        self.id = id
        self.current_hub = current_hub
        self.path_done = [current_hub]
        self.next_hub = next_hub
        self.in_transit = in_transit
        self.transit_remaining = transit_remaining
        self.transit_destination = transit_destination
