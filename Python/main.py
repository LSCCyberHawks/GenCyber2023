import pygame

from gamescreen import GameScreen

def main():
    height = 416#608
    width  = 320
    tile   = 32
    g      = GameScreen(width, height, tile)


    play = True
    intro = False    
    game = True
    scores = False

    while(play):
        #while(intro):
        #    intro = introloop(i)
        
        while(game):
            
           game = gameloop(g)

        #while(scores):
        #    scores = scoreloop(s)

        #play = 

def gameloop(g):

    keepGoing = g.update()

    return keepGoing

main()
