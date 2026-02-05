from core.settings import Settings


class Bomb(Settings):
    def __init__(self, x, y, file_name, folder_name, type_object, width= 45, height= 45):
        super().__init__(width= width, height= height, x= x, y= y, file_name= file_name, folder_name= folder_name, type_object= type_object)