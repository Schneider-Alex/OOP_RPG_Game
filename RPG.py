class Weapon:
    def __init__(self, name, weight:int, power:int):
        self.weight=weight
        self.power=power
        self.name=name

class Player:
    def __init__(self, name, health=100,):
        self.health = health
        self.name = name
        self.weapons = [Weapon("Sword",45,35),]
        self.alive = True
    def attack(self, attackee):
        attackPower=0
        for x in range (len(self.weapons)):
            attackPower+=self.weapons[x].power
        attackee.health -= attackPower
        if attackee.health <=0:
            attackee.alive = False
            print(f"The light has left {attackee.name}'s eyes...")
            attackee.loot(self,attackee)
    def loot(self,winner,loser):
        for x in range(len(loser.weapons)):
            winner.weapons.append(loser.weapons[x])
            print(f"{winner.name} has  obtained {loser.name}'s {loser.weapons[0].name}. Weild it well!")
    def heal(self):
        self.health+=25
    def step_on_snake(self):
        self.health=0
        self.alive=False
        print ("oh no! A snake! I've got a bad bite...I see the light")

class Giant(Player):
    def __init__(self,name,health=200):
        super().__init__(name,health)
    def heal(self):
        self.health+=20
# added class just to examine child/parent relationships and to create a method in the child to over ride the parent



# right now this only exists to test the creation of an enemy and if killing it works,it does!
def  create_orc(): 
    EnemyOne=Player('The Orc')
    print ("A Ghastly Orc approaches, he doesn't look friendly!")
    killQuestion=input("Would you like to attack?(y/n)")
    if killQuestion == "y":
        while EnemyOne.health>0:
            P1.attack(EnemyOne)
            if EnemyOne.health>0:
                print (f"Nice Shot! He only has {EnemyOne.health} health left!")
    else:
        print("Alright, he shall live another day...wait...what's this?")
        P1.step_on_snake()

def create_giant():
    EnemyTwo=Giant("The Giant")
    print(f'{EnemyTwo.name} has come stumbling over a hill in the distance')
    killQuestion=input("Would you like to attack?(y/n)")
    if killQuestion == "y":
        while EnemyTwo.health>0:
            print("You perform an offensive maneuver!")
            P1.attack(EnemyTwo)
            
            if EnemyTwo.health>0:
                print(f"A striking blow! {EnemyTwo.name} has {EnemyTwo.health}")
                EnemyTwo.heal()
                print(f"but...it looks like he is healing! he is restored to {EnemyTwo.health}")




Character = input("What is your name traveler? \n")
P1=Player(Character)
print (f"Welcome to the outlands {P1.name} !")
create_orc()
create_giant()













