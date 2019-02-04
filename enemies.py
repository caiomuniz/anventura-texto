class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects!")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 15

class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of bats"
        self.hp = 100
        self.damage = 4

class RockElemental(Enemy):
    def __init__(self):
        self.name = "Rock Elemental"
        self.hp = 80
        self.damage = 15

class GateKeeper(Enemy):
    def __init__(self):
        self.name = "Gate Keeper"
        self.hp = 500
        self.damage = 20
