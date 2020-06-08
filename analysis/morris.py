import pickle

from SALib.sample.morris import sample as m_sample
from SALib.analyze.morris import analyze as m_analyze
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class MorrisAnalyzer(Analyzer):

    def analyze(self):
        # calculate sensitivity measure
        X = m_sample(self.problem, 1000, num_levels = 4)
        Y = ACBM.evaluate(X)
        si = m_analyze(
            problem = self.problem,
            X = X,
            Y = np.array(Y),
            num_levels = 4)

        pickle.dump(si, open(self.path_output + 'morris.txt', 'wb'))

if __name__ == '__main__':
    alzr = MorrisAnalyzer()
    alzr.analyze()