from core.settings import Settings
import pygame
from utils.path_to_hero import find_path_to_hero
from core.database import list_blocks
pygame.init()

class Hero(Settings):
    def __init__(self, width1, height1, x1, y1, file_name1, folder_name1, type_object="hero"):
        super().__init__(width=width1, height=height1, x=x1, y=y1, file_name=file_name1, folder_name=folder_name1, type_object=type_object)
        self.SPEED = 2
        self.load_image()
        self.is_jumping = False
        self.jump_timer = 0

    def get_keys(self):
        return pygame.key.get_pressed()

    def move_hero(self):
        keys = self.get_keys()
        if keys[pygame.K_a]:
            self.collision_left()
            self.X -= self.SPEED
            self.FILE_NAME = "hero_left.png"
            self.DIRECTION_L_R = False
            self.SPEED = 2
            self.load_image()

        if keys[pygame.K_d]:
            self.collision_right()
            self.X += self.SPEED
            self.FILE_NAME = "hero_left.png"
            self.DIRECTION_L_R = True
            self.SPEED = 2
            self.load_image()

        if keys[pygame.K_w]:
            self.collision_up()
            self.Y -= self.SPEED
            self.SPEED = 2
            self.FILE_NAME = "hero.png"
            self.DIRECTION_U_D = True
            self.load_image()
            
        if keys[pygame.K_s]:
            self.collision_down()
            self.Y += self.SPEED
            self.SPEED = 2
            self.FILE_NAME = "hero.png"
            self.DIRECTION_U_D = False
            self.load_image()

    def move_jump(self):
        keys = self.get_keys()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.jump_timer = 15

        if self.is_jumping:
            self.Y += -self.SPEED * 2
            self.jump_timer -= 1
            if self.jump_timer <= 0:
                self.is_jumping = False

    def stop_up(self, block, step):
        if block.X < self.X + step and block.X + block.WIDTH > self.X + step: 
            if block.Y + block.HEIGHT > self.Y - 2 and block.Y + block.HEIGHT < self.Y + self.HEIGHT:
                self.SPEED = 0
    
    def stop_down(self, block, step):
        if block.X < self.X + step and block.X + block.WIDTH > self.X + step: 
            if block.Y <= self.Y + self.HEIGHT + 2 and block.Y > self.Y:
                self.SPEED = 0

    def stop_left(self, block, step):
        if block.Y < self.Y + step and block.Y + block.HEIGHT > self.Y + step:
            if block.X + block.WIDTH >= self.X - 2 and block.X + block.WIDTH < self.X + self.WIDTH:
                self.SPEED = 0

    def stop_right(self, block, step):
        if block.Y < self.Y + step and block.Y + block.HEIGHT > self.Y + step:
            if block.X <= self.X + self.WIDTH + 2 and block.X > self.X + self.WIDTH:
                self.SPEED = 0

    def collision_up(self):
        for block in list_blocks:
            self.stop_up(block= block, step = 0)
            self.stop_up(block= block, step = 2)
            self.stop_up(block= block, step = 6)
            self.stop_up(block= block, step = self.WIDTH // 8)
            self.stop_up(block= block, step = 12)
            self.stop_up(block= block, step = self.WIDTH // 4)

    def collision_down(self):
        for block in list_blocks:
            self.stop_down(block= block, step= 0)
            self.stop_down(block= block, step= 2)
            self.stop_down(block= block, step= self.WIDTH // 8)
            self.stop_down(block= block, step= 6)
            self.stop_down(block= block, step=  self.WIDTH // 4)
            self.stop_down(block= block, step= 12)

    def collision_left(self):
        for block in list_blocks:
            self.stop_left(block= block, step= 0)
            self.stop_left(block= block, step= 2)
            self.stop_left(block= block, step= self.WIDTH // 8)
            self.stop_left(block= block, step= 6)
            self.stop_left(block= block, step=  self.WIDTH // 4)
            self.stop_left(block= block, step= 12)
    
    def collision_right(self):
        for block in list_blocks:
            self.stop_right(block= block, step= 0)
            self.stop_right(block= block, step= 2)
            self.stop_right(block= block, step= self.WIDTH // 8)
            self.stop_right(block= block, step= 6)
            self.stop_right(block= block, step=  self.WIDTH // 4)
            self.stop_right(block= block, step= 12)

hero = Hero(25, 25, 62.5, 62.5, "hero.png", "hero")
list_blocks.append(hero)