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
        
    def play(self, board):
        game.display(game.getPlayerMatrix(), game.getPlayer2Matrix(), game.getHorizontalWallMatrix(), game.getVerticalWallMatrix(), game.getNumPlayerWalls(), game.getNumPlayer2Walls())
        valid_pawn_moves = self.game.generateValidNorthPawnMoves(game.player, game.player2, game.h_walls, game.v_walls)
        print("Valid Pawn Moves: ")
        for i in range(9):
            for j in range(9):
                if valid_pawn_moves[i][j]:
                    print(str(i+1), str(j+1))
                
        print("Valid Horizontal Wall Moves: ")        
        valid_horiz_moves = self.game.generateValidHorizWalls(game.player, game.player2, game.h_walls, game.v_walls)
        for i in range(0,9):
            for j in range(0,9):
                if valid_horiz_moves[i][j]:
                    print(str(i+1), str(j+1))
                    
        print("Valid Vertical Wall Moves: ")        
        valid_vert_moves = self.game.generateValidVertWalls(game.player, game.player2, game.h_walls, game.v_walls)
        for i in range(0,9):
            for j in range(0,9):
                if valid_vert_moves[i][j]:
                    print(str(i+1), str(j+1))            
                
                
        while True: 
            # Python 3.x
            print("enter a move (e.g. a3 or c4v): ")
            a = input()
            # Python 2.x 
            # a = raw_input()
            if(a.len() == 3):
                x,y = [int(x) for x in a.split(' ')]
                if valid_pawn_moves[x][y]:
                    break
                else:
                    print('Invalid')
            #need to add break down for a wall move
            #make a method in GameState that takes in single move?
        return a
      