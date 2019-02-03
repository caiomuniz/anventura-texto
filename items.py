########## Super classes ##########
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects!")

    def __str__(self):
        return "{}: {}".format(self.name, self.description)

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects!")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing_value)

########## Weapons ##########

class Club(Weapon):
    def __init__(self):
        self.name = "Club"
        self.description =  "A half-burnt piece of wookd taken out of the campfire."\
                            "Not very strong, but better than bare fists."
        self.damage = 5
        self.value = 2

class Dagger (Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                        "Somewhat more dangerous than a plank."
        self.damage = 10
        self.value = 5

class RustySword (Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description =  "This sword is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20
        self.value = 15

class Machete (Weapon):
    def __init__(self):
        self.name = "Machete"
        self.description = "An old machete, but still have some strenght in it."
        self.damage = 50
        self.value = 60

########## Consumables ##########

class MouldyBread(Consumable):
    def __init__(self):
        self.name = "Mouldy Bread"
        self.healing_value = 10
        self.value = 12

class DriedMeat(Consumable):
    def __init__(self):
        self.name: "Dried Meat"
        self.healing_value = 25
        self.value = 28
