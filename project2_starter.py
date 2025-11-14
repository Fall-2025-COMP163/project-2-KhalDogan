import random

"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Khal Dogan]
Date: [11/12/2025]

AI Usage:
ChatGPT was used to help add comments and improve clarity of code structure.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for testing character classes.
    DO NOT MODIFY THIS CLASS.
    """

    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple turn-based battle between two characters."""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Display both characters' starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        
        # Character 1 attacks
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        # Character 2 attacks only if still alive
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        # Display final stats and winner
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# CHARACTER CLASSES TO IMPLEMENT
# ============================================================================

class Character:
    """
    Base class for all characters.
    Contains core stats and basic attack behavior.
    """

    def __init__(self, name, health, strength, magic, agility=10):
        """Initialize shared character attributes."""
        self.name = name
        self.health = max(0, int(health))  # Health cannot be negative
        self.strength = int(strength)
        self.magic = int(magic)
        self.agility = int(agility)
        
    def attack(self, target):
        """
        Basic physical attack.
        Damage is based on strength with small random variation.
        """
        damage = max(0, self.strength + random.randint(-5, 5))
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """
        Subtract damage from health.
        Ensures health never drops below 0.
        """
        damage = max(0, int(damage))
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self):
        """Prints core character stats."""
                stats = (
            f"Name: {self.name}\n"
            f"Health: {self.health}\n"
            f"Strength: {self.strength}\n"
            f"Magic: {self.magic}"
        )
            print(stats)
class Player(Character):
    """
    Base class for all player-controlled characters.
    Adds class name, level, and experience.
    """

    def __init__(self, name, character_class, health, strength, magic, agility=10):
        super().__init__(name, health, strength, magic, agility)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """
        Extends Character.display_stats by adding player-specific values.
        """
        super().display_stats()
        print(
            f"Class: {self.character_class}\n"
            f"Level: {self.level}\n"
            f"EXP: {self.experience}\n"
            f"Agility: {self.agility}"
        )

class Warrior(Player):
    """
    Warrior class: specializes in strong physical damage.
    Inherits from Player.
    """

    def __init__(self, name):
        # Warriors get high strength and health but low magic
        super().__init__(name, "Warrior", 120, 15, 5, 10)
        
    def attack(self, target):
        """
        Warrior attack overrides the basic attack.
        Adds bonus physical damage.
        """
        damage = max(0, self.strength + 5 + random.randint(0, 5))
        target.take_damage(damage)
        
    def power_strike(self, target):
        """
        A powerful special attack unique to Warriors.
        Deals heavy physical damage.
        """
        damage = max(0, self.strength + 10 + random.randint(2, 10))
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class: specializes in high magic damage.
    Inherits from Player.
    """

    def __init__(self, name):
        # Mages have high magic, low strength and health
        super().__init__(name, "Mage", 80, 8, 20, 12)
        
    def attack(self, target):
        """
        Override attack to use magic instead of strength.
        """
        damage = max(0, self.magic + random.randint(0, 3))
        target.take_damage(damage)
        
    def fireball(self, target):
        """
        Special spell that deals significant magic damage.
        """
        damage = max(0, self.magic + 15 + random.randint(5, 15))
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class: specializes in agility and critical hit damage.
    """

    def __init__(self, name):
        # Rogues have balanced stats with very high agility
        super().__init__(name, "Rogue", 90, 12, 10, 18)
        
    def attack(self, target):
        """
        Rogue attack includes chances for different critical hits.
        Higher agility increases damage significantly.
        """
        crit_roll = random.randint(1, 10)

        # Multiple levels of crits for fun gameplay variation
        if crit_roll >= 9:
            print("Extreme Critical Hit!")
            damage = (self.agility * 2) + random.randint(0, 3)
        elif crit_roll >= 6:
            print("Lucky Critical Hit!")
            damage = (self.agility * 2) + random.randint(1, 7)
        elif crit_roll >= 3:
            print("Critical Hit!")
            damage = (self.agility * 2) + random.randint(0, 3)
        else:
            print("No Critical Hit.")
            damage = self.agility + random.randint(0, 2)

        target.take_damage(damage)
        
    def sneak_attack(self, target):
        """
        Rogue's guaranteed critical strike ability.
        Always produces at least a basic critical hit.
        """
        crit_roll = random.randint(1, 11)

        if crit_roll >= 9:
            print("Extreme Critical Hit!")
            damage = ((self.agility * 2)*2 + random.randint(0, 5)) 
        elif crit_roll >= 6:
            print("Lucky Critical Hit!")
            damage = (self.agility*2) + random.randint(0, 5)
        else:
            print("Critical Hit!")
            damage = ((self.agility*2) + random.randint(0, 3))

        target.take_damage(damage)

class Weapon:
    """
    Weapon class: demonstrates composition (a character *has a* weapon).
    """

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = int(damage_bonus)
        
    def display_info(self):
        """Prints the weapon's name and damage bonus."""
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")

# ============================================================================
# MAIN TESTING PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create different character types
    warrior = Warrior("Optimus Prime")
    mage = Mage("Soundwave")
    rogue = Rogue("Bumblebee")
    
    # Display starting stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    rogue.display_stats()
    
    # Demonstrate polymorphism
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset health after each attack
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
