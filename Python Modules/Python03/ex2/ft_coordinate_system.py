#!/usr/bin/env python3

import math


def distance_calculation(tupla1: tuple, tupla2: tuple) -> float:
    '''Method for distance calculation between two given positions.'''
    x1, y1, z1 = tupla1
    x2, y2, z2 = tupla2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def main() -> None:
    print("=== Game Coordinate System ===")
    input1 = (10, 20, 5)
    input2 = "3,4,0"
    input3 = "abc,def,ghi"
    zero_pos = (0, 0, 0)
    print(f"\nPosition created: {input1}")
    distance1 = distance_calculation(zero_pos, input1)
    print(f"Distance between {zero_pos} and {input1}: {distance1:.2f}")

    position_list2 = input2.split(",")
    try:
        position2 = (int(position_list2[0]), int(position_list2[1]),
                     int(position_list2[2]))
    except ValueError as error:
        print(f"Parsing invalid coordinates: {input2}")
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__},"
              f" Args: (\"{error}\")")
        return
    x, y, z = position2
    print(f"\nParsing coordinates: \"{input2}\"")
    print(f"Parsed position: {position2}")
    distance2 = distance_calculation(zero_pos, position2)
    print(f"Distance between {zero_pos} and {position2}: {distance2:.2f}")

    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

    position_list3 = input3.split(",")
    try:
        position3 = (int(position_list3[0]), int(position_list3[1]),
                     int(position_list3[2]))
    except ValueError as error:
        print(f"\nParsing invalid coordinates: \"{input3}\"")
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__},"
              f"Args: (\"{error}\")")
        return
    print(f"\nParsing coordinates: \"{input3}\"")
    print(f"Parsed position: {position3}")
    distance = distance_calculation(zero_pos, position3)
    print(f"Distance between {zero_pos} and {position3}: {distance}")


if __name__ == "__main__":
    main()
