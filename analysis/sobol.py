import pickle

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class SobolAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/sobol.txt"""

        X = saltelli.sample(self.problem, 1000, seed = 1)
        Y = ACBM.evaluate(X)
        si = sobol.analyze(self.problem, Y, seed = 2)
        pickle.dump(si, open(self.path_output + 'sobol.txt', 'wb'))