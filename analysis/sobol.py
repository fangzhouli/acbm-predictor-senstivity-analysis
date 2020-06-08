import pickle

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class SobolAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = saltelli.sample(self.problem, 1000)
        Y = ACBM.evaluate(X)
        si = sobol.analyze(
            problem = self.problem,
            Y = np.array(Y))

        pickle.dump(si, open(self.path_output + 'sobol.txt', 'wb'))

if __name__ == '__main__':
    alzr = SobolAnalyzer()
    alzr.analyze()