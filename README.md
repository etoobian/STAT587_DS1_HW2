# STAT 587 — Data Science I — Homework 2 (Winter 2026)

This repository contains the code and reproducible analysis used to generate the figures and tables for Homework 2.

## Assignment Overview

### Question 1: College data (ISLP)
Predict the number of applications received (`Apps`) using the remaining variables:
- Linear regression (least squares)
- Regression tree + pruning via cross-validation
- Bagging (B = 500, 1000)
- Random forest (B = 500, 1000; m = 3)
- Comparison and recommendation

### Question 2: Business school admissions (admission.csv)
Classify applicants into three categories (admit / do not admit / borderline):
- Exploratory analysis (training set)
- LDA + decision boundary + performance (train/test)
- QDA + decision boundary + performance (train/test)
- KNN (choose K using test error) + metrics + test error
- Comparison and recommendation

## Repository Structure

- `data/`  
  Input data files (e.g., `admission.csv`)

- `notebooks/`  
  Working Jupyter notebook(s) used for analysis and figure/table generation

- `src/`  
  Helper Python modules/functions used by the notebook(s)

- `reports/figures/`  
  Saved figures used in the written submission

- `reports/tables/`  
  Saved tables used in the written submission

## How to Run

1. Create an environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open and run the notebook(s) in `notebooks/` top-to-bottom.

   Notes:

   - Random seeds are fixed to support reproducibility
   - Figures/tables are saved to `reports/figures/` and `reports/tables`.
   
