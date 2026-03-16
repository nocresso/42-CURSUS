import sys


def main() -> None:
    print("=== Command Quest ===")
    total = len(sys.argv)
    if total < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        args = total - 1
        print(f"Arguments received: {args}")
        for i in range(1, total):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()
