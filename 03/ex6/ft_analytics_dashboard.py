def categorize_score(score: int) -> str:
    if score >= 2000:
        return "high"
    if score >= 1500:
        return "medium"
    return "low"


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]

    achievements = {
        "alice": [
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
            "collector"],

        "bob": ["first_kill",
                "level_10",
                "boss_slayer"],

        "charlie": ["level_10",
                    "boss_slayer",
                    "treasure_hunter",
                    "perfectionist",
                    "speed_demon",
                    "collector",
                    "first_kill"],

        "diana": ["first_kill",
                  "level_10",
                  "treasure_hunter",
                  "boss_slayer"],
    }

    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "east",
    }

    print("=== List Comprehension Examples ===")
    high = [players[i] for i in range(len(players)) if scores[i] > 2000]
    scores_doubled = [s * 2 for s in scores]
    active_players = [p for p in players if len(achievements.get(p, [])) > 0]

    print(f"High scorers (>2000): {high}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    player_scores = {players[i]: scores[i] for i in range(len(players))}

    score_categories = {
        "high": len([s for s in scores if categorize_score(s) == "high"]),
        "medium": len([s for s in scores if categorize_score(s) == "medium"]),
        "low": len([s for s in scores if categorize_score(s) == "low"]),
    }

    achievement_counts = {p: len(achievements.get(p, [])) for p in players}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")

    print("=== Set Comprehension Examples ===")
    unique_players = {p for p in players}
    unique_achievements = {a for p in players for a in achievements.get(p, [])}
    active = {regions.get(p) for p in players if regions.get(p) is not None}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active}\n")

    print("=== Combined Analysis ===")
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / len(scores)

    top_score = max(scores)
    top_index = scores.index(top_score)
    top_player = players[top_index]
    top_achievements = len(achievements.get(top_player, []))

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({top_score} points, ", end="")
    print(f"{top_achievements} achievements)")


if __name__ == "__main__":
    main()
