import pygame
import random
import noise
import itertools
from animals import *
from enviroment import *
from constants import *

pygame.init()



WINDOW =pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0,GRID_HEIGHT), random.randrange(0,GRID_WIDTH))for _ in range(num)])

def draw_grid(terrain_grid):
    for position, terrain in terrain_grid.items():
        col, row = position
        top_left = (col*TILE_SIZE, row*TILE_SIZE)
        grouped = gen_groups()

        if isinstance(terrain, Mountain):
            pygame.draw.rect(WINDOW, colors['BROWN'], (*top_left, TILE_SIZE, TILE_SIZE))
        elif isinstance(terrain, Field):
            pygame.draw.rect(WINDOW, colors['GREEN'], (*top_left, TILE_SIZE, TILE_SIZE))
        elif isinstance(terrain, Water):
            pygame.draw.rect(WINDOW, colors['BLUE'], (*top_left, TILE_SIZE, TILE_SIZE))
        elif isinstance(terrain, Forest):
            pygame.draw.rect(WINDOW, colors['D_GREEN'], (*top_left, TILE_SIZE, TILE_SIZE))
        elif isinstance(terrain, Dirt):
            pygame.draw.rect(WINDOW, colors['GREY'], (*top_left, TILE_SIZE, TILE_SIZE))


    for row in range (GRID_HEIGHT):
        pygame.draw.line(WINDOW, colors['BLACK'], (0,row*TILE_SIZE), (WIDTH, row*TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(WINDOW, colors['BLACK'], (col*TILE_SIZE, 0 ), (col*TILE_SIZE, HEIGHT))

def generate_terrain():
    terrain_grid = {}
    scale = 20

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):              
            value = noise.pnoise2(col/scale, row/scale, octaves = 6, persistence = 0.5, lacunarity = 2.0, repeaty = 1024, base = 42)
            terrain_type = choose_terrain_based_on_height(value)
            terrain_type.altitude = value
            terrain_grid[(col, row)] = terrain_type

    return terrain_grid

def choose_terrain_based_on_height(terrain):
    if terrain > 0.27:
        return Mountain()
    elif terrain > 0.15:
        return Forest()
    elif terrain > -0.2:
        return Field()
    else:
        return Water()

def gen_groups(num_groups = random.randint(1, 7), groups_size = int(round(random.gauss(15, 5)))):
    groups = []
    for _ in range(num_groups):
        group = gen(groups_size)
        groups.append(group)
    return groups
    
def draw_animals(all_animals, terrain_grid):
    if len (all_animals) > 0:
        for dinosaur in all_animals:
            col, row = dinosaur.position
            size = 1


            print(f"Dinosaur at position ({col}, {row}) with size {size}")
            
            for i in range(size):
                for j in range(size):
                    top_left = ((col + i) * TILE_SIZE, (row + j) * TILE_SIZE)

                    if dinosaur.diet == 'plants':
                        pygame.draw.rect(WINDOW, dino_colors['ORANGE'], (*top_left, TILE_SIZE, TILE_SIZE))
                    elif dinosaur.diet == 'meat':
                        pygame.draw.rect(WINDOW, dino_colors['RED'], (*top_left, TILE_SIZE, TILE_SIZE))
                    else:
                        pass
    else:
        print('No dinosaurs are charged.')

def draw_animal_moves(terrain_grid, all_animals):
    new_animals = itertools.zip_longest(all_animals, all_animals, fillvalue= None)
    new_animals_dict= dict(new_animals)

    for dinosaur_name, dinosaur_position in new_animals_dict.items():
       # old_animals = dinosaur_position.position
        new_animals = dinosaur_name.move(dinosaur_position, new_animals)

        for dinosaur in new_animals_dict:
            col, row = dinosaur.position
            top_left = (col * TILE_SIZE, row * TILE_SIZE)
            if dinosaur.diet == 'plants':
                pygame.draw.rect(WINDOW, dino_colors['ORANGE'], (*top_left, TILE_SIZE, TILE_SIZE))
            elif dinosaur.diet == 'meat':
                pygame.draw.rect(WINDOW, dino_colors['RED'], (*top_left, TILE_SIZE, TILE_SIZE))

#    for dinosaur in all_animals:
#        col, row = dinosaur.position
#        top_left = (col * TILE_SIZE, row * TILE_SIZE)
#        if dinosaur.diet == 'plants':
#            pygame.draw.rect(WINDOW, dino_colors['ORANGE'], (*top_left, TILE_SIZE, TILE_SIZE)) 
#        elif dinosaur.diet == 'meat':
#            pygame.draw.rect(WINDOW, dino_colors['RED'], (*top_left, TILE_SIZE, TILE_SIZE))

                


def main():
    running = True
    playing = False
    count = 0
    update_freq = 30
    all_animals = []
    max_animals = 20
    terrain_grid = generate_terrain()

    
    
    def gen_animals():
        num_dinasours = min(random.randint(15, 20), max_animals - len(all_animals))
        for _ in range(num_dinasours):            
            dinosaur_class = random.choice([Iguanodon, Compsognathus])
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            dinosaur = dinosaur_class()
            dinosaur.position = position
            all_animals.append(dinosaur)

    def grow():
        for terrain in terrain_grid:
            if isinstance (terrain, Field):
                terrain.grow_grass()
            elif isinstance (terrain, Forest):
                terrain.grow_leaf()
            else:
                pass
    gen_animals()

    WINDOW.fill(colors['BLACK'])
    draw_grid(terrain_grid)
    draw_animals(all_animals, terrain_grid)
    pygame.display.update()
    
    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0

        pygame.display.set_caption("Simulation paused" if playing else "Simulating")

    
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass #waiting to the dino generation

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                # ERASE ALL THE ANIMALS
                if event.key == pygame.K_c:
                    all_animals = []
                    count = 0
                # GEN ANIMALS AGAIN
                if event.key == pygame.K_b:
                    all_animals = []
                    gen_animals()
                    draw_animals(all_animals, terrain_grid)

                if event.key == pygame.K_t:
                    WINDOW.fill(colors['BLACK'])
                    terrain_grid = generate_terrain()
                    draw_grid(terrain_grid)
                    pygame.display.flip()  

        WINDOW.fill(colors['BLACK'])
        draw_grid(terrain_grid)
        grow()
        if count % 2 == 0:
            for dinosaur in all_animals:
                dinosaur.move(terrain_grid, dinosaur)
            draw_animal_moves(terrain_grid, all_animals)
        pygame.display.update()  
            
    pygame.quit()

if __name__ == "__main__":
    main()