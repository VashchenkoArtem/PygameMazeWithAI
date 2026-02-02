import pygame
from utils.path_to_texture import find_path_to_texture

pygame.init()

class Settings():
    def __init__(self, width= 50, height= 50, x= 0, y= 0, file_name= None, folder_name= None, type_object = None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.IMG = None
        self.FILE_NAME = file_name
        self.FOLDER_NAME = folder_name
        self.TYPE = type_object
        self.DIRECTION_L_R = False
        self.DIRECTION_U_D = False

    def load_image(self):
        image_load = pygame.image.load(find_path_to_texture(self.FILE_NAME, self.FOLDER_NAME))
        image_load = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        self.IMG = pygame.transform.flip(image_load, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)

    def blit_sprite(self, screen):
        screen.blit(self.IMG, (self.X, self.Y))