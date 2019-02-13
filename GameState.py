#!/usr/bin/env python

import numpy as np
import re

#top left corner of matrix is (0,0)

class GameState():
    
    def __init__(self):
        #matrix for horiztontal walls
        self.h_walls = np.zeros( (9, 9) )
        #matrix for vertical walls
        self.v_walls = np.zeros( (9, 9) )
        #white pawn tuple
        self.player = (0,4)
        #black pawn tuple
        self.player2 = (8,4);

        #list of player walls (to keep track of how many walls left)
        '''
            Each player has a list of 10 wall matrices (all ones). When a wall
            is used, the matrice will be all zeros. When all the matrices are the
            zero matrice, the player may not use any more walls. They number of walls left
            are kept within self. Call getWallMatrices for matrix representation.
        '''
        self.numPlayerWalls = 10;
        self.numPlayer2Walls = 10;
        
    def getNumPlayerWalls(self):
        return self.numPlayerWalls;
    
    def getNumPlayer2Walls(self):
        return self.numPlayer2Walls;
    
    #output of 10 matrices. Matrices of all 1s mean they exist, Matrices of all 0s means they've been used.
    def getWallMatrices(self, player):
        result = [];
        if(player == 1):
            for i in range(10):
                if(i < self.numPlayerWalls):
                    result.append(np.ones((9,9)))
                else:
                    result.append(np.zeros((9,9)))
        elif(player == 2):
            for i in range(10):
                if(i < self.numPlayer2Walls):
                    result.append(np.ones((9,9)))
                else:
                    result.append(np.zeros((9,9)))
        return result

    def placePlayer(self, row, column):
        self.player = (row, column)
        
    def placePlayer2(self, row, column):
        self.player2 = (row, column)
        
    def getVerticalWallMatrix(self):
        return self.v_walls
    
    def getHorizontalWallMatrix(self):
        return self.h_walls
    
    def addPlayerWall(self, row, column, direction):
        if (row == 0 or column == 0):
            print("Invalid wall position.")
            return
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
        #if there is a wall to use, make it unuseable
        if(self.isPlayerWallsLeft()):
            self.numPlayerWalls = self.numPlayerWalls -1
            
    def addPlayer2Wall(self, row, column, direction):
        if (row == 0 or column == 0):
            print("Invalid wall position.")
            return
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
       #if there is a wall to use, make it unuseable
        if(self.isPlayer2WallsLeft()):
            self.numPlayer2Walls = self.numPlayer2Walls -1
            
    def isPlayerWallsLeft(self):
        if(self.numPlayerWalls > 0):
           return True
        return False
    
    def isPlayer2WallsLeft(self):
        if(self.numPlayer2Walls > 0):
           return True
        return False
    
    #returns numpy array of where the white pawn is located
    def getPlayerMatrix(self):
        white = np.zeros( (9, 9) )
        white[self.player[0]][self.player[1]] = 1
        return white;
    
    #returns numpy array of where the black pawn is located
    def getPlayer2Matrix(self):
        black = np.zeros( (9, 9) )
        black[self.player2[0]][self.player2[1]] = 1
        return black;

    #send in a round of moves (e.g. 1.e8 e2) 
    def makeMoves(self, move):
        moves = move.replace('.',' ').split()
        print(moves)
        self.findPlayerMove(moves[1])
        self.findPlayer2Move(moves[2])
            
    def findPlayerMove(self, playerMove):
        #if pawn move
        if(len(playerMove) == 2):
            if(playerMove[0] == 'a'):
                self.placePlayer(int(playerMove[1])-1, 0)
            elif(playerMove[0] == 'b'):
                self.placePlayer(int(playerMove[1])-1, 1)
            elif(playerMove[0] == 'c'):
                self.placePlayer(int(playerMove[1])-1, 2) 
            elif(playerMove[0] == 'd'):
                self.placePlayer(int(playerMove[1])-1, 3)
            elif(playerMove[0] == 'e'):
                self.placePlayer(int(playerMove[1])-1, 4)
            elif(playerMove[0] == 'f'):
                self.placePlayer(int(playerMove[1])-1, 5)
            elif(playerMove[0] == 'g'):
                self.placePlayer(int(playerMove[1])-1, 6)
            elif(playerMove[0] == 'h'):
                self.placePlayer(int(playerMove[1])-1, 7)
            elif(playerMove[0] == 'i'):
                self.placePlayer(int(playerMove[1])-1, 8)
        #if wall placement
        elif(len(playerMove) == 3):
            if(playerMove[0] == 'a'):
                self.addPlayerWall(int(playerMove[1])-1, 0, playerMove[2])
            if(playerMove[0] == 'b'):
                self.addPlayerWall(int(playerMove[1])-1, 1, playerMove[2])
            if(playerMove[0] == 'c'):
                self.addPlayerWall(int(playerMove[1])-1, 2, playerMove[2]) 
            if(playerMove[0] == 'd'):
                self.addPlayerWall(int(playerMove[1])-1, 3, playerMove[2])
            if(playerMove[0] == 'e'):
                self.addPlayerWall(int(playerMove[1])-1, 4, playerMove[2])
            if(playerMove[0] == 'f'):
                self.addPlayerWall(int(playerMove[1])-1, 5, playerMove[2])
            if(playerMove[0] == 'g'):
                self.addPlayerWall(int(playerMove[1])-1, 6, playerMove[2])
            if(playerMove[0] == 'h'):
                self.addPlayerWall(int(playerMove[1])-1, 7, playerMove[2])
            if(playerMove[0] == 'i'):
                self.addPlayerWall(int(playerMove[1])-1, 8, playerMove[2])
                
    def findPlayer2Move(self, playerMove):
        #if pawn move
        if(len(playerMove) == 2):
            if(playerMove[0] == 'a'):
                self.placePlayer2(int(playerMove[1])-1, 0)
            elif(playerMove[0] == 'b'):
                self.placePlayer2(int(playerMove[1])-1, 1)
            elif(playerMove[0] == 'c'):
                self.placePlayer2(int(playerMove[1])-1, 2) 
            elif(playerMove[0] == 'd'):
                self.placePlayer2(int(playerMove[1])-1, 3)
            elif(playerMove[0] == 'e'):
                self.placePlayer2(int(playerMove[1])-1, 4)
            elif(playerMove[0] == 'f'):
                self.placePlayer2(int(playerMove[1])-1, 5)
            elif(playerMove[0] == 'g'):
                self.placePlayer2(int(playerMove[1])-1, 6)
            elif(playerMove[0] == 'h'):
                self.placePlayer2(int(playerMove[1])-1, 7)
            elif(playerMove[0] == 'i'):
                self.placePlayer2(int(playerMove[1])-1, 8)
        #if wall placement
        elif(len(playerMove) == 3):
            if(playerMove[0] == 'a'):
                self.addPlayer2Wall(int(playerMove[1])-1, 0, playerMove[2])
            if(playerMove[0] == 'b'):
                self.addPlayer2Wall(int(playerMove[1])-1, 1, playerMove[2])
            if(playerMove[0] == 'c'):
                self.addPlayer2Wall(int(playerMove[1])-1, 2, playerMove[2]) 
            if(playerMove[0] == 'd'):
                self.addPlayer2Wall(int(playerMove[1])-1, 3, playerMove[2])
            if(playerMove[0] == 'e'):
                self.addPlayer2Wall(int(playerMove[1])-1, 4, playerMove[2])
            if(playerMove[0] == 'f'):
                self.addPlayer2Wall(int(playerMove[1])-1, 5, playerMove[2])
            if(playerMove[0] == 'g'):
                self.addPlayer2Wall(int(playerMove[1])-1, 6, playerMove[2])
            if(playerMove[0] == 'h'):
                self.addPlayer2Wall(int(playerMove[1])-1, 7, playerMove[2])
            if(playerMove[0] == 'i'):
                self.addPlayer2Wall(int(playerMove[1])-1, 8, playerMove[2])
    #needs to return a list of all the numpy arrays           
    def getAllMatrices(self):
        result = []
        result.append(self.getPlayerMatrix())
        result.append(self.getPlayer2Matrix())
        result.append(self.getVerticalWallMatrix())
        result.append(self.getHorizontalWallMatrix())
        return result
   
    def getGameState(self):
        result = np.array
        listOfMatrices = getAllMatrices(self)
        
        
    #needs to return a numpy array of 209 possible moves, marked by 1 meaning valid and 0 meaning invalid
    #def findValidMoves(self):
        
    '''
    #figure out how to categorize legal moves
    def isLegalMove(self):
        
    def getAsMatrices(self):
        
    def getValidMoves(self):
    '''
  
                
        
            
