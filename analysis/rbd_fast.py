import pickle

from SALib.sample import latin
from SALib.analyze import rbd_fast
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class RDBFastAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = latin.sample(self.problem, 1000)
        Y = ACBM.evaluate(X)
        si = rbd_fast.analyze(
            problem = self.problem,
            X = X,
            Y = np.array(Y))

        pickle.dump(si, open(self.path_output + 'rbd_fast.txt', 'wb'))

if __name__ == '__main__':
    alzr = RDBFastAnalyzer()
    alzr.analyze()