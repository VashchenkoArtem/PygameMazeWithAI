import pygame
from core.settings import Settings

pygame.init()

class Block(Settings):
    def __init__(self, width, height, x, y, file_name, folder_name):
        Settings.__init__(self, width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name)
        self.load_image()