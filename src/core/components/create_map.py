import pygame
from core.settings import Settings
from core.block import Block
from core.database import list_map, list_blocks
from core.setup import screen
from core.spice import Spice
from core.hero import hero

pygame.init()

class Map(Settings):
    def __init__(self, x1 = 0, y1 = 0):
        Settings.__init__(self, x= x1, y= y1)

    def create_map(self):
        x = self.X
        y = self.Y
        for list_row in list_map:
            for block in list_row:
                if block == 1:
                    wall = Block(width= 50, height= 50, x= x, y= y, file_name= "block.png", folder_name= "background")
                    wall.load_image()
                    list_blocks.append(wall)
                if block == 2:
                    spice = Spice(width= 45, height= 45, x= x + 2.5, y= y + 2.5, file_name= "spice.png", folder_name= "enemies", hero= hero)
                    spice.load_image()
                    list_blocks.append(spice)
                x += 50
            y += 50
            x = self.X
game_map = Map()
game_map.create_map()