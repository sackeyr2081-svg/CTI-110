# Name: Raphael Sackey
# Course: CTI-110 – Final Project
# Assignment: Text-based Car Race Game
# Date: 12/13/2025

import random
import time

# ------------- Global data -------------

player = {
    "name": "",
    "car": "",
    "speed": 0,      # base speed
    "grip": 0,       # how well the car handles
    "nitro": 1,      # nitro boosts left
    "position": 0,   # distance traveled
    "damage": 0      # 0–100, when 100 = crash
}

opponent = {
    "name": "Shadow Rider",
    "position": 0
}

TRACK_DISTANCE = 100  # finish line


# ------------- Helper functions -------------

def slow_print(text, delay=0.03):
    """Print text slowly for dramatic effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def pause(seconds=1.0):
    time.sleep(seconds)


# ------------- Game functions -------------

def intro():
    slow_print("🏁 Welcome to NIGHT STREET RACER 🏁\n")
    name = input("Enter your racer name: ")
    player["name"] = name if name.strip() else "Player 1"
    slow_print(f"\nWelcome, {player['name']}!")
    slow_print("Tonight you race against the mysterious Shadow Rider.\n")
    pause(1.5)


def choose_car():
    slow_print("Choose your car:\n")
    slow_print("1) Street Runner  (balanced)\n   speed: 7, grip: 5")
    slow_print("2) Drift King     (better handling)\n   speed: 6, grip: 7")
    slow_print("3) Turbo Beast    (very fast, low grip)\n   speed: 8, grip: 3\n")

    while True:
        choice = input("Pick a car (1, 2, or 3): ").strip()
        if choice == "1":
            player["car"] = "Street Runner"
            player["speed"] = 7
            player["grip"] = 5
            break
        elif choice == "2":
            player["car"] = "Drift King"
            player["speed"] = 6
            player["grip"] = 7
            break
        elif choice == "3":
            player["car"] = "Turbo Beast"
            player["speed"] = 8
            player["grip"] = 3
            break
        else:
            print("Invalid choice, try again.")

    slow_print(f"\nYou chose the {player['car']}!")
    show_stats()
    pause(1.5)


def show_stats():
    print("\n--- Your Car Stats ---")
    print(f"Car:        {player['car']}")
    print(f"Speed:      {player['speed']}")
    print(f"Grip:       {player['grip']}")
    print(f"Nitro left: {player['nitro']}")
    print(f"Damage:     {player['damage']}")
    print("----------------------\n")


def race_turn():
    """One turn of the race for the player."""
    print(f"Track: {player['position']} / {TRACK_DISTANCE}")
    print(f"Opponent: {opponent['position']} / {TRACK_DISTANCE}")
    print("\nYour move:")
    print("  (a)ccelerate   – more speed, more risk")
    print("  (s)afe drive   – steady and safe")
    print("  (n)itro boost  – huge burst, very risky\n")

    choice = input("Choose action (a/s/n): ").lower().strip()
    base_speed = player["speed"]

    # Damage slows you down a bit
    if player["damage"] >= 50:
        base_speed -= 1

    move = 0

    if choice == "s":
        slow_print("You keep it safe, taking clean racing lines.")
        move = base_speed + random.randint(3, 6)

    elif choice == "n":
        if player["nitro"] > 0:
            player["nitro"] -= 1
            slow_print("You slam the nitro button! 🚀")
            move = base_speed + random.randint(15, 25)
            # high risk of damage
            if random.random() < 0.5:
                damage = random.randint(15, 30)
                player["damage"] += damage
                slow_print(f"The car shakes! You take {damage} damage.")
        else:
            slow_print("No nitro left! You just accelerate instead.")
            move = base_speed + random.randint(5, 9)

    else:  # 'a' or anything else
        slow_print("You floor the pedal and push the car hard!")
        move = base_speed + random.randint(5, 9)
        # moderate risk based on grip
        risk = max(0.2, 0.6 - player["grip"] * 0.05)
        if random.random() < risk:
            damage = random.randint(5, 15)
            player["damage"] += damage
            slow_print(f"You slide a bit and scrape the guardrail! +{damage} damage.")

    # Apply movement, but not below zero
    move = max(0, move)
    player["position"] += move
    slow_print(f"You gain {move} meters.\n")


def opponent_turn():
    """Simple AI for the opponent's movement."""
    # Opponent speed is around 9–13 per turn with small randomness
    opponent_move = random.randint(8, 13)
    opponent["position"] += opponent_move
    slow_print(f"{opponent['name']} gains {opponent_move} meters.")


def check_crash():
    if player["damage"] >= 100:
        return True
    return False


def check_winner():
    player_finished = player["position"] >= TRACK_DISTANCE
    opponent_finished = opponent["position"] >= TRACK_DISTANCE

    if player_finished and not opponent_finished:
        return "player"
    elif opponent_finished and not player_finished:
        return "opponent"
    elif player_finished and opponent_finished:
        # whoever is farther wins
        if player["position"] > opponent["position"]:
            return "player"
        elif opponent["position"] > player["position"]:
            return "opponent"
        else:
            return "tie"
    else:
        return None


def player_wins():
    slow_print("\n🔥 You cross the finish line first! 🔥")
    slow_print(f"{player['name']} and the {player['car']} win the night race!")
    show_stats()


def opponent_wins():
    slow_print(f"\n{opponent['name']} crosses the finish line before you...")
    slow_print("You lose this race, but you can always challenge them again.")
    show_stats()


def tie_race():
    slow_print("\nIt’s a photo finish! You both cross at the same time.")
    slow_print("The crowd goes wild – it’s declared a tie!")


def crash_game_over():
    slow_print("\nYour car is too damaged to continue!")
    slow_print("Smoke rises from the hood as you roll to a stop...")
    slow_print("🏁 GAME OVER 🏁")


# ------------- Main loop -------------

def main():
    intro()
    choose_car()

    slow_print("The engines roar as the race begins...\n")
    pause(1.5)

    while True:
        race_turn()

        if check_crash():
            crash_game_over()
            break

        opponent_turn()

        winner = check_winner()
        if winner == "player":
            player_wins()
            break
        elif winner == "opponent":
            opponent_wins()
            break
        elif winner == "tie":
            tie_race()
            break

        pause(1.0)

    slow_print("\nThanks for playing NIGHT STREET RACER!")


if __name__ == "__main__":
    main()
