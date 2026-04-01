import sys
import os
import site


def main() -> None:
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still pllugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: Not detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:"
              "\npython -m venv matrix_env"
              "\nsource matrix_env/bin/activate  # On Unix"
              "\nmatrix_env"
              "\nScripts"
              "\nactivate    # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting"
              "\nthe global system.")
        print()
        print("Package installation path:")
        path = site.getsitepackages()
        print(f"{path[0]}")


if __name__ == "__main__":
    main()
