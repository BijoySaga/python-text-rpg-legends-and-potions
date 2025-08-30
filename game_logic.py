
import random

def combat(player, villain):
    print(f"[BATTLE] {player.name} vs {villain.name}")
    print(f"Your HP: {player.health} | Villain HP: {villain.health}")
    dmg = random.randint(15, 30)
    villain.health -= dmg
    print(f"You attack for {dmg} damage!")
    if villain.health > 0:
        v_dmg = random.randint(10, 20)
        player.health -= v_dmg
        print(f"{villain.name} attacks for {v_dmg} damage!")

def use_potion(player):
    player.heal()
    if crit:
        dmg = int(dmg * 1.5)
        print("Critical hit!")
    villain.health -= dmg
    print(f"You attack {villain.name} for {dmg} damage!")
    if villain.health <= 0:
        print(f"You defeated {villain.name}!")
        return True
    player.take_damage(villain.attack_power)
    print(f"{villain.name} attacks for {villain.attack_power} damage!")
    return False

def use_potion_menu(player):
    if not player.inventory:
        print("[Inventory] No potions in inventory!")
        return
    print("[Inventory] Your Potions:")
    for idx, p in enumerate(player.inventory):
        print(f"  {idx+1}. {p}")
    while True:
        sel = input("Choose potion to use (number, or 0 to cancel): ")
        if sel == "0":
            print("Cancelled using potion.")
            return
        try:
            sel = int(sel) - 1
            potion = player.inventory.pop(sel)
            if potion.name == "Shield Potion":
                player.shield = True
                print("You used a Shield Potion! Next attack will be blocked.")
            else:
                player.use_potion(potion)
                print(f"You used {potion.name} and healed {potion.heal_amount} HP!")
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")

def shop(player):
    # ...existing code for shop from main.py...
    pass

def rest_action(player):
    # ...existing code for rest_action from main.py...
    pass

def get_ending(player, win):
    # ...existing code for get_ending from main.py...
    pass

def find_potion():
    # ...existing code for find_potion from main.py...
    pass
