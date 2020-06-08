from math import log
import pickle

from SALib.sample import finite_diff
from SALib.analyze import dgsm
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class DGSMAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = finite_diff.sample(self.problem, 1000, delta = 0.0001)
        Y = ACBM.evaluate(X)
        si = dgsm.analyze(
            problem = self.problem,
            X = X,
            Y = np.array(Y))

        si['vi'] = [x ** (1 / 16) for x in si['vi']]
        pickle.dump(si, open(self.path_output + 'dgsm.txt', 'wb'))

if __name__ == '__main__':
    alzr = DGSMAnalyzer()
    alzr.analyze()