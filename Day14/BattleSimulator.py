class Player:
    def __init__(self, name, health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self,  monster, damage=1,):
        monster.health -= damage
        self.damage = damage
        self.energy -= self.damage
        if monster.is_attacked:
            self.health -= monster.damage          
            print(f"{self.name} attacking the {monster.name} {self.damage}")
            return f"{monster.name} is attacked {self.name} -10"             

    def info(self):
        return f"{self.name} \n (health : {self.health}) \n (energy : {self.energy})"


class Monster:
    def __init__(self, name, health=500, damage=10):
        self.name = name
        self.health = health
        self.current_health = self.health
        self.damage = damage

    def is_attacked(self):
        return self.health < self.current_health

    def info(self):
        return f"{self.name}(monster) \n(health  : {self.health})"


monster = Monster("Lizard", 500)
player1 = Player("Gangga")
player2 = Player("Rudy")

print(player1.info())
print(player2.info())
print(monster.info())
print("\n")


print(f"{player1.attack(monster, 50)}")
print(f"{player2.attack(monster, 50)}")

monster.is_attacked()
print("\n")

print("Current : ")
print("Player : ")
print(player1.info())
print(player2.info())
print("Monster :")
print(monster.info())
