from core.settings import Settings
from core.database import list_hearts

class Spice(Settings):
    def __init__(self, width, height, x, y, file_name, folder_name, hero, type_object = "temporary spice"):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name)
        self.HERO = hero
        self.TYPE = type_object
        self.ANIMATION_COUNT = 0

    def animate_temporary_spice(self):
        if self.TYPE != "temporary spice":
            return

        center_x = self.X + self.WIDTH // 2
        center_y = self.Y + self.HEIGHT // 2

        if self.ANIMATION_COUNT == 0:
            self.WIDTH = 45
            self.HEIGHT = 45
            self.FILE_NAME = "big_spice.png"
            self.load_image()

        if self.ANIMATION_COUNT == 40 or self.ANIMATION_COUNT == 120:
            self.WIDTH = 35
            self.HEIGHT = 35
            self.FILE_NAME = "middle_spice.png"
            self.load_image()

        if self.ANIMATION_COUNT == 80:
            self.WIDTH = 25
            self.HEIGHT = 25
            self.FILE_NAME = "small_spice.png"
            self.load_image()

        self.X = center_x - self.WIDTH // 2
        self.Y = center_y - self.HEIGHT // 2

        if self.ANIMATION_COUNT == 160:
            self.ANIMATION_COUNT = -1

        self.ANIMATION_COUNT += 1

    def check_hero_up(self, step):
        if  self.X < self.HERO.X + self.HERO.WIDTH and self.X + self.WIDTH > self.HERO.X:
            if self.Y + self.HEIGHT <= self.HERO.Y and self.Y + self.HEIGHT + step >= self.HERO.Y:
                self.HERO.HP -= 1
                self.HERO.Y += 15
                del list_hearts[-1]

    def check_hero_down(self, step):
        if  self.X < self.HERO.X + self.HERO.WIDTH and self.X + self.WIDTH > self.HERO.X:
            if self.Y - 2 <= self.HERO.Y + self.HERO.HEIGHT + 2 and self.Y > self.HERO.Y:
                self.HERO.HP -= 1
                self.HERO.Y -= 15
                del list_hearts[-1]
    
    def check_hero_left(self, step):
        if self.Y < self.HERO.Y + self.HERO.HEIGHT and self.Y + self.HEIGHT > self.HERO.Y:
            if self.X + self.WIDTH >= self.HERO.X - 5 and self.X + self.WIDTH < self.HERO.X + self.HERO.WIDTH:
               self.HERO.HP -= 1
               self.HERO.X += 15
               del list_hearts[-1]

    def check_hero_right(self, step):
        if self.Y < self.HERO.Y + self.HERO.HEIGHT and self.Y + self.HEIGHT > self.HERO.Y:
            if self.X <= self.HERO.X + self.HERO.WIDTH + 4 and self.X > self.HERO.X + self.HERO.WIDTH:
                self.HERO.HP -= 1
                self.HERO.X -= 15
                del list_hearts[-1]

    def collision_hero_up(self):
        self.check_hero_up(2)
        self.check_hero_up(4)
    
    def collision_hero_down(self):
        self.check_hero_down(2)
        self.check_hero_down(4)

    def collision_hero_left(self):
        self.check_hero_left(2)
        self.check_hero_left(4)
    
    def collision_hero_right(self):
        self.check_hero_right(2)
        self.check_hero_right(4)