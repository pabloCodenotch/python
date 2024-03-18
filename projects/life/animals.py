import random
from constants import GRID_HEIGHT, GRID_WIDTH
from enviroment import Mountain, Water

class Dinosauria:
    def __init__(self) -> None:
        self.size = int
        self.__alive = True 
        self.food = int
        self.hunger = 0
        self.gender = random.choice(['Male', 'Female'])
        self.age = int
        self.max_age = int
        self.__corpse = False 
        self.vision_range = int
        self.position = ()

    def __iter__(self):
        yield self.position
                
    def death(self):
        if self.__alive== False:
            self.__corpse = True
            print("Dinosaur is dead.")
        elif self.age == self.max_age:
            self.__corpse = True
            print("Dinosaur is dead.")        
        else:
            self.__corpse = False
    
    def eat(self):
        pass # Waiting to code food mechanic

    def starve(self):
        if self.hunger == self.food:
            self.death()
        elif self.hunger > self.food / 2:
            self.eat()
        else:
            pass
    
    def move(self, terrain_grid, all_animals):
    
        move_x = random.choice([-1, 0, 1])
        move_y = random.choice([-1, 0, 1])
        new_position = (self.position[0] + move_x, self.position[1] + move_y)
        (x, y) = new_position
            
        if self.hunger > self.food / 4:
            pass
        if self.is_valid_move(new_position, terrain_grid, all_animals):
            #move = list(self.position)
            #move[0], move[1] = x, y
            #self.position = tuple(move)
            return new_position
        else:
            move = list(self.position)
            move[0], move[1] = x, y
            self.position = tuple(move)
            print ('moved')
            #return self.position
            return new_position
                    

    def is_valid_move(self, new_position,terrain_grid, all_animals):
        col, row = new_position
                      
        for dinosauria in all_animals:
            if col < 0 or col >= GRID_WIDTH or row < 0 or row >= GRID_HEIGHT:
                return False
            elif self.position != new_position and self.manhattan_distance(self.position, new_position) < self.vision_range:
                return False
            if isinstance(new_position, (Mountain, Water)):
                return False
            else:
                return True
               
    
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

class Hervibore(Dinosauria):
    def __init__(self) ->None:
        super().__init__()
        self.diet = 'plants'

class Carnivore(Dinosauria):
    def __init__(self):
        super().__init__()
        self.diet = 'meat'

class Iguanodon(Hervibore):
    def __init__(self) -> None:
        super().__init__()
        self.size = 2
        self.name = "Iguanodon"
        self.food = 30
        self.age = random.randint(0, 30)
        self.max_age = 31
        self.vision_range = 6

class Compsognathus(Carnivore):
    def __init__(self) -> None:
        super().__init__()
        self.size = 1
        self.name = "Compy"
        self.food = 5
        self.age = random.randint(0, 10)
        self.max_age = 11
        self.vision_range = 5