from Creature import *
class Warrior(Creature):

    def __init__ (self, atk, deff, hp, fury, name):
        Creature.__init__(self, atk, deff, hp)
        self.fury = fury;
        self.name = name;

    def special_attack (self, attacked_creature):
        attacked_creature.hp -= int(self.damage * 1.5)
    
