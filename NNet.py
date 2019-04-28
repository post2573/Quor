import os
import sys

import numpy as np

from NeuralNet import NeuralNet
from QuorNNet import QuorNNet

class NNetWrapper(NeuralNet):
    def __init__(self, game):
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()