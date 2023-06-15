import pygame

class Walls(object):

    def __init__(self, g, x, y, tile):

        self.x = x
        self.y = y
        self.game = g
        self.tileSize = tile

        #wall
        self.image = pygame.Surface( (self.tileSize, self.tileSize) )
        self.image.fill( (255, 0, 0) )

        self.rect = self.image.get_rect()
        
        self.walls = []

    def add_wall(self, x, y):
        x = x * self.tileSize
        y = y * self.tileSize
        
        self.walls.append([x,y])

    def display_walls(self):

        for i in range(len(self.walls)):
            coords = self.walls[i]
            self.game.scene.blit( self.image , (coords[0],coords[1]) )

    def collided(self, x, y):
        x = x * self.tileSize
        y = y * self.tileSize
        result = False
        for i in range(len(self.walls)):
            coords = self.walls[i]
            if(x == coords[0] and y == coords[1]):
                result = True
                self.image.fill( (0,0,255) )

        return result
