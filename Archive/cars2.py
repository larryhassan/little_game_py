import pygame
import math


WINDOW_SIZE = [1400, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)
colour = [59, 77, 82]
screen.fill(colour)
pygame.init()





class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load('tiles/' + image)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.bottom = x, y


class Tile_map():
    def __init__(self, filename):
        self.tile_size = (93, 63)
    def load_map(self, filename):
        meta = open(filename)
        #meta = meta.readlines()
        #meta.rstrip()        
        ma = []
        li = []
        for item in meta :
            a = item.split(',')
            li = []
            for line in a:
                if line != '\n' :
                    li.append(line)
                else:
                    break
             
            ma.append(li)
            
        return ma    
        
    def load_tiles(self, filename):
        back_tiles  = []
        back_tiles2 = []

        road_tiles = []
        road_tiles2 = []

        bend_tiles1 = []
        bend_tiles2 = []
        bend_tiles3 = []
        bend_tiles4 = []



        
        map1 = self.load_map(filename)
       # print(map1.count('1'))
        x, y = 930, -1260
        
        for row in map1:
            #print('quincy')
            x = 0
            #print(row)
            for tile in row:
                #print(tile, 'y')
                if tile == '1' :
                    road_tiles2.append(Tile( x, y, 'Road_Side2.png'))
                if tile == '2':
                    road_tiles.append(Tile( x, y,'Road_Main2.png'))
                #if tile == '3':
                 #   tiles.append(Tile( x, y, 'hardwareshop1f.png'))
                if tile == '4':
                    bend_tiles2.append(Tile(x, y, 'Road_01_Tile_02.png'))
                if tile == '5':
                    road_tiles.append(Tile( x, y, 'Road_Main.png'))
                if tile == '6':
                    back_tiles2.append(Tile( x, y, 'Bush_01.png'))
                if tile == '7':
                    bend_tiles3.append(Tile( x, y, 'Road_01_Tile_03.png'))
                if tile == '8':
                    bend_tiles1.append(Tile( x, y, 'Road_01_Tile_01.png'))
                if tile == '9':
                    bend_tiles4.append(Tile( x, y, 'Road_01_Tile_04.png'))
                    
                if tile == '10':
                    back_tiles.append(Tile( x, y, 'Grass_Tile2.png'))
                    #print('quincy')
                if tile == '11':
                    back_tiles2.append(Tile( x, y, 'Bush_02.png'))
                if tile == '12':
                    road_tiles2.append(Tile( x, y, 'Road_Side.png'))
                '''if tile == '13':
                    player = Player( x, y, 'green_car.png')
                    cars.add(player)'''
                        
                if tile != ',':
                    x += self.tile_size[0]
            y += self.tile_size[1]
        return back_tiles, back_tiles2 ,road_tiles, road_tiles2, bend_tiles1, bend_tiles2 ,bend_tiles3 ,bend_tiles4 #, player       

#maper = Tile_map('map1.txt')

all_tiles = pygame.sprite.Group()


back_tiles = pygame.sprite.Group()
back_tiles2 = pygame.sprite.Group()

road_tiles = pygame.sprite.Group()
road_tiles2 = pygame.sprite.Group()        

bend_tiles1 = pygame.sprite.Group()        
bend_tiles2 = pygame.sprite.Group()        
bend_tiles3 = pygame.sprite.Group()        
bend_tiles4 = pygame.sprite.Group()        

cars = pygame.sprite.Group()

tiler = Tile_map('map1b.txt')

#w = tiler.load_map('map1b.txt')
#print(w)



btiles = tiler.load_tiles('map1b.txt')
#print(type(btiles))

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
    
    
    

    


clock = pygame.time.Clock()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(colour)
    back_tiles.draw(screen)
   

    road_tiles.draw(screen)
    road_tiles2.draw(screen)

    bend_tiles1.draw(screen)
    bend_tiles2.draw(screen)
    bend_tiles3.draw(screen)
    bend_tiles4.draw(screen)
    
    # go ahead and update the screen with what we've drawn
    pygame.display.flip()
    clock.tick(60)



#w = maper.load_map('map1.txt')
#print(w)
