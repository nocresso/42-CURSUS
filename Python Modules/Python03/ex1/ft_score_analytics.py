import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3"
              f" {sys.argv[0]} <score1> <score2> ...")
    else:
        scores = []
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                print("Invalid score provided. Score should be a number.")
                return
        total_players = len(scores)
        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        average = sum(scores) / total_players
        print(f"Total scores: {sum(scores)}")
        print(f"Average score: {average}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
