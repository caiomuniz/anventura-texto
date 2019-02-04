import random
import enemies
import npc
from player import Player


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError ("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):

    def intro_text(self):
        return """
        You find yourself in a dark room inside an old mansion.
        There is nothing special about this room.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's the exit door!


        Victory is yours!
        """

    def modify_player(self, player):
        player.vitory = True

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = """
            A giant spider jumps down from its web in front of you!
            """
            self.dead_text = """
            The corpse of a dead spider rots on the ground.
            """
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = """
            A mighty ogre blocks your path.
            """
            self.dead_text = """
            A dead ogre reminds you of your tryumph.
            """
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = """
            Seems like you got lost in the middle of a smarm of bats!
            """
            self.dead_text = """
            Dozens of dead bats are scattered on the ground.
            """
        else:
            self.enemy = enemies.RockElemental()
            self.alive_text = """
            A pile of rocks seems to have found its way to me middle of the room. When you get near it, you see it's a Rock Elemental!
            """
            self.dead_text = """
            As it was defeated, it became a pile of crumbled rocks.
            """

        super().__init__(x,y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - (self.enemy.damage - 0.5*player.most_powerful_armor())
            print("Enemy does {} damage.".format(self.enemy.damage))
            if player.hp < 25:
                print("You are in critical condition, you should heal.")

#Tiles where the consumable Trader is.
class TraderTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {}".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

        def swap(self, seller, buyer, item):
            if item.value > buyer.gold:
                print("Not enough gold to make the trade.")
                return
            seller.inventory.remove(item)
            buyer.inventory.append(item)
            seller.gold = seller.gold + item.value
            buyer.gold = buyer.gold - item.value
            print("Trade complete!")

        def check_if_trade(self, player):
            while True:
                print("Would you like to (B)uy, (S)ell or (Q)uit? ")
                user_input = input("> ")
                if user_input in ['q','Q']:
                    return
                elif user_input in ['b', 'B']:
                    print("Here's what's available to buy: ")
                    self.trade(buyer = player, seller = self.trader)
                elif user_input in ['s', 'S']:
                    print("What do you want to sell? ")
                    self.trade(buyer = self.trader, seller = player)
                else:
                    print("Invalid option!")

class ConsumableTraderTile(TraderTile):
    def __init__(self, x, y):
        self.trader = npc.ConsumableTrader()
        super().__init__(x, y)

    def intro_text(self):
        return """
        A tall hooded figure looks at you and clinks some of his gold coins between his hands, looking at you.
            "Do you wish to trade?"
        """
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell or (Q)uit? ")
            user_input = input()
            if user_input in ['q','Q']:
                return
            elif user_input in ['b', 'B']:
                print("Here's what's available to buy: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input in ['s', 'S']:
                print("What do you want to sell? ")
                self.trade(buyer = self.trader, seller = player)
            else:
                print("Invalid option!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {}".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

        def swap(self, seller, buyer, item):
            if item.value > buyer.gold:
                print("Not enough gold to make the trade.")
                return
            seller.inventory.remove(item)
            buyer.inventory.append(item)
            seller.gold = seller.gold + item.value
            buyer.gold = buyer.gold - item.value
            print("Trade complete!")

class WeaponTraderTile(TraderTile):
    def __init__(self, x, y):
        self.trader = npc.WeaponTrader()
        super().__init__(x, y)

    def intro_text(self):
        return """
        A tall hooded figure looks at you and clinks some of his gold coins between his hands, looking at you.
            "Do you wish to trade?"
        """
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell or (Q)uit? ")
            user_input = input()
            if user_input in ['q','Q']:
                return
            elif user_input in ['b', 'B']:
                print("Here's what's available to buy: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input in ['s', 'S']:
                print("What do you want to sell? ")
                self.trade(buyer = self.trader, seller = player)
            else:
                print("Invalid option!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {}".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("Not enough gold to make the trade.")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Just an unremarkable part of this mansion.
            You should move onwards...
            """
        else:
            return """
            You found some gold dropped on the floor, and pick it up.
            """
class HealingTile(MapTile):
    def intro_text(self):
        return """
        At the moment you enter this room, you feel all your wounds being cured and you feel restored.
        """

    def modify_player(self, player):
        cured_hp = 100 - player.hp
        player.hp = 100
        print("+ {} HP.".format(cured_hp))

class BossTile(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.GateKeeper()
        self.alive_text = """
        There is a gigantic golem blocking your path to your next objective.
        It looks menacing and ready to attack.
        """
        self.dead_text = """
        There are now just a lot of rocks where once stood a giant golem blocking your way.
        When you look to it, you feel proud of yourdelf to have been able to defeat it.
        """
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining. ".format(self.enemy.damage, player.hp))



def tile_at(x, y):
    if x< 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

world_dsl = """
|ET|  |FG|ET|  |  |  |  |  |FG|BT|HT|FG|
|ET|  |  |ET|  |  |  |  |  |HT|  |FG|  |
|HT|ET|ET|ST|  |WT|FG|CT|ET|FG|  |  |VT|
|ET|  |  |ET|  |  |ET|  |  |ET|WT|CT|BT|
|ET|  |  |FG|ET|FG|ET|  |  |ET|  |  |CT|
|FG|WT|  |ET|  |  |ET|  |  |ET|  |  |WT|
|FG|  |ET|FG|  |FG|ET|FG|ET|ET|ET|ET|FG|
"""

tile_type_dict = {
"VT": VictoryTile,
"ET": EnemyTile,
"ST": StartTile,
"CT": ConsumableTraderTile,
"WT": WeaponTraderTile,
"FG": FindGoldTile,
"HT": HealingTile,
"BT": BossTile,
"  ": None
}

start_tile_location = None
world_map = []

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    #Separa as linhas do mapa em DSL
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    #Separa as colunas do DSL
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        #Cria cada uma das células do mapa
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x,y) if tile_type else None)

        world_map.append(row)


##If the DSL created is or not valid
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True
