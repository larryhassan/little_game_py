import pygame
import math


''' Why pygame.sprite.Group()
    (1). Easy updating
    (2) Easily draw
    (3) updating variables is easy.
   Sprite has a two dimentional character.
   Any two dimentional character is a Sprite.
-- Hitbox is a way that sprite is represented.
'''



WINDOW_SIZE = [1400, 700]
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
COLOR = [59, 77, 82]
SCREEN.fill(COLOR)

pygame.init() #initializes all of pygame modules


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load('Racing Car Sprites/' + image)
        self.image = pygame.transform.flip(self.image, False, True) # horizontal flip, Vertical flip.
        self.image2 = pygame.image.load('Racing Car Sprites/' + image)
        self.image2 = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = x,y
        self.scale = 0.5
        self.angle = 0

       # self.joystick = pygame.joystick.Joystick(1) #second device of (1), first device is (0). 
        #self.joystick.init()# get the joystick ready to be used.

        #self.horiz_axis = None
        #self.vert_axis = None
        
    def rotate(self, image, angle, scale):
        surface = pygame.transform.rotozoom(surface, angle, scale)
        return surface
    
    def update(self):
        #keyboard version
        for event in pygame.event.get():
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rect.y -= 5
                if event.type == pygame.K_DOWN:
                    self.rect.y += 5

        #joy stick version
        #self.horiz_axis = self.joystick.get_axis(0)
        #self.vert_axis = self.joystick.get_axis(1)
                
        self.image = self.rotate(self.image2, self.angle, self.scale)
        #self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        #self.image = self.rotate(self.image2, self.angle, 1)
        #self.angle += 5
        if self.angle > 360:
            self.angle = 0

        
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite. __init__(self)  #Parent class helps with the self.image attribute.
        self.image = pygame.image.load('tiles/' + image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Tile_map():
    def __init__(self, filename):
        self.tile_size = (92,63)
    def load_map(self, filename):
        meta = open(filename)
        #meta = meta.readlines()
        #meta.rstrip()
        ma = []
        li = []
        for item in meta:
            a = item.split(',')
            li = []
            for line in a:
                if line != '\n':
                    li.append(line)
                else:
                    break

            ma.append(li)

        return ma

    def load_tiles(self, filename):
        back_tiles = []
        back_tiles2 = []

        road_tiles = []
        road_tiles2 = []

        bend_tiles1 = []
        bend_tiles2 = []
        bend_tiles3 = []
        bend_tiles4 = []
        
        map1 = self.load_map(filename)
        x, y = 0, -1230  # tuple datatype 

        for row in map1:
            x = 0
            for tile in row:
                if tile == '1':
                    road_tiles2.append(Tile(x,y, 'Road_Side2.png'))
                if tile == '2':
                    road_tiles.append(Tile(x,y, 'Road_Main2.png'))
                if tile == '4':
                    bend_tiles2.append(Tile(x,y, 'Road_01_Tile_02.png'))
                if tile == '5':
                    road_tiles.append(Tile(x,y, 'Road_Main.png'))
                if tile == '6':
                    back_tiles2.append(Tile(x,y, 'Bush_01.png'))
                if tile == '7':
                    bend_tiles3.append(Tile(x,y, 'Road_01_Tile_03.png'))
                if tile == '8':
                    bend_tiles1.append(Tile(x,y, 'Road_01_Tile_01.png'))
                if tile == '9':
                    bend_tiles4.append(Tile(x,y, 'Road_01_Tile_04.png'))
                if tile == '10':
                    back_tiles.append(Tile(x,y, 'Grass_Tile2.png'))
                if tile == '11':
                    back_tiles2.append(Tile(x,y, 'Bush_02.png'))
                if tile == '12':
                    road_tiles2.append(Tile(x,y, 'Road_Side.png'))
                if tile == '13':
                    player = Player(x, y, 'green_car.png')
                    cars.add(player)  #what is the difference between 'add' and 'append' here?

                if tile !=',':
                    x += self.tile_size[0]
            y += self.tile_size[1]
            
        return back_tiles, back_tiles2, road_tiles, road_tiles2, bend_tiles1, bend_tiles2, bend_tiles3, bend_tiles4

'''Question: list road_tiles2 has two different list of items?
'''
all_tiles = pygame.sprite.Group() #this instance allows to move all tiles(character) at the same time. 

back_tiles = pygame.sprite.Group()
back_tiles2 = pygame.sprite.Group()

road_tiles = pygame.sprite.Group()
road_tiles2 = pygame.sprite.Group()

bend_tiles1 = pygame.sprite.Group()
bend_tiles2 = pygame.sprite.Group()
bend_tiles3 = pygame.sprite.Group()
bend_tiles4 = pygame.sprite.Group()


cars = pygame.sprite.Group()
tiler = Tile_map('map1b.txt') #map1b is for background tiles
btiles = tiler.load_tiles('map1b.txt') 

'''the result value is a tuple from the return keyword in the load_tile function. Once
you assigne more than two values to a variable, it's a tuple.'''

for tile in btiles[0]:
    back_tiles.add(tile)
    all_tiles.add(tile)


tiles = tiler.load_tiles('map1.txt')
for tile in tiles[1]:
    back_tiles2.add(tile)
    all_tiles.add(tile)

for tile in tiles[2]:
    road_tiles.add(tile)
    all_tiles.add(tile)


for tile in tiles[3]:
    road_tiles2.add(tile)
    all_tiles.add(tile)

for tile in tiles[4]:
    bend_tiles1.add(tile)
    all_tiles.add(tile)

for tile in tiles[5]:
    bend_tiles2.add(tile)
    all_tiles.add(tile)

for tile in tiles[6]:
    bend_tiles3.add(tile)
    all_tiles.add(tile)

for tile in tiles[7]:
    bend_tiles4.add(tile)
    all_tiles.add(tile)


def align_car():
    for player in cars:
        while player.rect.y > 500:
            player.rect.y -= 200
            for tile in all_tiles:
                tile.rect.y -= 100
        while player.rect.y < 400:
            player.rect.y += 100
            for tile in all_tiles:
                tile.rect.y += 100
            
align_car()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    SCREEN.fill(COLOR)
    back_tiles.draw(SCREEN)
    
    road_tiles.draw(SCREEN)
    road_tiles2.draw(SCREEN)

    bend_tiles1.draw(SCREEN)
    bend_tiles2.draw(SCREEN)
    bend_tiles3.draw(SCREEN)
    bend_tiles4.draw(SCREEN)
    
    back_tiles2.draw(SCREEN)

    cars.draw(SCREEN)
    cars.update()

    
    pygame.display.flip()
    clock.tick(60)


#w = maper.load_map('map1.txt')
#print(w)
