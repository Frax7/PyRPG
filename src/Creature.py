class Creature ():

    def __init__ (self, atk, deff, hp):
        self.damage = atk
        self.armor = deff
        self.hp = hp

    def attack (self, attacked_creature):
        newHp -= int(self.damage - (self.armor / 3))
        attacked_creature.setHp(newHp)

    def attacked (self, atk):
        self.hp -= atk - (self.armor / 3)

    def getHp (self):
        return self.hp

    def setHp (self, hp):
        self.hp = hp
