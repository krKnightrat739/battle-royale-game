```python
import random
import time

# Game choices
choices = ["rock", "paper", "scissors", "fire", "water"]

# Rules
win_rules = {
    "rock": ["scissors", "fire"],
    "paper": ["rock", "water"],
    "scissors": ["paper", "fire"],
    "fire": ["paper", "scissors"],
    "water": ["rock", "fire"]
}


def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return None

    if choice2 in win_rules[choice1]:
        return 1
    else:
        return 2


def play_match(player1, player2):
    print(f"\n🔥 Match: {player1} vs {player2}")

    while True:
        print(f"\n{player1}'s turn")
        p1 = input("Choose (rock/paper/scissors/fire/water): ").lower()

        print("\n" * 50)

        print(f"{player2}'s turn")
        p2 = input("Choose (rock/paper/scissors/fire/water): ").lower()

        if p1 not in choices or p2 not in choices:
            print("❌ Invalid choice. Try again.")
            continue

        winner = determine_winner(p1, p2)

        print(f"\n{player1} chose: {p1}")
        print(f"{player2} chose: {p2}")

        if winner is None:
            print("🤝 It's a draw! Replay...")
            continue

        elif winner == 1:
            print(f"✅ {player1} wins this match!")
            return player1

        else:
            print(f"✅ {player2} wins this match!")
            return player2


def tournament(players):
    round_num = 1

    while len(players) > 1:
        print(f"\n==========================")
        print(f"🏆 ROUND {round_num}")
        print(f"==========================")

        next_round = []

        random.shuffle(players)

        # If odd number of players
        if len(players) % 2 == 1:
            lucky = players.pop()
            print(f"\n🎟️ {lucky} gets a free pass!")
            next_round.append(lucky)

        for i in range(0, len(players), 2):
            winner = play_match(players[i], players[i + 1])
            next_round.append(winner)

        players = next_round
        round_num += 1

    return players[0]


print("==============================")
print("🎮 BATTLE ROYALE TOURNAMENT 🎮")
print("==============================")

num_players = int(input("\nEnter number of players: "))

players = []

for i in range(num_players):
    name = input(f"Enter Player {i+1} Name: ")
    players.append(name)

print("\n⏳ Starting Tournament...")
time.sleep(2)

winner = tournament(players)

print("\n=================================")
print(f"🏆 FINAL WINNER IS: {winner}")
print("🎁 Prize: RayBan Meta Glass Gen 1")
print("=================================")
```
