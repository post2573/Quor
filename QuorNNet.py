import sys
sys.path.append('..')
from utils import *

import argparse
from keras.models import *
from keras.layers import *
from keras.optimizers import *

class QuorNNet():
    #other NNets send in args... not sure what args is
    def __init__(self, game, args):
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        self.args = args
        
        # Neural Net
        #instantiates a Keras tensor (a tensor object from the underlying backend, TensorFlow)
        #Arguments: shape (doesn't include batch size) indicates that the input will be x by y dimensional vectors
        self.input_boards = Input(shape=(self.board_x, self.board_y))
        
        #Reshapes an output of certain shape, this is the first layer in the model
        #Arguements: target shape 
        x_image = Reshape((self.board_x, self.board_y, 1))(self.input_boards)