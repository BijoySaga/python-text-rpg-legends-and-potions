class Potion:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount
    def __str__(self):
        return f"{self.name} (+{self.heal_amount} HP)"
