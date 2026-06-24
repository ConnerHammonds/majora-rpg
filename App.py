class Character:
    def __init__(self, name, actions, health, weakness, stamina, mana):
        self.name = name
        self.actions = Action()
        self.health = health
        self.weakness = weakness
        self.stamina = stamina
        self.mana = mana


class Action:
    def __init__(self, name, damage, type, accuracy, attacks, defend, items):
        self.name = name
        self.damage = damage  # negative damage for healing actions
        self.type = type
        self.accuracy = accuracy
        self.attacks = []
        self.defend = []
        self.items = []

    def add_attack(self, attack):
        self.attacks.append(attack)

    def add_defense(self, defense):
        self.defend.append(defense)

    def add_item(self, item):
        self.items.append(item)


class Physical(Action):
    def __init(self, staminaCost):
        self.staminaCost = staminaCost


class Magic(Action):
    def __init__(self, manaCost):
        self.manaCost = manaCost


class Item(Action):
    def __init(self, itemCount):
        self.itemCount = itemCount


Link = Character(
    name="Link", attacks="attacks", health=1000, weakness="magic", stamina=100, mana=100
)

# Shared Actions
# Dodge and block can be used as a means of trying to build up stamina/mana
# block reduces damage by half
block = Action("Defend", 0, "physical", 1)
# dodge has a .5 percent chance of dodging all damage
dodge = Action("Dodge", 0, "physical", 1)

# Link Actions
slash = Physical(name="Slash", damage=50, type="physical", accuracy=0.9, staminaCost=10)
jumpSlash = Physical(
    name="Jump Slash", damage=100, type="physical", accuracy=0.5, staminaCost=25
)
bow = Item(name="Bow", damage=50, type="item", accuracy=0.8, itemCount=5)
bomb = Item(name="Bomb", damage=100, type="item", accuracy=1, itemCount=1)

# Reduces enemy accuracy
dekuNut = Item(name="Deku Nut", damage=0, type="item", accuracy=0.75, itemCount=5)
potion = Item(name="Potion", damage=-250, type="item", accuracy=100, itemCount=1)
dinsFire = Magic(name="Din's Fire", damage=250, type="magic", accuracy=1, manaCost=250)

Link.add_attack(slash)
Link.add_attack(jumpSlash)
Link.add_attack(bow)
Link.add_attack(bomb)
Link.add_attack(dekuNut)
Link.add_attack(dinsFire)
Link.add_defense(block)
Link.add_defense(dodge)
Link.add_item(potion)

Ganon = Character(
    name="Ganon", attacks="attacks", health=3000, weakness="bow", stamina=100, mana=100
)

# Ganon Actions
punch = Physical(name="Punch", damage=25, type="physical", accuracy=1, staminaCost=30)
heavyPunch = Action(
    name="Heavy Punch", damage=150, type="physical", accuracy=0.35, staminaCost=60
)
warlockPunch = Action(
    name="Warlock Punch", damage=400, type="magic", accuracy=0.5, manaCost=80
)

Ganon.add_attack(punch)
Ganon.add_attack(heavyPunch)
Ganon.add_attack(warlockPunch)
Ganon.add_defense(block)
Ganon.add_defense(dodge)
Ganon.add_item(potion)


class Battle:
    def __init__(self, asdf):
        # placeholder
        self.asdf = asdf


# Not sure if Status needs to be it's own class
class Status:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


# Link attacks: sword, bow, bomb, tranform
# Ganon attacks: physical, dark magic

# Gather input: Attack, Defend, Talk,

# MAIN FUNCTION

# While link.health and ganon.health > 0
#   main game/fight logic
#
# if link.health <= 0
#   "Game Over"
# else:
#   "Ganon has been defeated"


def main():
    pass
