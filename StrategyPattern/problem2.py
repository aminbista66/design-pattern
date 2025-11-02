"""
Problem 2: Character Attack Behaviors (Game)

Scenario:
In a role-playing game, characters can have different attack types (e.g., Sword Attack, Bow Attack, Magic Attack).
Different characters may change their attack type during the game.

Goal:
Implement characters that can switch their attack behavior dynamically.

Hint:
Use a Character class with an AttackBehavior interface and concrete behaviors like SwordAttack, BowAttack, etc.

"""
from abc import ABC, abstractmethod

class AttackBehaviour(ABC):
    
    @abstractmethod
    def performAttack(self, attackParameters: dict={}):
        ...

class SwordAttack(AttackBehaviour):
    attackName: str = "Sword"

    def performAttack(self, attackParameters: dict = {}):
        print(f"Performed {self.attackName} Attack")

class MagicAttack(AttackBehaviour):
    attackName: str = "Magic"

    def performAttack(self, attackParameters: dict = {}):
        print(f"Performed {self.attackName} Attack")
    
class BowAttack(AttackBehaviour):
    attackName: str = "Bow"

    def performAttack(self, attackParameters: dict = {}):
        print(f"Performed {self.attackName} Attack")

class Character:
    attackBehaviour: AttackBehaviour

    def setBehaviour(self, attackBehaviour: AttackBehaviour):
        self.attackBehaviour = attackBehaviour
    
    def attack(self, attackParameters: dict = {}):
        if not self.attackBehaviour:
            raise ValueError("Attack Behaviour not set.")
        self.attackBehaviour.performAttack(attackParameters)

if __name__ == "__main__":
    attackBehaviour = SwordAttack()
    knight: Character = Character()
    knight.setBehaviour(attackBehaviour)
    knight.attack()