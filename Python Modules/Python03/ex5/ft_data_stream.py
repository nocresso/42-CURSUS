#!/usr/bin/env python3

import time
from typing import Generator


def fibonacci(n: int) -> Generator[int, None, None]:
    ''' Fibonacci sequence generator'''
    first = 0
    second = 1
    count = 2
    yield first
    yield second
    while count < n:
        third = first + second
        yield third
        first, second = second, third
        count += 1


def prime_numbers(n: int) -> Generator[int, None, None]:
    '''Prime numbers generator'''
    num = 2
    count = 0
    while count < n:
        i = 2
        while i <= num:
            if i == num:
                yield num
                count += 1
            elif num % i == 0:
                break
            i += 1
        num += 1


def print_numbers() -> None:
    '''print numbers originated by generators'''
    fib_num = 10
    fib = fibonacci(fib_num)
    print(f"Fibonacci sequence (first {fib_num}): ", end="")
    for i in range(fib_num):
        num = next(fib)
        if i < (fib_num - 1):
            print(num, end=", ")
        else:
            print(num)

    prime_num = 5
    prime = prime_numbers(prime_num)
    print(f"Prime numbers (first {prime_num}): ", end="")
    for j in range(prime_num):
        num = next(prime)
        if j < (prime_num - 1):
            print(num, end=", ")
        else:
            print(num)


def game_events(n: int) -> Generator[tuple[str, str, int], None, None]:
    '''Game events generator'''
    players = ["Alice", "Bob", "Charlie", "Paul"]
    actions = ["killed a monster", "found treasure",
               "leveled up", "eat an apple"]
    levels = [5, 12, 8, 10, 4, 34, 10, 6, 23, 6, 25, 16]
    for i in range(n):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = levels[i % len(levels)]
        yield player, action, level


def process_events(n: int) -> None:
    start = time.time()
    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {n} game events...\n")
    high_level = 0
    treasure = 0
    level_up = 0
    for i, (player, action, level) in enumerate(game_events(n)):
        print(f"Event {i+1}: Player {player} (level {level}) {action}")
        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1
    duration = time.time() - start
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {n}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {duration:.4f} seconds")

    print("\n=== Generator Demonstration ===")
    print_numbers()


if __name__ == "__main__":
    process_events(10)
