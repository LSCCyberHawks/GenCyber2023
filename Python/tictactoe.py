"""
Game: Tic Tac Toe
Author: Shawn Mitchell
Concept(s): Think like an Adversary

"""

import random

def displayBoard(boardState):
    #print top lines
    print("   | 1 | 2 | 3 |")
    print("-"*16)
    #initialize board spot variable
    spot = 0
    #for loop for each of the rows
    for row in range(3):
        #print left side bar
        print(" "+str(row+1)+" |", end="")
        for col in range(3):
            #if spot if empty, print a blank spot
            if(boardState[spot]==''):
                print('   |',end="")
            else:
                print(' '+boardState[spot]+' |', end="")

            spot += 1
        print('')
        print("-"*16)

def playerTurn(boardState, ply, letter):
    #row+col - 2 = spot
    while(True):
        if(ply != 1):
            column = int(input("Enter Column number > "))
            row    = int(input("Enter Row number > "))
        else:
            #random number for each
            column = random.randint(1,3)
            row    = random.randint(1,3)
            
        if((row < 4) and (row > 0) and (column < 4) and (column > 0)):
            
            if(row == 1):
                rowv = -1
            elif(row == 2):
                rowv = 2
            elif(row == 3):
                rowv = 5

            if(boardState[rowv+column] == ''):
                boardState[rowv+column] = letter
                return (not gameOver(boardState))
            else:
                if(ply != 1):
                    print('Spot Taken, Try again')
        else:
            print("Invalid coordinate, try again")
        
    displayBoard(boardState)

def gameOver(boardState):
    #define gameDone
    gameDone = True
    win = "?"
    #check board for full
    for count in range(len(boardState)):
        if(boardState[count]==''):
            gameDone = False
    #check board for win
    if(not gameDone):
        #check rows
        for count in range(3):
            if(boardState[count*3]==boardState[count*3+1]==boardState[count*3+2] and boardState[count*3] != ''):
                gameDone = True
                win = boardState[count*3]
        #check columns
        for count in range(3):
            if(boardState[count]==boardState[count+3]==boardState[count+6] and boardState[count] != ''):
                gameDone = True
                win = boardState[count]
        #check diagonals
        if(boardState[0]==boardState[4]==boardState[8] and boardState[4] != ''):
            gameDone = True
            win = boardState[4]
        if(boardState[2]==boardState[4]==boardState[6] and boardState[4] != ''):
            gameDone = True
            win = boardState[4]
    if(gameDone):
        if(win == "?"):
            print("Game ends in stalemate!")
        else:
            print("Winner is : "+win)
            
    return gameDone
    
def main():
    #Board consists of 9 squares. Create a dictionary containing the starting
    #values of all spaces (empty strings)
    boardState = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''}
    #variable playGame will be checked after the end of every turn (player and computer!)
    playGame = True

    numPlayers = int(input("How many human players? [1-2] > "))
    
    while(playGame):
        #display board at beginning of turn
        displayBoard(boardState)
        #player turn set to playGame
        playGame = playerTurn(boardState,0,'X')            
        #if player did not win, game should still be played
        if(playGame):
            #computers or player turn turn now. numPlayers 1 = comp 2 = play2
            playGame = playerTurn(boardState, numPlayers,'O')
    displayBoard(boardState)
    print("Game Over")
     
main()
