import pickle

from SALib.sample import latin
from SALib.analyze import delta
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class DeltaAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = latin.sample(self.problem, 1000)
        Y = ACBM.evaluate(X)
        si = delta.analyze(
            problem = self.problem,
            X = X,
            Y = np.array(Y))

        pickle.dump(si, open(self.path_output + 'delta1.txt', 'wb'))

if __name__ == '__main__':
    alzr = DeltaAnalyzer()
    alzr.analyze()