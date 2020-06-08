import pickle

from SALib.sample.morris import sample as m_sample
from SALib.analyze.morris import analyze as m_analyze
import numpy as np

from function import ACBM
from analysis._base import Analyzer

class MorrisAnalyzer(Analyzer):

    def analyze(self):
        """store analysis output at /data/output/morris.txt"""

        X = m_sample(self.problem, 1000, num_levels = 4, seed = 7)
        Y = ACBM.evaluate(X)
        si = m_analyze(self.problem, X, Y, num_levels = 4, seed = 8)
        pickle.dump(si, open(self.path_output + 'morris.txt', 'wb'))