#!/usr/bin/env python3


def analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===")
    players = {
        "alice": {
            "score": 2300,
            "status": "active",
            "region": "north",
            "achievements": 5,
            "top_achievement": "first_kill"
        },
        "charlie": {
            "score": 2150,
            "status": "active",
            "region": "east",
            "achievements": 7,
            "top_achievement": "level_10"
        },
        "bob": {
            "score": 1800,
            "status": "active",
            "region": "central",
            "achievements": 3,
            "top_achievement": "boss_slayer"
        },
        "diana": {
            "score": 2200,
            "status": "inactive",
            "region": "central",
            "achievements": 2,
            "top_achievement": "super_jump"
        }
    }
    score_categories = {
        "high": 3,
        "medium": 2,
        "low": 1
    }

    print("\n=== List Comprehension Examples ===")
    highscorers = [name for name, data in players.items()
                   if data["score"] > 2000]
    active = [name for name, data in players.items()
              if data["status"] == "active"]
    scores = [2300, 5326, 5461, 1000, 4600, 4600, 3600, 3600, 4300, 4300]
    doubled = [n for n in set(scores) if scores.count(n) > 1]
    print(f"High scorers (>2000): {highscorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {name: data["score"] for name, data in players.items()}
    player_ach = {name: data["achievements"] for name, data in players.items()}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {player_ach}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {name for name, data in players.items()}
    unique_achievements = {data["top_achievement"]
                           for name, data in players.items()}
    active_regions = {data["region"] for name, data in players.items()}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n===Combined Analysis ===")
    print(f"Total players: {len(players)}")
    total_ach = sum(data["achievements"] for name, data in players.items())
    print(f"Total unique achievements: {total_ach}")
    average_score = ((sum(data["score"] for name, data in players.items()))
                     / len(players))
    print(f"Average score: {average_score}")
    max_score = max(player_scores.values())
    top_player = max(player_scores, key=player_scores.get)
    top_ach = player_ach[top_player]
    print(f"Top performer: {top_player} ({max_score}"
          f" points, {top_ach} achievements)")


if __name__ == "__main__":
    analytics_dashboard()
