import random
from constants import colors

class Terrain():
    def __init__(self):
        self.__spawneable = bool()
        self.__altitude = int()

class Usefull(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.__spawneable = True
        self.__color = None

class Unusefull(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.__spawneable = False
        self.__color = colors['BLACK']

    def get_color(self):
        return self.__color

class Mountain(Usefull):
    def __init__(self) -> None:
        super().__init__()
        self.__spawneable = False
        self.__altitude = random.randint(40, 100)
        self.__color = colors['BROWN']
        self.__vision = 8

    def get_color(self):
        return self.__color

class Field(Usefull):
    def __init__(self) ->None:
        super().__init__()
        self.__spawneable = True
        self.__altitude = random.randint(0, 39)
        self.__color = colors['GREEN']
        self.__vision = 10

    def get_color(self):
        return self.__color

class Water(Usefull):
    def __init__(self) ->None:
        super().__init__()
        self.__spawneable = False
        self.__altitude = random.randint(-50, -1)
        self.__color = colors['BLUE']
        # Vision is not relevant for water
    def get_color(self):
        return self.__color

class Forest(Usefull):
    def __init__(self) ->None:
        super().__init__()
        self.__spawneable = True
        self.__altitude = random.uniform(20, 60)
        self.__color = colors['D_GREEN']
        self.__vision = 5

    def get_color(self):
        return self.__color

class Dirt(Usefull):
    def __init__(self) -> None:
        super().__init__()
        self.__spawneable = True
        self.__altitude = random.randint(0, 39)
        self.__color = colors['GREY']
        self.__vision = 10

    def get_color(self):
        return self.__color