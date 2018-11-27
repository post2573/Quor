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
        
        def placePlayer(self, row, column):
            self.player = np.zeros((9,9))
            self.player[row][column] = 1
        def placePlayer2(self, row, column):
            self.player2 = np.zeros((9,9))
            self.player2[row][column] = 1
