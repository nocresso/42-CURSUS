#!/usr/bin/env python3


def file_handling(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to {filename}...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    file1 = "lost_archive.txt"
    file2 = "classified_vault.txt"
    file3 = "standard_archive.txt"

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    file_handling(file1)
    print()
    file_handling(file2)
    print()
    file_handling(file3)
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
