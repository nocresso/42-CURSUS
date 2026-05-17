import pygame
from src.network_graph import NetworkGraph
from src.simulation_manager import SimulationManager
from src.input_validation import Hub, ZoneType
from typing import Dict, Any, cast, Set, List
from src.drone import Drone
import random


def hub_to_pixel(hub: Hub, scale: Dict[str, int]) -> tuple[int, int]:
    """
    Convert hub logical coordinates to screen pixel coordinates.
    """
    x = ((hub.coordinates[0] - scale["min_x"]) * scale["coord_factor_x"]
         + scale["margin"])
    y = ((hub.coordinates[1] - scale["min_y"]) * scale["coord_factor_y"]
         + scale["margin"])
    return (x, y)


def draw_network(network_graph: NetworkGraph, screen: pygame.Surface,
                 scale: Dict[str, int], icon_font: pygame.font.Font) -> None:
    """
    Draw connections and hubs onto the provided screen surface.
    """
    hub_dict = network_graph.hub_map
    color = (random.randint(0, 255), random.randint(0, 255),
             random.randint(0, 255))
    for connection in network_graph.config.connections:
        hub1 = hub_to_pixel(connection.zone1, scale)
        hub2 = hub_to_pixel(connection.zone2, scale)
        pygame.draw.line(screen, (255, 255, 255), hub1, hub2, 2)
    for _, hub in hub_dict.items():
        x, y = hub_to_pixel(hub, scale)
        if hub.color is None:
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 20)
        else:
            if hub.color == "rainbow":
                color = (random.randint(0, 255), random.randint(0, 255),
                         random.randint(0, 255))
                hub_color = pygame.Color(color)
            else:
                hub_color = pygame.Color(hub.color)
            pygame.draw.circle(screen, hub_color, (x, y), 20)
        if hub.zone == ZoneType.priority:
            star = icon_font.render("★", True, (255, 215, 0))
            screen.blit(star, (x, y - 10))
        elif hub.zone == ZoneType.blocked:
            cross = icon_font.render("✖", True, (255, 0, 0))
            screen.blit(cross, (x + 1, y - 5))
        elif hub.zone == ZoneType.restricted:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 20, 2)


def draw_drones(screen: pygame.Surface, image: pygame.Surface,
                drone_position: Dict[int, Dict[str, Any]], t: float) -> None:
    """
    Render drone images interpolated between origin and destination.
    ``t`` is an interpolation parameter in [0, 1] indicating progress
    along the current movement for smooth animation.
    """
    for drone_id, pos in drone_position.items():
        origin_px = pos["orig"]
        dest_px = pos["dest"]
        x = origin_px[0] + (dest_px[0] - origin_px[0]) * t
        y = origin_px[1] + (dest_px[1] - origin_px[1]) * t
        screen.blit(image, (x - image.get_width() // 2,
                            y - image.get_height() // 2))


def visual_representation(network_graph: NetworkGraph) -> None:
    """
    Launch the interactive Pygame visualization for the simulation.
    This function initializes Pygame, creates a SimulationManager
    and runs the main loop until the simulation completes or the user
    closes the window.
    """
    pygame.init()
    screen_width = 2000
    screen_height = 1600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    simulation_finished = False
    turn_nb = 0
    manager = SimulationManager(network_graph)
    drone_img = pygame.image.load("assets/drone.png").convert_alpha()
    drone_img = pygame.transform.scale(drone_img, (80, 80))
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background,
                                        (screen_width, screen_height))
    font = pygame.font.Font(None, 80)
    icon_font = pygame.font.Font("/usr/share/fonts/truetype/noto/"
                                 "NotoSansSymbols2-Regular.ttf", 40)
    scale = {}
    all_x = [hub.coordinates[0] for hub in network_graph.hub_map.values()]
    all_y = [hub.coordinates[1] for hub in network_graph.hub_map.values()]
    min_x = min(all_x)
    max_x = max(all_x)
    min_y = min(all_y)
    max_y = max(all_y)
    margin = 120
    coord_factor_x = (screen.get_width() - 2 * margin) // max(max_x - min_x, 1)
    coord_factor_y = ((screen.get_height() - 2 * margin)
                      // max(max_y - min_y, 1))
    scale = {"min_x": min_x,
             "max_x": max_x,
             "min_y": min_y,
             "max_y": max_y,
             "margin": margin,
             "coord_factor_x": coord_factor_x,
             "coord_factor_y": coord_factor_y
             }
    end_name = next(h.name for h in network_graph.config.hubs
                    if h.hub_type.name == "end")
    end_pos = hub_to_pixel(network_graph.hub_map[end_name], scale)
    t = 0.0
    drone_position = {
        drone.id: {
            "orig": hub_to_pixel(network_graph.hub_map[drone.current_hub],
                                 scale),
            "dest": hub_to_pixel(network_graph.hub_map[drone.current_hub],
                                 scale)
        }
        for drone in manager.drones
    }
    arrived_drones: Set[int] = set()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise KeyboardInterrupt
                running = False

        screen.blit(background, (0, 0))
        t += 0.02
        if simulation_finished:
            t = min(t, 1.0)
        if t >= 1.0 and not simulation_finished:
            t = 0.0
            for drone_id in arrived_drones:
                drone_position[drone_id]["orig"] = (
                    drone_position[drone_id]["dest"])
            pre_turn: List[Dict[str, Any]] = [
                {
                    "drone": drone,
                    "hub": drone.current_hub,
                    "was_in_transit": drone.in_transit,
                    "transit_dest": drone.transit_destination,
                }
                for drone in manager.drones
            ]
            for info in pre_turn:
                drone = cast(Drone, info["drone"])
                if info["was_in_transit"]:
                    drone_position[drone.id]["orig"] = hub_to_pixel(
                        network_graph.hub_map[cast(str, info["transit_dest"])],
                        scale)
                else:
                    drone_position[drone.id]["orig"] = hub_to_pixel(
                        network_graph.hub_map[cast(str, info["hub"])], scale)
            manager.turn_mechanics()
            for info in pre_turn:
                drone = cast(Drone, info["drone"])
                if drone not in manager.drones:
                    if not info["was_in_transit"]:
                        drone_position[drone.id]["orig"] = hub_to_pixel(
                            network_graph.hub_map[info["hub"]], scale)
                    drone_position[drone.id]["dest"] = end_pos
                    arrived_drones.add(drone.id)
                elif not info["was_in_transit"] and drone.in_transit:
                    drone_position[drone.id]["dest"] = hub_to_pixel(
                        network_graph.hub_map[
                            cast(str, drone.transit_destination)], scale)
                else:
                    drone_position[drone.id]["dest"] = hub_to_pixel(
                        network_graph.hub_map[drone.current_hub], scale)
            turn_nb += 1
            if not manager.drones:
                simulation_finished = True
        text = font.render(f"Turn: {turn_nb}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        draw_network(network_graph, screen, scale, icon_font)
        draw_drones(screen, drone_img, drone_position, min(t, 1.0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
