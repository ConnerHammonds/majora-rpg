
## The OOP Pillars via an RPG Project
### 1. Classes and Objects (The Blueprints)
In an RPG, everything is a distinct "thing." OOP is all about creating blueprints (**Classes**) and instantiating actual instances of them (**Objects**).
 * You will create a Player class and an Enemy class.
 * The classes will hold **attributes** (like health, mana, and damage) and **methods/behaviors** (like attack(), take_damage(), or heal()).
### 2. Encapsulation (Protecting Data)
Encapsulation is the practice of keeping an object's data safe from outside interference and forcing interaction through specific methods.
 * Instead of allowing your game loop to directly alter a player's health (player.health = -50), you hide that data and use a method: player.take_damage(50).
 * Inside that method, you can write logic to check if the player has armor or if the damage drops them to 0 (triggering a game over), keeping the code clean and safe.
### 3. Inheritance (Reusing Code)
Instead of writing entirely separate code for a Goblin, a Dragon, and a Zombie, you use **Inheritance** to pass down common traits.
 * You create a base class called Character or Enemy that handles basic things like health and movement.
 * Then, you create specific subclasses like Dragon that *inherit* those basics but add unique features, like a breathe_fire() method.
### 4. Polymorphism (Many Forms)
Polymorphism allows different objects to respond to the exact same action in their own unique way.
 * Imagine your Player encounters a room with a list of generic Enemy objects.
 * When the turn starts, you can loop through them and call .perform_attack(). Because of polymorphism, the Goblin object will stab with a dagger, while the Wizard object will cast a spell—even though your main game loop just treats them all as a generic "Enemy."
## How to Build It (Phase by Phase)
To avoid getting overwhelmed, build it incrementally:
 * **Phase 1: The Duel.** Create a Player and a single Slime object. Make them take turns attacking each other in the console until one reaches 0 health.
 * **Phase 2: The Inventory.** Create an Item class. Give your player an inventory (a list of Item objects) like a Sword (adds damage) or a Potion (restores health).
 * **Phase 3: The Map.** Create a Room class. Each room can have a description, an item on the floor, or an enemy inside. Connect the rooms so the player can type go north or go south.
By the time you finish Phase 3, you won't just understand OOP theory—you'll intuitively grasp *why* it exists and how it keeps large codebases from turning into a tangled mess of spaghetti.
What programming language are you planning to use for this project?


