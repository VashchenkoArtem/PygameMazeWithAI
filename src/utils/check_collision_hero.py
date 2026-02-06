def is_collision_hero_up(block, hero):
    if  block.X < hero.X + hero.WIDTH and block.X + block.WIDTH > hero.X:
        if block.Y + block.HEIGHT <= hero.Y and block.Y + block.HEIGHT >= hero.Y:
            return True
        
def is_collision_hero_down(block, hero):
    if  block.X < hero.X + hero.WIDTH and block.X + block.WIDTH > hero.X:
        if block.Y - 2 <= hero.Y + hero.HEIGHT + 2 and block.Y > hero.Y:
            return True
        
def is_collision_hero_left(block, hero):
    if block.Y < hero.Y + hero.HEIGHT and block.Y + block.HEIGHT > hero.Y:
        if block.X + block.WIDTH >= hero.X - 5 and block.X + block.WIDTH < hero.X + hero.WIDTH:
            return True
    
def is_collision_hero_right(block, hero):
    if block.Y < hero.Y + hero.HEIGHT and block.Y + block.HEIGHT > hero.Y:
        if block.X <= hero.X + hero.WIDTH + 4 and block.X > hero.X + hero.WIDTH:
            return True