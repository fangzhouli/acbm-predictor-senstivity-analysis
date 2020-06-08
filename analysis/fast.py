import pickle

from SALib.sample import fast_sampler
from SALib.analyze import fast
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class FastAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/fast.txt"""

        X = fast_sampler.sample(self.problem, 1000, M = 4, seed = 3)
        Y = ACBM.evaluate(X)
        si = fast.analyze(self.problem, Y, M = 4, seed = 4)
        pickle.dump(si, open(self.path_output + 'fast.txt', 'wb'))