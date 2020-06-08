import pickle

from SALib.sample import latin
from SALib.analyze import rbd_fast
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class RDBFastAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/rbd_fast.txt"""

        X = latin.sample(self.problem, 1000, seed = 5)
        Y = ACBM.evaluate(X)
        si = rbd_fast.analyze(self.problem, X, Y, M = 10, seed = 6)
        pickle.dump(si, open(self.path_output + 'rbd_fast.txt', 'wb'))