import numpy as np

class RandomPlayer():
    
    def __init__(self, game):
        self.game = game  
        
    def play(self, board):
        a = np.random.randint(243)
        valids = self.game.generateValidMoveVector(game.player, game.player2, game.h_walls, game.v_walls)
        while valids[a]!=1:
            a = np.random.randint(243)
        return a
        
        
class HumanPlayer():
    
    def __init__(self, game):
        self.game = game
        
    def play(self, game):
        #display the board for the user so they can see options
        self.game.display(self.game.getPlayerMatrix(), self.game.getPlayer2Matrix(), self.game.getHorizontalWallMatrix(), self.game.getVerticalWallMatrix(), self.game.getNumPlayerWalls(), self.game.getNumPlayer2Walls())
        valid_pawn_moves = self.game.generateValidNorthPawnMoves(self.game.player, self.game.player2, self.game.h_walls, self.game.v_walls) 
        print("Valid Pawn Moves: ")
        for i in range(9):
            for j in range(9):
                if valid_pawn_moves[i][j]:
                    print(str(i+1), str(j+1))
        valid_vertWalls = self.game.generateValidVertWalls(self.game.player, self.game.player2, self.game.h_walls, self.game.v_walls)
        valid_horizWalls = self.game.generateValidHorizWalls(self.game.player, self.game.player2, self.game.h_walls, self.game.v_walls)
                
        while True: 
            print("while loop")
            # Python 3.x
            print("enter a move (e.g. a3 or c4v): ")
            a = input()
            # Python 2.x 
            # a = raw_input()
            if(len(a) == 3):
                if(a[2] == 'v'):
                    result = self.game.isValidMove(a,valid_vertWalls)
                elif(a[2] == 'h'):
                    result = self.game.isValidMove(a,valid_horizWalls)
            elif(len(a) == 2):
                result = self.game.isValidMove(a,valid_pawn_moves)
            if(result == True):
                break
            else:
                print('Invalid')
            #need to add break down for a wall move
            #make a method in GameState that takes in single move?
        return a
      