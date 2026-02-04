from core.settings import Settings
from core.database import list_hearts

class Heart(Settings):
    def __init__(self, x, y, width= 50, height= 50, file_name= "heart.png", folder_name= "icons"):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name)

def generate_heart(hp):
    x = 10
    for heart in range(hp):
        heart = Heart(x, 0)
        heart.load_image()
        list_hearts.append(heart)
        x += 60