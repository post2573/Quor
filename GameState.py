#!/usr/bin/env python

import numpy as np
import re

#top left corner of matrix is (0,0)

class GameState():
    
    def __init__(self):
        #matrix for horiztontal walls
        self.h_walls = np.zeros( (9, 9), dtype=int )
        #matrix for vertical walls
        self.v_walls = np.zeros( (9, 9), dtype=int )
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
        result = []
        if(player == 1):
            for i in range(10):
                if(i < self.numPlayerWalls):
                    wall = np.ones((9,9), dtype=int)
                    #put 0s where invalid wall placement
                    for j in range(9):
                        wall[0][j] = 0;
                        wall[j][0] = 0;
                    result.append(wall)
                else:
                    result.append(np.zeros((9,9), dtype=int))
        elif(player == 2):
            for i in range(10):
                if(i < self.numPlayer2Walls):
                    wall = np.ones((9,9), dtype=int)
                    #put 0s where invalid wall placement
                    for j in range(9):
                        wall[0][j] = 0;
                        wall[j][0] = 0;
                    result.append(wall)
                else:
                    result.append(np.zeros((9,9), dtype=int))
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
        white = np.zeros( (9, 9), dtype=int )
        white[self.player[0]][self.player[1]] = 1
        return white;
    
    #returns numpy array of where the black pawn is located
    def getPlayer2Matrix(self):
        black = np.zeros( (9, 9), dtype=int )
        black[self.player2[0]][self.player2[1]] = 1
        return black;

    #send in a round of moves (e.g. 1.e8 e2) 
    def makeMoves(self, move):
        moves = move.replace('.',' ').split()
        print(moves)
        self.findPlayerMove(moves[1])
        self.findPlayer2Move(moves[2])
            
    def findPlayerMove(self, playerMove):
        moveMap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        #if pawn move
        if(len(playerMove) == 2):
            self.placePlayer(int(playerMove[1])-1, moveMap[playerMove[0]])
        #if wall placement
        elif(len(playerMove) == 3):
            self.addPlayerWall(int(playerMove[1])-1, moveMap[playerMove[0]], playerMove[2])
           
    def findPlayer2Move(self, playerMove):
        moveMap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        #if pawn move
        if(len(playerMove) == 2):
             self.placePlayer2(int(playerMove[1])-1, moveMap[playerMove[0]])
        #if wall placement
        elif(len(playerMove) == 3):
            self.addPlayer2Wall(int(playerMove[1])-1, moveMap[playerMove[0]], playerMove[2])
            
    #needs to return a list of all the numpy arrays           
    def getAllMatrices(self):
        result = []
        result.append(self.getPlayerMatrix())
        result.append(self.getPlayer2Matrix())
        result.append(self.getVerticalWallMatrix())
        result.append(self.getHorizontalWallMatrix())
        result.append(self.getWallMatrices(1))
        result.append(self.getWallMatrices(2))
        return result
   '''
    def getGameState(self):
        result = np.array
        listOfMatrices = getAllMatrices(self)
   '''     
        
    def shiftdown9x9(self, mat):
        return np.append(np.zeros((1,9), dtype=int), mat[0:8,:], 0)

    def shiftup9x9(self, mat):
        return np.append(mat[1:,:], np.zeros((1,9), dtype=int), 0)

    def shiftleft9x9(self, mat):
        return np.append(mat[:,1:], np.zeros((9,1), dtype=int), 1)

    def shiftright9x9(self, mat):
        return np.append(np.zeros((9,1), dtype=int), mat[:, 0:8], 1)

    def bfs(self, starting, h_walls, v_walls):
        curr_state = np.copy(starting)==1
        while (True):
            canGoUp = np.logical_not(np.logical_or(h_walls, self.shiftleft9x9(h_walls)))
            canGoDown = np.logical_not(np.logical_or(self.shiftup9x9(h_walls), self.shiftup9x9(self.shiftleft9x9(h_walls))))
            canGoLeft = np.logical_not(np.logical_or(v_walls, self.shiftup9x9(v_walls)))
            canGoRight = np.logical_not(np.logical_or(self.shiftleft9x9(v_walls), self.shiftleft9x9(self.shiftup9x9(v_walls))))
            next_state = np.copy(curr_state)
            #update up
            next_state = np.logical_or(next_state, self.shiftup9x9(np.logical_and(canGoUp, curr_state)))
            #update down
            next_state = np.logical_or(next_state, self.shiftdown9x9(np.logical_and(canGoDown, curr_state)))
            #update left
            next_state = np.logical_or(next_state, self.shiftleft9x9(np.logical_and(canGoLeft, curr_state)))
            #update right
            next_state = np.logical_or(next_state, self.shiftright9x9(np.logical_and(canGoRight, curr_state)))

            print("next state is ")
            print(next_state)
            if (np.array_equal(next_state, curr_state)):
                return next_state*1
            curr_state = next_state

        
    #needs to return a numpy array of 209 possible moves, marked by 1 meaning valid and 0 meaning invalid
    #def findValidMoves(self):
        
    '''
    #figure out how to categorize legal moves
    def isLegalMove(self):
        
    def getAsMatrices(self):
        
    def getValidMoves(self):
    '''
  
                
        
            
