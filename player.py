
class Player:
    def __init__(self, name, char_class=None):
        self.name = name
        self.health = 100
        self.potions = 2
        self.small_potions = 1
        self.big_potions = 0
        self.potions_used = 0
        self.total_gold_earned = 30
        self.gold = 30
        self.xp = 0
        self.char_class = char_class

    def heal(self):
        if self.potions > 0:
            self.health = min(100, self.health + 30)
            self.potions -= 1
            print(f"You used a potion! HP: {self.health}, Potions left: {self.potions}")
        else:
            print("No potions left!")



                # --- Player setup and benefit logic ---
def create_new_player():
    import random
    name = input("Enter your hero's name: ")
    classes = ["Warrior", "Mage", "Rogue", "Paladin", "Hunter", "Berserker"]
    genders = ["Male", "Female"]
    char_class = random.choice(classes)
    gender = random.choice(genders)
    class_benefits = {
        "Warrior": ("+30 HP", lambda p: setattr(p, "max_health", p.max_health + 30)),
        "Mage": ("+10 Crit Chance", lambda p: setattr(p, "crit_chance", p.crit_chance + 0.1)),
        "Rogue": ("+50 Gold", lambda p: setattr(p, "gold", p.gold + 50)),
        "Paladin": ("+20 HP, +20 Gold", lambda p: (setattr(p, "max_health", p.max_health + 20), setattr(p, "gold", p.gold + 20))),
    # Removed advanced class logic for simplicity
        "Berserker": ("+15 HP, +0.05 Crit", lambda p: (setattr(p, "max_health", p.max_health + 15), setattr(p, "crit_chance", p.crit_chance + 0.05))),
    }
    gender_benefits = {
        "Male": ("+10 Max HP, +5 Gold", lambda p: (setattr(p, "max_health", p.max_health + 10), setattr(p, "gold", p.gold + 5))),
        "Female": ("+0.05 Crit Chance, +10 XP", lambda p: (setattr(p, "crit_chance", p.crit_chance + 0.05), setattr(p, "xp", p.xp + 10))),
    }
    gender_weaknesses = {
        "Male": ("-0.05 Crit Chance", lambda p: setattr(p, "crit_chance", max(0, p.crit_chance - 0.05))),
        "Female": ("-10 Max HP", lambda p: setattr(p, "max_health", max(1, p.max_health - 10))),
    }
    pet_benefits = {
        "heal": ("Heals you for 10 HP at start", lambda p: p.heal(10)),
        "gold": ("Finds 20 gold at start", lambda p: setattr(p, "gold", p.gold + 20)),
        "block": ("Gives you a shield at start", lambda p: setattr(p, "shield", True)),
        "crit": ("Increases crit chance by 0.05", lambda p: setattr(p, "crit_chance", p.crit_chance + 0.05)),
    # Removed advanced pet logic for simplicity
        "burn": ("Deals 10 damage to first villain", None),
        "revive": ("Will revive you once if you fall", None),
        "luck": ("Increases all random event chances", None),
    }
    pet_types = [
        ("Cat", ["heal", "gold", "block", "crit"]),
        ("Dog", ["heal", "block", "find_potion"]),
        ("Dragonling", ["burn", "heal", "gold"]),
        ("Fairy", ["heal", "revive", "luck"]),
        ("Wolf", ["crit", "block", "heal"]),
        ("Phoenix", ["revive", "heal", "burn"])
    ]
    pet_roll = random.random()
    pets = []
    if pet_roll < 0.7:
        pet_type, bonuses = random.choice(pet_types)
        bonus = random.choice(bonuses)
    # Removed pet logic for simplicity
    # Removed pet logic for simplicity
    elif pet_roll < 0.9:
        pets = []
    else:
        for _ in range(2):
            pet_type, bonuses = random.choice(pet_types)
            bonus = random.choice(bonuses)
            # Removed pet logic for simplicity
    player = Player(name=name if name else "Hero", char_class=char_class)
    player.gender = gender
    player.pet = pets[0] if pets else None
    class_benefit_text, class_benefit_fn = class_benefits[char_class]
    class_benefit_fn(player)
    gender_benefit_text, gender_benefit_fn = gender_benefits[gender]
    gender_benefit_fn(player)
    gender_weakness_text, gender_weakness_fn = gender_weaknesses[gender]
    gender_weakness_fn(player)
    pet_benefit_texts = []
    for p in pets:
        benefit = pet_benefits.get(p.bonus_type)
        if benefit and benefit[1]:
            benefit[1](player)
        if benefit:
            pet_benefit_texts.append(f"{p.name} ({p.bonus_type}): {benefit[0]}")
        else:
            pet_benefit_texts.append(f"{p.name} ({p.bonus_type})")
    print(f"You are a {gender} {char_class} (Class Benefit: {class_benefit_text}, Gender Benefit: {gender_benefit_text}, Gender Weakness: {gender_weakness_text}) with {len(pets)} pet(s):")
    for txt in pet_benefit_texts:
        print(f"  - {txt}")
    print("\n--- Press Enter to begin your adventure! ---")
    input()
    return player
