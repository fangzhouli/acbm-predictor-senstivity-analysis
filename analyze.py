from analyzers import *


def analyze_all():
    delta = DeltaAnalyzer()
    dgsm = DGSMAnalyzer()
    fast = FastAnalyzer()
    morris = MorrisAnalyzer()
    rbd_fast = RDBFastAnalyzer()
    sobol = SobolAnalyzer()

    delta.analyze()
    dgsm.analyze()
    fast.analyze()
    morris.analyze()
    rbd_fast.analyze()
    sobol.analyze()


if __name__ == '__main__':
    analyze_all()
