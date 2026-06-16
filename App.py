class Character:
    def __init__(self, name, magic, attacks, health, weakness, stamina, mana):
        self.name = name
        self.magic = magic
        self.attacks = attacks
        self.health = health
        self.weakness = weakness
        self.stamina = stamina
        self.mana = mana


class Action:
    def __init__(self, name, damage, type, accuracy):
        self.name = name
        self.damage = damage  # negative damage for healing actions
        self.type = type
        self.accuracy = accuracy


class Physical(Action):
    def __init(self, staminaCost):
        self.staminaCost = staminaCost


class Magic(Action):
    def __init__(self, manaCost):
        self.manaCost = manaCost


class Item(Action):
    def __init(self, itemCount):
        self.itemCount = itemCount


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

# Ganon Actions
punch = Physical(name="Punch", damage=25, type="physical", accuracy=1, staminaCost=30)

heavyPunch = Action(
    name="Heavy Punch", damage=150, type="physical", accuracy=0.35, staminaCost=60
)

warlockPunch = Action(
    name="Warlock Punch", damage=400, type="magic", accuracy=0.5, manaCost=80
)

# Shared Actions
# Dodge and block can be used as a means of trying to build up stamina/mana

# block reduces damage by half
block = Action("Defend", 0, "physical", 1)
# dodge has a .5 percent chance of dodging all damage
dodge = Action("Dodge", 0, "physical", 1)


class Battle:
    def __init__(self, asdf):
        # placeholder
        self.asdf = asdf


class Status:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


# Link attacks: sword, bow, bomb, tranform
# Ganon attacks: physical, dark magic

Link = Character(
    name="Link", attacks="attacks", health=1000, weakness="magic", stamina=100, mana=100
)

Ganon = Character(
    name="Ganon", attacks="attacks", health=3000, weakness="bow", stamina=100, mana=100
)


# Gather input: Attack, Defend, Talk,

# MAIN FUNCTION

# While link.health and ganon.health > 0
#   main game/fight logic
#
# if link.health <= 0
#   "Game Over"
# else:
#   "Ganon has been defeated"
