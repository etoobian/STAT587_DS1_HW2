# STAT 587 — Data Science I — Homework 2 (Winter 2026)

This repository contains the code and reproducible analysis used to generate the figures and tables for Homework 2.
The project was completed with a standardized structure, global output controls, and automated table/figure generation to support reproducibility and clean reporting.

## Assignment Overview

### Question 1: College data (ISLP)
Predict the number of applications received (`Apps`) using the remaining variables:
- Linear regression (least squares)
- Regression tree + pruning via cross-validation
- Bagging (B = 500, 1000)
- Random forest (B = 500, 1000; m = 3)
- Comparison and recommendation

### Question 2: Business school admissions (`admission.csv`)
Classify applicants into three categories (Admit / Not Admit / Border):
- Exploratory analysis (training set)
- Linear Discriminant Analysis (LDA)
  - Decision regions
  - Confusion matrices and misclassification rates (train/test)
  - Multiclass OvR sensitivity, specificity, and AUC
- Quadratic Discriminant Analysis (QDA)
  - Decision regions
  - Confusion matrices and misclassification rates (train/test)
  - Multiclass OvR sensitivity, specificity, and AUC
- K-Nearest Neighbors (KNN)
  - Predictor standardization
  - Selection of K via 5-fold cross-validation
  - Decision regions at optimal K
  - Confusion matrices and multiclass OvR metrics (train/test)
- Final comparison and recommendation based on test-set performance

## Repository Structure

- `data/`  
  Input data files (e.g., `admission.csv`)

- `notebooks/`  
  Working Jupyter notebook(s) used for all analysis, modeling, and figure/table generation

- `src/`  
  Helper modules/functions used by the notebook(s)

- `reports/figures/`  
  Saved figures used in the written submission (automatically generated)

- `reports/tables/`  
  Saved tables used in the written submission (automatically generated)

## Global Output Controls

The notebook uses three global flags to control verbosity and artifact generation:

```python
VERBOSE = True      # Print/display intermediate outputs
SAVE_FIGS = True    # Save figures to reports/figures/
SAVE_TABLES = True  # Save LaTeX tables to reports/tables/
```


## How to Run

1. Create an environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open and run the notebook(s) in `notebooks/` top-to-bottom.

   Notes:

   - Random seeds are fixed to support reproducibility
   - Figures/tables are saved to `reports/figures/` and `reports/tables`.