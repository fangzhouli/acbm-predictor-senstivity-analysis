# A Comprehensive Sensitivity Analysis for the Animal-cell-based Meat Predictor

## Introduction

This project aims to provide a comprehensive sensitivity analysis for animal-cell-based meat (ACBM) cost prediction model.

The analysis consists of the application of 6 algorithms: Morris Method (MM), Sobol Sensitivity Analysis (SSA), Random Balance Designs Fourier Amplitude Sensitivity Test (RBD-FAST), Fourier Amplitude Sensitivity Test (FAST), Delta Moment-Independent Measure (DMIM), and Derivative-based Global Sensitivity Measure (DGSM).

## Usage

### Installation

```console
git clone git@github.com:fangzhouli/ACBM-SA.git
cd path/to/ACBM-SA
pip install .
```

### Usage

```console
python analyze.py  # generates analysis result files in 'acbm/data/output'
python plot.py  # create a spider plot to visualize SA
```

## Methods

![fig](/fig/spiderplot.png)

## Authors

- Fangzhou Li - https://github.com/fangzhouli

## Ackowledgements

- Derrick Risner, for providing ACBM model and data
- Ilias Tagkopoulos, for advisory and documentation review
- SALib, for providing analysis tools https://salib.readthedocs.io/en/latest/