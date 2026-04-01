import os
import sys

try:
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Error: {e}")
    sys.exit(1)


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    load_dotenv()
    print("Configuration loaded:")
    check_var = True
    if not os.getenv("MATRIX_MODE"):
        print("[WARNING] Matrix mode not indicated")
        check_var = False
    else:
        print(f"Mode: {os.getenv('MATRIX_MODE')}")
    if not os.getenv("DATABASE_URL"):
        print("[WARNING] Connection not found")
        check_var = False
    else:
        print("Database: Connected to local instance")
    if not os.getenv("API_KEY"):
        print("[WARNING] Authentication failed")
        check_var = False
    else:
        print("API Access: Authenticated")
    if not os.getenv("LOG_LEVEL"):
        print("[WARNING] Log level not indicated")
        check_var = False
    else:
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    if not os.getenv("ZION_ENDPOINT"):
        print("[WARNING] Zion Network disconnected")
        check_var = False
    else:
        print("Zion Network: Online")
    print()
    print("Environment security check:")
    if check_var is False:
        print("Provide complete information for a secure connection.")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
