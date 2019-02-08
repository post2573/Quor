#!/usr/bin/env python

import GameState as g

def Main():
    game = g.GameState()
    print('Position of Player 1: ' + str(game.player2))
    print(game.player)
    
    #print(game.getNumPlayerWalls())
    #print(game.getNumPlayer2Walls())
    #print(game.getWallMatrices(1))
    
    game.placePlayer(5,6)
    print(game.player)
Main()