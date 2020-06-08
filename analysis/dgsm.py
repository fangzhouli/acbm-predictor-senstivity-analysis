from math import log
import pickle

from SALib.sample import finite_diff
from SALib.analyze import dgsm
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class DGSMAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/dgsm.txt"""

        X = finite_diff.sample(self.problem, 1000, delta = 0.0001, seed = 11)
        Y = ACBM.evaluate(X)
        si = dgsm.analyze(self.problem, X, Y, seed = 12)

        # scale down the values of vi
        si['vi'] = [x ** (1 / 16) for x in si['vi']]
        pickle.dump(si, open(self.path_output + 'dgsm.txt', 'wb'))