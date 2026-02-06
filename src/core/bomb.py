from core.spice import Spice
from core.hero import hero
from utils.check_collision_hero import *
from core.database import list_blocks
from utils.heart import damage_hero

class Bomb(Spice):
    def __init__(self, x, y, file_name, folder_name, type_object, width= 45, height= 45, hero = hero):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name, type_object= type_object, hero= hero)
        self.is_exploded = False
        self.explosion_timer = 120

    def collision_hero_bomb_up(self):
        if is_collision_hero_up(self, self.HERO):
            self.Y += 10
            self.HERO.freeze(2)
            self.is_exploded = True 
            damage_hero(3, self.HERO)       
    
    def collision_hero_bomb_down(self):
        if is_collision_hero_down(self, self.HERO):
            self.Y -= 10
            self.HERO.freeze(2)
            self.is_exploded = True
            damage_hero(3, self.HERO)  
    
    def collision_hero_bomb_right(self):
        if is_collision_hero_right(self, self.HERO):
            self.HERO.X -= 10
            self.HERO.freeze(2)
            self.is_exploded = True
            damage_hero(3, self.HERO)
    
    def collision_hero_bomb_left(self):
        if is_collision_hero_left(self, self.HERO):
            self.HERO.X += 10
            self.HERO.freeze(2)
            self.is_exploded = True
            damage_hero(3, self.HERO) 

    def if_exploded(self):
        if self.is_exploded:
            self.FILE_NAME = "explosion.png"
            self.FOLDER_NAME = "effects"
            self.load_image()
            self.explosion_timer -= 1
            if self.explosion_timer <= 0:
                list_blocks.remove(self)
                self.is_exploded = False