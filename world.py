import random
import enemies
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
        You find yourself in a dark forest with only a campfire in front of you.
        You can make out four paths, each equally as dark and foreboding in the woods.
        """

class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's your friends' camp!


        Victory is yours!
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from its web in front of you!"
            self.dead_text = "The corpse of a dead spider rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "A mighty ogre blocks your path."
            self.dead_text = "A dead ogre reminds you of your tryumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "Seems like you got lost in the middle of a smarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockElemental()
            self.alive_text = "A pile of rocks seems to have found its way to me middle of the room. When you get near it, you see it's a Rock Elemental!"
            self.dead_text = "As it was defeated, it became a pile of crumbled rocks."

        super().__init__(x,y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive
        else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

world_dsl = """
|  |VT|  |
|  |EN|  |
|EN|ST|EN|
|  |EN|  |
"""

tile_type_dict = {"VT": VictoryTile, "EN": EnemyTile, "ST": StartTile, "  ": None}


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
            tile_type = tyle_tipe_dict[dsl_cell]
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
    pipe_counts = [line.count("|") fo line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True
def tile_at(x, y):
    if x< 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
