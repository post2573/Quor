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
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
        #if there is a wall to use, make it unuseable
        if(isPlayerWallsLeft(self)):
            self.numPlayerWalls = self.numPlayerWalls -1
            
    def addPlayer2Wall(self, row, column, direction):
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
       #if there is a wall to use, make it unuseable
        if(isPlayer2WallsLeft(self)):
            self.numPlayer2Walls = self.numPlayer2Walls -1
            
    def isPlayerWallsLeft(self):
        if(self.numPlayerWalls > 0):
           return true
        return false
    
    def isPlayer2WallsLeft(self):
        if(self.numPlayer2Walls > 0):
           return true
        return false
    
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
        moves = re.split(" .", move)
        findPlayerMove(self, moves[1])
        findPlayer2Move(self, moves[2])
            
    def findPlayerMove(self, playerMove):
        #if pawn move
        if(len(playerMove) == 2):
            if(playerMove[0] == 'a'):
                placePlayer(self, playerMove[1], 0)
            if(playerMove[0] == 'b'):
                placePlayer(self, playerMove[1], 1)
            if(playerMove[0] == 'c'):
                placePlayer(self, playerMove[1], 2) 
            if(playerMove[0] == 'd'):
                placePlayer(self, playerMove[1], 3)
            if(playerMove[0] == 'e'):
                placePlayer(self, playerMove[1], 4)
            if(playerMove[0] == 'f'):
                placePlayer(self, playerMove[1], 5)
            if(playerMove[0] == 'g'):
                placePlayer(self, playerMove[1], 6)
            if(playerMove[0] == 'h'):
                placePlayer(self, playerMove[1], 7)
            if(playerMove[0] == 'i'):
                placePlayer(self, playerMove[1], 8)
        #if wall placement
        elif(len(playerMove) == 3):
            if(playerMove[0] == 'a'):
                addPlayerWall(self, playerMove[1], 0, playerMove[2])
            if(playerMove[0] == 'b'):
                addPlayerWall(self, playerMove[1], 1, playerMove[2])
            if(playerMove[0] == 'c'):
                addPlayerWall(self, playerMove[1], 2, playerMove[2]) 
            if(playerMove[0] == 'd'):
                addPlayerWall(self, playerMove[1], 3, playerMove[2])
            if(playerMove[0] == 'e'):
                addPlayerWall(self, playerMove[1], 4, playerMove[2])
            if(playerMove[0] == 'f'):
                addPlayerWall(self, playerMove[1], 5, playerMove[2])
            if(playerMove[0] == 'g'):
                addPlayerWall(self, playerMove[1], 6, playerMove[2])
            if(playerMove[0] == 'h'):
                addPlayerWall(self, playerMove[1], 7, playerMove[2])
            if(playerMove[0] == 'i'):
                addPlayerWall(self, playerMove[1], 8, playerMove[2])
                
    def findPlayer2Move(self, playerMove):
        #if pawn move
        if(len(playerMove) == 2):
            if(playerMove[0] == 'a'):
                placePlayer2(self, playerMove[1], 0)
            if(playerMove[0] == 'b'):
                placePlayer2(self, playerMove[1], 1)
            if(playerMove[0] == 'c'):
                placePlayer2(self, playerMove[1], 2) 
            if(playerMove[0] == 'd'):
                placePlayer2(self, playerMove[1], 3)
            if(playerMove[0] == 'e'):
                placePlayer2(self, playerMove[1], 4)
            if(playerMove[0] == 'f'):
                placePlayer2(self, playerMove[1], 5)
            if(playerMove[0] == 'g'):
                placePlayer2(self, playerMove[1], 6)
            if(playerMove[0] == 'h'):
                placePlayer2(self, playerMove[1], 7)
            if(playerMove[0] == 'i'):
                placePlayer2(self, playerMove[1], 8)
        #if wall placement
        elif(len(playerMove) == 3):
            if(playerMove[0] == 'a'):
                addPlayer2Wall(self, playerMove[1], 0, playerMove[2])
            if(playerMove[0] == 'b'):
                addPlayer2Wall(self, playerMove[1], 1, playerMove[2])
            if(playerMove[0] == 'c'):
                addPlayer2Wall(self, playerMove[1], 2, playerMove[2]) 
            if(playerMove[0] == 'd'):
                addPlayer2Wall(self, playerMove[1], 3, playerMove[2])
            if(playerMove[0] == 'e'):
                addPlayer2Wall(self, playerMove[1], 4, playerMove[2])
            if(playerMove[0] == 'f'):
                addPlayer2Wall(self, playerMove[1], 5, playerMove[2])
            if(playerMove[0] == 'g'):
                addPlayer2Wall(self, playerMove[1], 6, playerMove[2])
            if(playerMove[0] == 'h'):
                addPlayer2Wall(self, playerMove[1], 7, playerMove[2])
            if(playerMove[0] == 'i'):
                addPlayer2Wall(self, playerMove[1], 8, playerMove[2])
                
    #needs to return a list of all the numpy arrays           
    def getAllMatrices(self):
        result = []
        result.append(self.getPlayerMatrix(self))
        result.append(self.getPlayer2Matrix(self))
        result.append(self.getVerticalWallMatrix(self))
        result.append(self.getHorizontalWallMatrix(self))
        
        
    #needs to return a numpy array of 209 possible moves, marked by 1 meaning valid and 0 meaning invalid
    #def findValidMoves(self):
        
    '''
    #figure out how to categorize legal moves
    def isLegalMove(self):
        
    def getAsMatrices(self):
        
    def getValidMoves(self):
    '''
  
                
        
            
