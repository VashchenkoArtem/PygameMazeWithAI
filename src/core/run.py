import pygame
from core.setup import clock
from core.components.create_map import game_map
from core.database import list_blocks
from core.setup import screen
from core.hero import hero

def run_game():

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for hero in list_blocks:
            if hero.TYPE == "hero":
                hero.blit_sprite(screen)
                
                hero.move_hero()
                hero.move_run()
                hero.move_jump()
                
        for block in list_blocks:
            block.blit_sprite(screen)
        pygame.display.flip()
        clock.tick(60)