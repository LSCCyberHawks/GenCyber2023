import pygame

from player import Player

class GameScreen(object):

    def __init__(self, w, h, tilesize):
        pygame.init()

        #initialize all screen variables

        self.width  = w
        self.height = h
        self.scene   = pygame.display.set_mode( (w,h) )
        self.caption = pygame.display.set_caption("This is Game Title")
        self.icon    = pygame.image.load("assets/icon.png")
        #actually displays the icon
        pygame.display.set_icon(self.icon)

        #tilesize setup
        self.tileSize = tilesize
        self.gridColor = (130,98,22)

        # any game sound here. 
        self.track   = pygame.mixer.music.load("assets/levelMusic.wav")
        self.m_loop  = pygame.mixer.music.play(-1)
        self.m_volum = pygame.mixer.music.set_volume(0)

        # also include background image

        self.bgc     = (51,51,51)

        #define player
        self.player =  Player(self, 5, 8)

        self.water = pygame.image.load("assets/water.png")
        self.grass = pygame.image.load("assets/grass.png")
        self.street = pygame.image.load("assets/road.png")
        self.CL    = pygame.image.load("assets/car_l.png")
        self.CR    = pygame.image.load("assets/car_r.png")
        self.LL    = pygame.image.load("assets/log_l.png")
        self.LM    = pygame.image.load("assets/log_m.png")
        self.LR    = pygame.image.load("assets/log_r.png")

        #roads
        self.roads = []
        self.roads.append(["","","CL","CR","","","","CL","CR",""])
        self.roads.append(["CR","","","","","","","","","CL"])
        self.roads.append(["","","","","","","CL","CR","",""])
        self.roads.append(["CL","CR","","","","","","","",""])
        self.roads.append(["","","CL","CR","","","","CL","CR",""])

        #logs
        self.logs = []
        self.logs.append(["LL","LM","LR","","","","","","",""])
        self.logs.append(["LR","","","","","","","","","LL"])
        self.logs.append(["","","LL","LM","LR","","","","",""])
        self.logs.append(["","LL","LR","","","","","LL","LR",""])
        self.logs.append(["","","","","LL","LM","LR","","",""])
        #self.object = ()

        self.clock = pygame.time.Clock()
        #self.timer = pygame.time.get_ticks()

        self.elapsedTime = 0

    def draw_grid(self):
        for x in range(0, self.width, self.tileSize):
            pygame.draw.line(self.scene, self.gridColor, (x, 0), (x, self.height) )
        for y in range(0, self.height, self.tileSize):
            pygame.draw.line(self.scene, self.gridColor, (0, y), (self.width, y) )
        
    def setBackground(self):
        self.scene.fill(self.bgc)
        self.draw_grid()

    def display_board(self):

        for i in range(10):
            coords = [i * self.tileSize, 0 * self.tileSize ]
            self.scene.blit(self.grass, ( coords[0] , coords[1] ) )

        for i in range(1,6):
            for u in range(10):
                coords = [u * self.tileSize, i * self.tileSize ]
                self.scene.blit(self.water, (coords[0], coords[1] ) )

        for i in range(10):
            coords = [i * self.tileSize, 6 * self.tileSize ]
            self.scene.blit(self.grass, ( coords[0] , coords[1] ) ) 

        for i in range(7,12):
            for u in range(10):
                coords = [u * self.tileSize, i * self.tileSize ]
                self.scene.blit(self.street, (coords[0], coords[1] ) )

        for i in range(10):
            coords = [i * self.tileSize, 12 * self.tileSize ]
            self.scene.blit(self.grass, ( coords[0] , coords[1] ) ) 

    def advance_rows(self):
        for i in range(len(self.roads)):
            row = self.roads[i]
            end = row.pop()
            row.insert(0, end)
            self.roads[i] = row
        for i in range(len(self.logs)):
            row = self.logs[i]
            end = row.pop()
            row.insert(0, end)
            self.logs[i] = row

    def display_objects(self):
        for i in range(len(self.roads)):
            row = self.roads[i]
            for u in range(len(row)):
                if(row[u] != ''):
                    if(row[u] == "CL"):
                        #print('-')
                        self.scene.blit(self.CL, (u * self.tileSize, (i+7) * self.tileSize) )
                    if(row[u] == "CR"):
                        #print('()')
                        self.scene.blit(self.CR, (u * self.tileSize, (i+7) * self.tileSize) )

        for i in range(len(self.logs)):
            row = self.logs[i]
            for u in range(len(row)):
                if(row[u] != ''):
                    if(row[u] == "LL"):
                        #print('-')
                        self.scene.blit(self.LL, (u * self.tileSize, (i+1) * self.tileSize) )
                    if(row[u] == "LM"):
                        #print('()')
                        self.scene.blit(self.LM, (u * self.tileSize, (i+1) * self.tileSize) )
                    if(row[u] == "LR"):
                        #print('()')
                        self.scene.blit(self.LR, (u * self.tileSize, (i+1) * self.tileSize) )


        
    def update(self):
        keepGoing = True

        self.setBackground()
        self.display_board()
        #self.draw_grid()

        dt = self.clock.tick()
        self.elapsedTime += dt

        if(self.elapsedTime > 1000):
            self.elapsedTime = 0
            self.advance_rows()
            
        self.display_objects()
        self.player.update()
        
        pygame.display.update()

        return keepGoing
