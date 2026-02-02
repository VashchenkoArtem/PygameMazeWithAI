import pygame
from core.setup import clock
from core.components.create_map import game_map
from core.database import list_blocks
from core.setup import screen

def run_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for block in list_blocks:
            block.blit_sprite(screen)
        pygame.display.flip()
        clock.tick(60)