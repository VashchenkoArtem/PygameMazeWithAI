import pygame
from core.setup import clock
from core.components.create_map import game_map
from core.database import list_blocks, list_hearts
from core.setup import screen
from core.hero import hero
from utils.heart import generate_heart

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
                hero.update_freeze()

                if not hero.is_frozen:
                    hero.move_hero()
                    hero.move_run()
                    hero.move_jump()
                
        for block in list_blocks:
            if block.TYPE == "temporary spice" or block.TYPE == "default spice":

                block.collision_hero_up()
                block.collision_hero_down()
                block.collision_hero_left()
                block.collision_hero_right()
                block.animate_temporary_spice()

            if block.TYPE == "bomb":
                block.collision_hero_bomb_up()
                block.collision_hero_bomb_down()
                block.collision_hero_bomb_left()
                block.collision_hero_bomb_right()
                block.if_exploded()

            block.blit_sprite(screen)
        for heart in list_hearts:
            heart.blit_sprite(screen)
        pygame.display.flip()
        clock.tick(60)