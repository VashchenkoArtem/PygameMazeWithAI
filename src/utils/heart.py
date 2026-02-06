from core.settings import Settings
from core.database import list_hearts

class Heart(Settings):
    def __init__(self, x, y, width= 50, height= 50, file_name= "heart.png", folder_name= "icons"):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name)

def generate_heart(hp):
    global list_hearts
    x = 10
    for heart in range(hp):
        heart = Heart(x, 0)
        heart.load_image()
        list_hearts.append(heart)
        x += 60
    return list_hearts
    
def damage_hero(damage_in_hp, hero):
    global list_hearts
    for heart in range(damage_in_hp):
        if len(list_hearts) > 0:
            del list_hearts[-1]
            hero.HP -= 1
            damage_in_hp -= 1
        else:
            list_hearts.clear()
            hero.HP = 0
    hero.is_dead()