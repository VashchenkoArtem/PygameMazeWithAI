import pygame
from utils.path_to_texture import find_path_to_texture

pygame.init()

class Settings():
    def __init__(self, width= 50, height= 50, x= 0, y= 0, file_name= None, folder_name= None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.IMG = None
        self.FILE_NAME = file_name

    def load_image(self):
        image_load = pygame.image.load(find_path_to_texture(self.FILE_NAME, "background"))
        image_load = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        self.IMG = image_load

    def blit_sprite(self, screen):
        screen.blit(self.IMG, (self.X, self.Y))