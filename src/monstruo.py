import criatura

class Monstruo(criatura.Criatura):
    def __init__(self, HP, ATK, DEF, Nombre):
        criatura.Criatura(HP, ATK, DEF)
        self.Nombre = Nombre