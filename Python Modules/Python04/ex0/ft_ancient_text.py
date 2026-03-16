#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    print("Connection established...\n")
    content = file.read()
    print(content)
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
