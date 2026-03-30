from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    from ex0.CardEnums import CardRarity
    card1 = TournamentCard("Fire Dragon", 5, CardRarity.LEGENDARY, 7)
    card2 = TournamentCard("Ice Wizard", 4, CardRarity.RARE, 5)

    id1 = platform.register_card(card1)
    id2 = platform.register_card(card2)

    print(f"Fire Dragon (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card1.calculate_rating()}")
    print(f"- Record: {card1.wins}-{card1.losses}\n")

    print(f"Ice Wizard (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card2.calculate_rating()}")
    print(f"- Record: {card2.wins}-{card2.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match(id1, id2)

    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    for i, (card_id, stats) in enumerate(leaderboard, start=1):
        print(
            f"{i}. {stats['name']} - Rating: "
            f"{stats['rating']} ({stats['record']})")

    report = platform.generate_tournament_report()

    print("\nPlatform Report:")
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
