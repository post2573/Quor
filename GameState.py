#!/usr/bin/env python

import numpy as np

#top left corner of matrix is (0,0)

class GameState():
    
    def __init__(self):
        #matrix for horiztontal walls
        self.h_walls = np.zeros( (9, 9) )
        #matrix for vertical walls
        self.v_walls = np.zeros( (9, 9) )
        #matrix for white pawn
        self.player = np.zeros( (9, 9) )
        self.player[0][4] = 1
        #matrix for black pawn
        self.player2 = np.zeros( (9, 9) )
        self.player2[8][4] = 1
        #list of player walls (to keep track of how many walls left)
        '''
            Each player has a list of 10 wall matrices (all ones). When a wall
            is used, the matrice will be all zeros. When all the matrices are the
            zero matrice, the player may not use any more walls.
        '''
        self.playerwalls = [np.ones((9,9)) for i in range(10)]
        self.player2walls = [np.ones((9,9)) for i in range(10)]

    def placePlayer(self, row, column):
        self.player = np.zeros((9,9))
        self.player[row][column] = 1
    def placePlayer2(self, row, column):
        self.player2 = np.zeros((9,9))
        self.player2[row][column] = 1
    def addPlayerWall(self, row, column, direction):
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
        for wall in self.playerwalls:
            #if there is a wall to use, make it unuseable
            if(np.count_nonzero(self.playerwalls[wall]) > 0):
                self.playerwalls[wall] = np.zeros((9,9))
    def addPlayer2Wall(self, row, column, direction):
        if (direction == 'v'):
            self.v_walls[row][column] = 1
        if (direction == 'h'):
            self.h_walls[row][column] = 1
        for wall in self.playerwalls:
            #if there is a wall to use, make it unuseable
            if(np.count_nonzero(self.player2walls[wall]) > 0):
                self.player2walls[wall] = np.zeros((9,9))
    def isPlayerWallsLeft(self):
        for wall in self.playerwalls:
            if(np.count_nonzero(self.playerwalls[wall]) > 0):
                return true
        return false
    def isPlayer2WallsLeft(self):
        for wall in self.player2walls:
            if(np.count_nonzero(self.player2walls[wall]) > 0):
                return true
        return false
    #figure out how to categorize legal moves
    def isLegalMove(self):
        
          
                
        
            
