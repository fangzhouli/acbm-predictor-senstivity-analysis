import pickle

from SALib.sample import fast_sampler
from SALib.analyze import fast
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class FastAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = fast_sampler.sample(self.problem, 1000)
        Y = ACBM.evaluate(X)
        si = fast.analyze(
            problem = self.problem,
            Y = np.array(Y))

        pickle.dump(si, open(self.path_output + 'fast2.txt', 'wb'))

if __name__ == '__main__':
    alzr = FastAnalyzer()
    alzr.analyze()