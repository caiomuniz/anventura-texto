import items

class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects!")

    def __str__(self):
        print(self.name)


class ConsumableTrader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Consumables Trader"
        self.inventory = [items.MouldyBread(), items.MouldyBread(), items.MouldyBread(), items.DriedMeat(), items.DriedMeat(), items.DriedMeat()]
        self.gold = 100

class WeaponTrader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Weapons Trader"
        self.gold = 100
        self.inventory = [items.Machete(), items.Dagger(), items.RustySword()]
