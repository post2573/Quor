#!/usr/bin/env python

import numpy as np
import re

#top left corner of matrix is (0,0)

class GameState():
    
    def __init__(self, n=9):
        #matrix for horiztontal walls
        self.h_walls = np.zeros( (9, 9), dtype=int )
        #matrix for vertical walls
        self.v_walls = np.zeros( (9, 9), dtype=int )
        #white pawn tuple
        self.player = (8,4)
        #black pawn tuple
        self.player2 = (0,4)
        self.n = n
        self.numPlayerWalls = 10
        self.numPlayer2Walls = 10
       
    def getBoardSize(self):
        return (self.n, self.n)
   
    def seeV_WallsFlipped(self, vertWalls):
        #rotate the existing matrix and shift to the right and then down
        rot = np.rot90(vertWalls, 2)
        #y = np.argwhere(rot==1)
        #print(y)
        rot = self.shiftright9x9(rot)
        rot = self.shiftdown9x9(rot)
        return rot
    
    def seeH_WallsFlipped(self,horizWalls):
        #rotate the existing matrix and shift to the right and then down
        rot = np.rot90(horizWalls, 2)
        #y = np.argwhere(rot==1)
        #print(y)
        rot = self.shiftright9x9(rot)
        rot = self.shiftdown9x9(rot)
        return rot
    
    def getNumPlayerWalls(self):
        return self.numPlayerWalls
    
    def getNumPlayer2Walls(self):
        return self.numPlayer2Walls
    
    #output of 10 matrices. Matrices of all 1s mean they exist, Matrices of all 0s means they've been used.
    def getWallMatrices(self, player):
        result = []
        if(player == 1):
            for i in range(10):
                if(i < self.numPlayerWalls):
                    wall = np.ones((9,9), dtype=int)
                    #put 0s where invalid wall placement
                    for j in range(9):
                        wall[0][j] = 0
                        wall[j][0] = 0
                    result.append(wall)
                else:
                    result.append(np.zeros((9,9), dtype=int))
        elif(player == 2):
            for i in range(10):
                if(i < self.numPlayer2Walls):
                    wall = np.ones((9,9), dtype=int)
                    #put 0s where invalid wall placement
                    for j in range(9):
                        wall[0][j] = 0
                        wall[j][0] = 0
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
        #NEED TO CHECK WHETHER WALL PLACEMENT IS VALID 
            #NO OVERLAPPING WALLS AND NO TRAPPING THE OTHER PLAYER COMPLETELY
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
        return white
    
    #returns numpy array of where the black pawn is located
    def getPlayer2Matrix(self):
        black = np.zeros( (9, 9), dtype=int )
        black[self.player2[0]][self.player2[1]] = 1
        return black

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
            
    def isValidMove(self, playerMove, validMoves):
        moveMap = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        if(validMoves[int(playerMove[1])-1][moveMap[playerMove[0]]] == 1):
            return True
        return False
    
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

            #print("next state is ")
            #print(next_state)
            if (np.array_equal(next_state, curr_state)):
                return next_state*1
            curr_state = next_state

        
    def canGoNorth(self, coord, players, h_walls, v_walls):
        self.canGoUpGivenWalls = np.logical_not(np.logical_or(h_walls, self.shiftleft9x9(h_walls)))
        # players is matrix with 1s where players are 
        (i,j) = coord #parse coordinate into two parts
        if (i<=0):
            # already at top of board
            return False

        #i > 0
        if (players[i-1,j]==0 and self.canGoUpGivenWalls[i,j]):
            return True
        else:
            return False


    def canGoSouth(self, coord, players, h_walls, v_walls):
        canGoDownGivenWalls = np.logical_not(np.logical_or(self.shiftup9x9(h_walls), self.shiftup9x9(self.shiftleft9x9(h_walls))))
        (i,j) = coord
        if (i>=8):
            # already at bottom
            return False
        # i < 8
        if (players[i+1, j]==0 and canGoDownGivenWalls[i,j]):
            return True
        else:
            return False


    def canGoWest(self, coord, players, h_walls, v_walls):
        canGoLeftGivenWalls = np.logical_not(np.logical_or(v_walls, self.shiftup9x9(v_walls)))
        (i,j) = coord
        if (j<=0):
            # already at left edge
            return False
        if (players[i,j-1]==0 and canGoLeftGivenWalls[i,j]):
            return True
        else:
            return False



    def canGoEast(self, coord, players, h_walls, v_walls):
        canGoRightGivenWalls = np.logical_not(np.logical_or(self.shiftleft9x9(v_walls), self.shiftleft9x9(self.shiftup9x9(v_walls))))
        (i,j) = coord
        if (j>=8):
            # already at right edge
            return False
        if (players[i, j+1]==0 and canGoRightGivenWalls[i,j]):
            return True
        else:
            return False





    # can go two spots north in one turn
    # only allowed if pawn to north and open one spot beyond 
    def canGoNorthNorth(self, coord, players, h_walls, v_walls):
        (i,j) = coord
        if (i<=1):
            # too close to top edge
            return False
        if (players[i-1, j]==1 and self.canGoNorth((i-1,j), players, h_walls, v_walls)):
            return True
        else:
            return False

    def canGoSouthSouth(self, coord, players, h_walls, v_walls):
        (i,j) = coord
        if (i>=7):
            # too close to bottom
            return False
        if (players[i+1, j]==1 and self.canGoSouth((i+1,j), players, h_walls, v_walls)):
            return True
        else:
            return False

    def canGoWestWest(self, coord, players, h_walls, v_walls):
        (i,j) = coord
        if (j<=1):
            # too close to left
            return False
        if (players[i, j-1]==1 and self.canGoWest((i,j-1), players, h_walls, v_walls)):
            return True
        else:
            return False   

    def canGoEastEast(self, coord, players, h_walls, v_walls):
        (i,j) = coord
        if (j>=7):
            # too close to right
            return False
        if (players[i, j+1]==1 and self.canGoEast((i,j+1), players, h_walls, v_walls)):
            return True
        else:
            return False 



    # only allowed if pawn above with wall above it, or pawn left with walls left of it
    # this code assume a two player game
    def canGoNorthWest(self, coord, players, h_walls, v_walls):
        canGoLeftGivenWalls = np.logical_not(np.logical_or(v_walls, self.shiftup9x9(v_walls)))
        canGoUpGivenWalls = np.logical_not(np.logical_or(h_walls, self.shiftleft9x9(h_walls)))
        (i,j) = coord

        if (i<=0 or j<=0):
            # already at top and/or left edge
            return False
        # if pawn above, cannot go NorthNorth due to walls, and pawn above can go west, then true
        if (players[i-1,j]==1 and not canGoUpGivenWalls[i-1,j] and self.canGoWest((i-1,j), players, h_walls, v_walls)):
            return True
        # if pawn left, cannot go westwest due to walls, and pawn left can go north, then true
        if (players[i, j-1]==1 and not canGoLeftGivenWalls[i,j-1] and self.canGoNorth((i, j-1), players, h_walls, v_walls)):
            return True
        # anything else is bad
        return False

    def canGoNorthEast(self, coord, players, h_walls, v_walls):

        canGoUpGivenWalls = np.logical_not(np.logical_or(h_walls, self.shiftleft9x9(h_walls)))
        canGoRightGivenWalls = np.logical_not(np.logical_or(self.shiftleft9x9(v_walls), self.shiftleft9x9(self.shiftup9x9(v_walls))))
        (i,j) = coord
        if (i<=0 or j>=8):
            # already at top and/or right edge
            return False
        # if pawn above, cannot go NorthNorth, and pawn above can go east, then true
        if (players[i-1,j]==1 and not canGoUpGivenWalls[i-1,j] and canGoEast((i-1,j), players, h_walls, v_walls)):
            return True
        # if pawn right, cannot go easteast, and pawn right can go north, then true
        if (players[i, j+1]==1 and not canGoRightGivenWalls[i,j+1] and canGoNorth((i, j+1), players, h_walls, v_walls)):
            return True
        # anything else is bad
        return False


    def canGoSouthEast(self, coord, players, h_walls, v_walls):
        canGoRightGivenWalls = np.logical_not(np.logical_or(self.shiftleft9x9(v_walls), self.shiftleft9x9(self.shiftup9x9(v_walls))))
        canGoDownGivenWalls = np.logical_not(np.logical_or(self.shiftup9x9(h_walls), self.shiftup9x9(self.shiftleft9x9(h_walls))))
        (i,j) = coord

        if (i>=8 or j>=8):
            # already at bottom and/or right edge
            return False
        # if pawn below, cannot go southsouth, and pawn below can go east, then true
        if (players[i+1,j]==1 and not canGoDownGivenWalls[i+1,j] and canGoEast((i+1,j), players, h_walls, v_walls)):
            return True
        # if pawn right, cannot go easteast, and pawn right can go south, then true
        if (players[i, j+1]==1 and not canGoRightGivenWalls[i,j+1] and canGoSouth((i, j+1), players, h_walls, v_walls)):
            return True
        # anything else is bad
        return False

    def canGoSouthWest(self, coord, players, h_walls, v_walls):
        canGoDownGivenWalls = np.logical_not(np.logical_or(self.shiftup9x9(h_walls), self.shiftup9x9(self.shiftleft9x9(h_walls))))
        canGoLeftGivenWalls = np.logical_not(np.logical_or(v_walls, self.shiftup9x9(v_walls)))
        (i,j) = coord

        if (i>=8 or j<=0):
            # already at bottom and/or left edge
            return False
        # if pawn below, cannot go southsouth, and pawn below can go west, then true
        if (players[i+1,j]==1 and not canGoDownGivenWalls[i+1,j] and self.canGoWest((i+1,j), players, h_walls, v_walls)):
            return True
        # if pawn left, cannot go westwest, and pawn left can go south, then true
        if (players[i, j-1]==1 and not canGoLeftGivenWalls[i,j-1] and self.canGoSouth((i, j-1), players, h_walls, v_walls)):
            return True
        # anything else is bad
        return False 
        
    # new code as of 2/24/19 below
    
 
    def canWinNorth(self, player, h_walls, v_walls):
        player_mat = np.zeros((9,9), dtype=int)
        (i,j)=player
        player_mat[i,j] = 1
        reachability = self.bfs(player_mat, h_walls, v_walls)
        return np.any(reachability[0, :])

    def canWinSouth(self, player, h_walls, v_walls):
        player_mat = np.zeros((9,9), dtype=int)
        (i,j)=player
        player_mat[i,j] = 1
        reachability = self.bfs(player_mat, h_walls, v_walls)
        return np.any(reachability[8, :])
    
    def hasNorthPlayerWon(self, north_player):
        return np.any(north_player[0,:])
                      
    def hasSouthPlayerWon(self, south_player):
        return np.any(south_player[8,:])

    def generateValidNorthPawnMoves(self, north_player, south_player, h_walls, v_walls):
        valid_moves = np.zeros((9,9), dtype=int)
        players = np.zeros((9,9), dtype=int)
        (ni,nj) = north_player
        (si,sj) = south_player
        players[ni,nj] = 1
        players[si,sj] = 1
        if (self.canGoNorth(north_player,players,h_walls,v_walls)):
            valid_moves[ni-1,nj] = 1
        if (self.canGoSouth(north_player,players,h_walls,v_walls)):
            valid_moves[ni+1,nj] = 1
        if (self.canGoWest(north_player,players,h_walls,v_walls)):
            valid_moves[ni,nj-1] = 1
        if (self.canGoEast(north_player,players,h_walls,v_walls)):
            valid_moves[ni,nj+1] = 1
        if (self.canGoNorthWest(north_player,players,h_walls,v_walls)):
            valid_moves[ni-1,nj-1] = 1
        if (self.canGoNorthEast(north_player,players,h_walls,v_walls)):
            valid_moves[ni-1,nj+1] = 1
        if (self.canGoSouthWest(north_player,players,h_walls,v_walls)):
            valid_moves[ni+1,nj-1] = 1
        if (self.canGoSouthEast(north_player,players,h_walls,v_walls)):
            valid_moves[ni+1,nj+1] = 1
        if (self.canGoNorthNorth(north_player,players,h_walls,v_walls)):
            valid_moves[ni-2,nj] = 1
        if (self.canGoSouthSouth(north_player,players,h_walls,v_walls)):
            valid_moves[ni+2,nj] = 1
        if (self.canGoWestWest(north_player,players,h_walls,v_walls)):
            valid_moves[ni,nj-2] = 1
        if (self.canGoEastEast(north_player,players,h_walls,v_walls)):
            valid_moves[ni,nj+2] = 1
        return valid_moves 

    def generateValidVertWalls(self, north_player, south_player, h_walls, v_walls):
        valid_vwalls = np.zeros((9,9), dtype=int)
        for i in range(9):
            for j in range(9):
                valid_vwalls[i,j]= self.canPlaceVertWall(i,j,north_player,south_player,h_walls,v_walls)
        return valid_vwalls

    def generateValidHorizWalls(self, north_player, south_player, h_walls, v_walls):
        valid_hwalls = np.zeros((9,9), dtype=int)
        for i in range(9):
            for j in range(9):
                valid_hwalls[i,j]= self.canPlaceHorizWall(i,j,north_player,south_player,h_walls,v_walls)
        return valid_hwalls


    def canPlaceVertWall(self, i, j, north_player, south_player, h_walls, v_walls):
        if (j==0):
            # left edge of board
            return False
        if (h_walls[i,j]==1 or v_walls[i,j]==1):
            # already wall there
            return False
        if (i==0):
            # top edge
            return False
        if (v_walls[i-1,j]==1):
            return False
        if (i<8 and v_walls[i+1,j]==1):
            return False
        v_wall_copy = np.copy(v_walls)
        v_wall_copy[i,j] = 1
        if (not self.canWinNorth(north_player, h_walls, v_wall_copy)):
            return False
        if (not self.canWinSouth(south_player, h_walls, v_wall_copy)):
            return False
        return True 

    def canPlaceHorizWall(self, i, j, north_player, south_player, h_walls, v_walls):
        if (j==0):
            # left edge of board
            return False
        if (h_walls[i,j]==1 or v_walls[i,j]==1):
            # already wall there
            return False
        if (i==0):
            # top edge
            return False
        if (h_walls[i,j-1]==1):
            return False
        if (j<8 and h_walls[i,j+1]==1):
            return False
        h_wall_copy = np.copy(h_walls)
        h_wall_copy[i,j] = 1
        if (not self.canWinNorth(north_player, h_wall_copy, v_walls)):
            return False
        if (not self.canWinSouth(south_player, h_wall_copy, v_walls)):
            return False
        return True 


    def generateValidMoveVector(self, north_player, south_player, h_walls, v_walls):
        pawnMoveMat = self.generateValidNorthPawnMoves(north_player, south_player, h_walls, v_walls)
        possibleHorizWallMat = self.generateValidHorizWalls(north_player, south_player, h_walls, v_walls)
        possibleVertWallMat = self.generateValidVertWalls(north_player, south_player, h_walls, v_walls)
        return np.concatenate((pawnMoveMat.flatten(), possibleHorizWallMat.flatten(), possibleVertWallMat.flatten()))

    def getActionSize(self):
        return self.generateValidMoveVector(self.player, self.player2, self.getVerticalWallMatrix(), self.getHorizontalWallMatrix()).size
    # todo - create entire board representation as list of matrices
    # will essentially be 9x9x24= 2 player 9x9 matrices, 20 walls remaining 9x9 matrices, 2 wall 9x9 matrices
    #order: northPlayer, north walls, south player, south walls, horizontal, vertical
    def getFullRepresentation(self, north_player, south_player, h_walls, v_walls, north_walls_remaining, south_walls_remaining):
        finalList = []
        northMat = np.zeros((9,9), dtype=int)
        northMat[north_player[0], north_player[1]] = 1
        finalList.append(northMat)

        for i in range(10):
            if (north_walls_remaining > i):
                finalList.append(np.ones((9,9), dtype=int))
            else:
                finalList.append(np.zeros((9,9), dtype=int))
        southMat = np.zeros((9,9), dtype=int)
        southMat[south_player[0], south_player[1]] = 1
        finalList.append(southMat)

        for i in range(10):
            if (south_walls_remaining > i):
                finalList.append(np.ones((9,9), dtype=int))
            else:
                finalList.append(np.zeros((9,9), dtype=int))

        finalList.append(h_walls)
        finalList.append(v_walls)

        return finalList



    # todo: horizontal symmetry property: board reflected horizontally is same. 
    # the code we want to use has a method that takes a board (like our 9x9x24 above) and a vector of moves (like our 243 size vector)
    # and returns the modified versions after horizontal board flip
    
    def getH_WallSymmetries(self, h_walls):
        return self.shiftright9x9(np.fliplr(h_walls))
        
        
    def getV_WallSymmetries(self, v_walls):
        return self.shiftright9x9(np.fliplr(v_walls))

    def getFullRepSymmetry(self, fullRep):
        finalList = []
        #north_player flipped
        finalList.append(np.fliplr(fullRep[0]))
        #north_player walls remaining
        finalList.append(fullRep[1:11])
        #south_player flipped
        finalList.append(np.fliplr(fullRep[11]))
        #south_player walls remaining
        finalList.append(fullRep[12:22])
        #horizontal walls
        finalList.append(self.getH_WallSymmetries(fullRep[22]))
        #vertical walls
        finalList.append(self.getV_WallSymmetries(fullRep[23]))
        return finalList
    
    
    #takes a flattened vector of 243 values and returns the symmetric representation
    def validMoveSymmetry(self, validMoves):
        
        #reshape each piece of the vector and get symmetry
        pawn_moves = np.fliplr(validMoves[0:81].reshape(9,9))
        horiz_walls = self.getH_WallSymmetries(validMoves[81:162].reshape(9,9))
        vert_walls = self.getV_WallSymmetries(validMoves[162:243].reshape(9,9))
        
        # flatten and return
        return np.concatenate((pawn_moves.flatten(), horiz_walls.flatten(), vert_walls.flatten()))
                      
    def display(self, north_player, south_player, horizontal_walls, vertical_walls, numPlayerWalls, numPlayer2Walls):
        cols = "abcdefghi"
        for i in range(0,9):
            print("")
            print(str(i+1) + " ", end="")
            for j in range(0,9):
                #check vert walls
                if(vertical_walls[i][j] == 1):
                    print("|", end="")
                elif((i != 8) and vertical_walls[i+1][j] == 1):
                    print("|",end="")
                else:
                    print(" ", end="")
                #check north player
                
                if(north_player[i][j] == 1):
                    print("N",end="")
                #check south player
                elif(south_player[i][j] == 1):
                    print("S",end="")
                else:
                    print("O",end="")
            print("\n   ",end="")
        
            for k in range(0,9):
                printWall = False
                if((i != 8) and (k!=8) and horizontal_walls[i+1][k+1] == 1):
                    print("-", end="")
                    printWall = True
                elif((i != 8) and horizontal_walls[i+1][k] == 1):
                    print("-", end="")
                    printWall = True  
            
                if(printWall == False):
                    print("  ",end="")
                else:
                    print(" ",end="")
        print("")
                
                
        #print column reference
        #print("")
        print("   ", end="")
        for a in cols:
            print(a + " ", end="")
        print("")
        
        #print num walls left
        print("Number of North Player Walls left: " + str(numPlayerWalls))
        print("Number of South Player Walls left: " + str(numPlayer2Walls))            
                        
    def getCannonicalForm(self, fullRep, player):
        #take in full representation and player and return the correct perspective
        finalList = []
        if(player == 1):
            return fullRep
        else:
            #South player becomes north player and matrices are rotated 180
            #south_player flipped
            finalList.append(np.rot90(fullRep[11], 2))
            #south_player walls remaining
            finalList.append(fullRep[12:22])
            #north_player from south perspective
            finalList.append(np.rot90(fullRep[0], 2))
            #north_player walls remaining
            finalList.append(fullRep[1:11])
            #horizontal walls
            finalList.append(self.seeV_WallsFlipped(fullRep[22]))
            #vertical walls
            finalList.append(self.seeH_WallsFlipped(fullRep[23]))
            return fullRep
                  
                      
                      
     
            
