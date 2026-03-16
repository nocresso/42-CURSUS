#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")

    print("\nSECURE EXTRACTION:")
    with open("classified_data.txt", "r") as file:
        print("Vault connection established with failsafe protocols")
        print(file.read())

    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as file:
        content = "[CLASSIFIED] New security protocols archived"
        file.write(content)
        print(content)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
