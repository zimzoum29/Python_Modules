from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8, 4, "drag_01")
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 3, 9, "wiz_01")

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"Registered: {dragon.name} (ID: {dragon.get_unique_id()})")
    print(f"Registered: {wizard.name} (ID: {wizard.get_unique_id()})")

    print("\nRunning Tournament Match...")
    match_res = platform.run_match(dragon, wizard)
    print(f"Match Result: {match_res}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(f"1. {entry}")

    print("\nPlatform Report:")
    print(platform.get_platform_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()
