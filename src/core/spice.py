from core.settings import Settings


class Spice(Settings):
    def __init__(self, width, height, x, y, file_name, folder_name, hero, type_object = "temporary spice"):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name)
        self.HERO = hero
        self.TYPE = type_object

    def check_hero_up(self, step):
        if  self.X < self.HERO.X + self.HERO.WIDTH and self.X + self.WIDTH > self.HERO.X:
            if self.Y + self.HEIGHT <= self.HERO.Y and self.Y + self.HEIGHT + step >= self.HERO.Y:
                self.HERO.HP -= 1
                print(self.HERO.HP)
                self.HERO.Y += 15

    def collision_hero_up(self):
        self.check_hero_up(2)
        self.check_hero_up(4)