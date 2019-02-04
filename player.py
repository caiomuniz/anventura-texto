import items
import world

class Player:
    def __init__(self):
        self.inventory = [items.Club(),
                         items.MouldyBread()
                         ]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('> ' + str(item))
        print("Gold: {}.".format(self.gold))
        self.print_life()

    def print_life(self):
        if self.hp < 25:
            print("You are in critical condition. You should heal now!")
        elif self.hp < 50:
            print("You have some wounds. but nothing critical")
        elif self.hp < 100:
            print("You have just some bruises.")
        else:
            print("You have full life.")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item  in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def most_powerful_armor(self):
        max_armor = 0
        best_armor = None
        for item  in self.inventory:
            try:
                if item.armor > max_armor:
                    best_armor = item
                    max_armor = item.armor
            except AttributeError:
                pass
        return best_armor

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name,enemy.name))
        enemy.hp -=  best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} receives {} damage".format(enemy.name, best_weapon.damage))

    def heal(self):
        consumables = [ item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You do not have any healing items on you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice)-1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (IndexError, ValueError):
                print("Invalid choice. Try again.")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx = 0,dy = -1)

    def move_south(self):
        self.move(dx = 0,dy = 1)

    def move_east(self):
        self.move(dx = 1,dy = 0)

    def move_west(self):
        self.move(dx = -1,dy = 0)
