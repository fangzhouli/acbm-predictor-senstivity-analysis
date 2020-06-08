import pickle

from SALib.sample import latin
from SALib.analyze import delta
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class DeltaAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/delta.txt"""

        X = latin.sample(self.problem, 1000, seed = 9)
        Y = ACBM.evaluate(X)
        si = delta.analyze(self.problem, X, Y, seed = 10)
        pickle.dump(si, open(self.path_output + 'delta.txt', 'wb'))