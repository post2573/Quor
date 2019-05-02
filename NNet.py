import os
import sys

import numpy as np

from NeuralNet import NeuralNet
from QuorNNet import QuorNNet

class NNetWrapper(NeuralNet):
    def __init__(self, game):
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        
        
    def train(self, examples):
        input_boards, target_pis, target_vs = list(zip(*examples))
        input_boards = np.asarray(input_boards)
        target_pis = np.asarray(target_pis)
        target_vs = np.asarray(target_vs)
        #NEED TO FIGURE OUT BATCH SIZE AND EPOCHS and VERBOSE?
        self.nnet.model.fit(x = input_boards, y = [target_pis, target_vs], batch_size = , epochs = args.epochs)
