# I can't believe I'm finally writing something. That took a long time.


class Character:
    health = 1000

    def __init__(self, name, character_type, attacks, weakness):
        self.name = name
        self.character_type = character_type
        self.attacks = attacks
        self.weakness = weakness


# Link attacks: sword, bow, bomb, boomerang
# Majora attacks: physical, dark magic

Link = Character("Link", good, sword, magic)
Majora = Character("Majora", bad, magic, bomb)

print("Link approaches the clock tower's peak and is met by the skull kid.")
print("Unfortunately, he looks to be controlled by the Majora's mask.")
print("The fight seems to be unavoidable. Or is it?")

# Gather input: Fight, Distract, Transform, Talk
print("What will Link do?")
