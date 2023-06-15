import pygame

#import walls
from wall import Walls

class Player(object):

    def __init__(self, g, x,y):

        self.x = x
        self.y = y
        self.game = g

        self.tileSize =  g.tileSize
       
        self.image = pygame.Surface((self.tileSize, self.tileSize))
        self.image.fill( (0, 255, 0) )

        self.rect = self.image.get_rect()

        self.walls = Walls(g, x, y, g.tileSize)
        self.frog = pygame.image.load("assets/frog.png")

        self.icon = self.frog

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

    def controls(self, events):
        for event in events:
            #Quit
            if(event.type == pygame.QUIT):
                running = False
                pygame.quit()
                quit()

            #(4) Check for left and right buttons
            if(event.type == pygame.KEYDOWN):
                #print("A key has been pressed")
                ###
                x = 0
                y = 0
                wall = False
                wx = self.x
                wy = self.y
                ###
                if(event.key == pygame.K_LEFT):
                    self.icon = pygame.image.load("assets/frog_l.png")
                    x = -1
                    wall = True
                if(event.key == pygame.K_RIGHT):
                    self.icon = pygame.image.load("assets/frog_r.png")
                    x = 1
                    wall = True
                if(event.key == pygame.K_UP):
                    self.icon = pygame.image.load("assets/frog.png")
                    y = -1
                    wall = True
                if(event.key == pygame.K_DOWN):
                    self.icon = pygame.image.load("assets/frog_d.png")
                    y = 1
                    wall = True

                self.move( x , y )
                
                #if(wall):
                    #self.walls.add_wall(wx, wy)

    def update(self):
        #check controls for keypress
        self.controls(pygame.event.get())

        #adjust location
        self.rect.x = self.x * self.tileSize
        self.rect.y = self.y * self.tileSize

        #draw to the screen
        self.game.scene.blit( self.icon, (self.rect.x, self.rect.y) )

        #display any walls
        self.walls.display_walls()

        #check collision
        if(self.walls.collided(self.x, self.y)):
            self.image.fill( (0, 0, 255) )
        
        
