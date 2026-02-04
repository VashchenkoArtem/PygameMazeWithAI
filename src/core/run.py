import pygame
from core.setup import clock
from core.components.create_map import game_map
from core.database import list_blocks, list_hearts
from core.setup import screen
from core.hero import hero
from core.heart import generate_heart

def run_game():
    running = True
    generate_heart(5)
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for hero in list_blocks:
            if hero.TYPE == "hero":
                hero.blit_sprite(screen)
                
                hero.is_dead()

                hero.move_hero()
                hero.move_run()
                hero.move_jump()
                
        for block in list_blocks:
            if block.TYPE == "temporary spice":

                block.collision_hero_up()
                block.collision_hero_down()
                block.collision_hero_left()
                block.collision_hero_right()
            block.blit_sprite(screen)
        for heart in list_hearts:
            heart.blit_sprite(screen)
        pygame.display.flip()
        clock.tick(60)