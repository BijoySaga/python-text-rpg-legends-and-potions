import random

class Villain:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

# Simple villain roster: all villains, no special abilities
def get_villain_roster(player_name):
    return [
        Villain("Goblin", 80, random.randint(10, 20)),
        Villain("Orc", 120, random.randint(15, 30)),
        Villain("Dark Mage", 150, random.randint(20, 35)),
        Villain("Assassin", 130, random.randint(18, 32)),
        Villain("Troll", 180, random.randint(22, 36)),
        Villain("Necromancer", 160, random.randint(20, 35)),
        Villain("Fire Elemental", 170, random.randint(25, 40)),
        Villain("Dragon", 220, random.randint(30, 45)),
        Villain("Demon Lord", 250, random.randint(35, 50)),
        Villain(f"Final Boss: Dark {player_name}", 300, random.randint(40, 60)),
    ]
