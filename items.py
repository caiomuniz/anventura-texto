########## Super classes ##########
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects!")

    def __str__(self):
        return self.name

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects!")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name, self.healing_value)

########## Weapons ##########

class Plank (Weapon):
    def __init__(self):
        self.name = "Plank"
        self.description =  "A broken plank found on the floor."\
                            "Not very strong, but better than bare fists."
        self.damage = 5

class Dagger (Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                        "Somewhat more dangerous than a plank."
        self.damage = 10

class RustySword (Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description =  "This sword is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20

class Machete (Weapon):
    def __init__(self):
        self.name = "Machete"
        self.description = "An old machete, but still have some strenght in it."
        self.damage = 25

########## Consumables ##########

class MouldyBread(Consumable):
    def __init__(self):
        self.name = "Mouldy Bread"
        self.healing_value = 10
