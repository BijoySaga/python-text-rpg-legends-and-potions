import sys
from player import Player
from villains import Villain
from game_logic import *

def main():
    print("🧙‍♂️✨ Welcome, Brave Adventurer, to Legends & Potions! ✨🧪")
    print("🌌 In a mystical realm shrouded in shadows, legendary villains threaten the peace of every village and forest.")
    print("⚔️ Only a true hero—armed with courage, wit, and enchanted potions—can stand against the darkness.")
    print("😈 Face fearsome foes, discover magical treasures, and forge your legend.")
    print("Will you rise as the savior of this land, or fall to the forces of evil?")
    print("🌟 Your journey begins now. Good luck, hero! 🌟\n")
    hero_name = input("Enter your hero's name: ")
    player = Player(hero_name if hero_name else "Hero")
    # Simple villain setup
    villains = [
        type('Villain', (), {'name': 'Goblin', 'health': 50, 'attack': 15})(),
        type('Villain', (), {'name': 'Orc', 'health': 70, 'attack': 18})(),
        type('Villain', (), {'name': 'Troll', 'health': 80, 'attack': 20})(),
        type('Villain', (), {'name': 'Dragon', 'health': 100, 'attack': 25})(),
    ]
    player.small_potions = 1
    player.big_potions = 0
    player.potions_used = 0
    player.gold = 30
    player.total_gold_earned = 30
    player.xp = 0

    def shop(player):
        print("\n🛒 Welcome to the shop! Each potion costs 10 gold.")
        print(f"You have {player.gold} gold. 💰")
        while True:
            print("1. Buy small potion (10 gold)\n2. Buy big potion (20 gold)\n3. Exit shop")
            choice = input("Choose an option: ")
            if choice == "1":
                if player.gold >= 10:
                    player.gold -= 10
                    player.small_potions += 1
                    player.total_gold_earned -= 10
                    print("You bought a small potion! 🧪")
                else:
                    print("Not enough gold!")
            elif choice == "2":
                if player.gold >= 20:
                    player.gold -= 20
                    player.big_potions += 1
                    player.total_gold_earned -= 20
                    print("You bought a BIG potion! 🧪🧪")
                else:
                    print("Not enough gold!")
            elif choice == "3":
                print("Leaving the shop. 👋")
                break
            else:
                print("Invalid option. ❌")

    def rest(player):
        print("You rest and recover 20 HP. 💤❤️")
        player.health = min(100, player.health + 20)

    def search_for_potion(player):
        import random
        print("🔎 You search the area...")
        outcome = random.choices(
            ["small_potion", "big_potion", "gold", "trap", "nothing"],
            weights=[18, 7, 20, 20, 35],
            k=1
        )[0]
        if outcome == "small_potion":
            player.small_potions += 1
            print("🎉 You found a small potion! 🧪")
        elif outcome == "big_potion":
            player.big_potions += 1
            print("🎉 You found a BIG potion! 🧪🧪")
        elif outcome == "gold":
            found = random.randint(5, 20)
            player.gold += found
            print(f"💰 You found {found} gold!")
        elif outcome == "trap":
            dmg = random.randint(5, 15)
            player.health -= dmg
            print(f"💥 Oh no! A trap! You lose {dmg} HP.")
        else:
            print("😕 You searched everywhere but found nothing this time.")

    # Main game loop
    for villain in villains:
        if player.health <= 0:
            break
        print(f"\n⚡ A wild {villain.name} appears! 😱 (HP: {villain.health}, ATK: {villain.attack})")
        while player.health > 0 and villain.health > 0:
            print(f"❤️ Your HP: {player.health} | 🧪 Small: {player.small_potions} | 🧪🧪 Big: {player.big_potions} | 💰 Gold: {player.gold} | 😈 {villain.name} HP: {villain.health}")
            print("Choose an action: 1️⃣  Search for Potion 🧪 | 2️⃣  Use Potion 🧪 | 3️⃣  Rest 💤 | 4️⃣  Attack Villain ⚔️ | 5️⃣  Shop 🛒 | 6️⃣  Escape 🏃‍♂️")
            choice = input("Enter 1-6: ")

            if choice == "1":
                search_for_potion(player)
                if villain.health > 0 and player.health > 0:
                    print("🎲 You must roll a dice to see if you dodge the villain's attack!")
                    roll = random.randint(1, 6)
                    print(f"You rolled a {roll}.")
                    if roll % 2 == 0:
                        print("🌀 You dodged the attack!")
                    else:
                        v_dmg = random.randint(1, 8)
                        player.health -= v_dmg
                        print(f"😈 {villain.name} attacks for {v_dmg} damage!")

            elif choice == "2":
                if player.small_potions == 0 and player.big_potions == 0:
                    print("No potions left! ❌")
                else:
                    print(f"🧪 You have {player.small_potions} small potion(s) and {player.big_potions} big potion(s).")
                    use = input("Use (s)mall, (b)ig potion, or (c)ancel? ").lower()
                    if use == "s":
                        if player.small_potions > 0:
                            player.health = min(100, player.health + 15)
                            player.small_potions -= 1
                            player.potions_used += 1
                            print(f"🧪 You used a small potion! HP: {player.health}, Small potions left: {player.small_potions}")
                        else:
                            print("You don't have any small potions! ❌")
                    elif use == "b":
                        if player.big_potions > 0:
                            player.health = min(100, player.health + 30)
                            player.big_potions -= 1
                            player.potions_used += 1
                            print(f"🧪🧪 You used a BIG potion! HP: {player.health}, Big potions left: {player.big_potions}")
                        else:
                            print("You don't have any big potions! ❌")
                    elif use == "c":
                        print("Cancelled potion use. 🚫")
                    else:
                        print("Invalid potion choice! ❓")
                # Villain attacks after potion use
                if choice == "2" and use in ["s", "b"] and villain.health > 0 and player.health > 0:
                    print("⚠️ After you heal, the villain seizes the moment and attacks!")
                    v_dmg = random.randint(10, villain.attack)
                    player.health -= v_dmg
                    print(f"😈 {villain.name} attacks for {v_dmg} damage!")

            elif choice == "3":
                rest(player)
                if villain.health > 0 and player.health > 0:
                    print("⚠️ After you rest, the villain seizes the moment and attacks!")
                    v_dmg = random.randint(10, villain.attack)
                    player.health -= v_dmg
                    print(f"😈 {villain.name} attacks for {v_dmg} damage!")

            elif choice == "4":
                dmg = random.randint(15, 30)
                if random.randint(1, 5) == 1:
                    dmg *= 2
                    print("💥 Critical hit!")
                villain.health -= dmg
                print(f"⚔️ You attack for {dmg} damage!")
                if villain.health > 0 and player.health > 0:
                    v_dmg = random.randint(10, villain.attack)
                    player.health -= v_dmg
                    print(f"😈 {villain.name} attacks for {v_dmg} damage!")

            elif choice == "5":
                shop(player)

            elif choice == "6":
                print("🏃‍♂️ You try to escape...")
                if random.randint(1, 2) == 1:
                    print("✅ You escaped successfully!")
                    break
                else:
                    print("❌ Escape failed! The villain attacks you.")
                    v_dmg = random.randint(10, villain.attack)
                    player.health -= v_dmg
                    print(f"😈 {villain.name} attacks for {v_dmg} damage!")

            else:
                print("Invalid choice. ❓")

        if player.health <= 0:
            print(f"\n💀 {player.name} was defeated by {villain.name}. Game Over!")
            break
        else:
            print(f"🏆 {player.name} defeated {villain.name}! You gain 10 gold.")
            player.gold += 10
            player.total_gold_earned += 10

    if player.health > 0:
        print(f"\n🎉 {player.name} defeated all villains! You win! 🏅")
    print(f"\nGame Over! Stats:")
    print(f"💰 Total gold earned: {player.total_gold_earned}")
    print(f"🧪 Potions used: {player.potions_used}")

if __name__ == "__main__":
    main()
