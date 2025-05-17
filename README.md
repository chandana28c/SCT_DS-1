# Demographic Data Visualization

This repository contains a Python script that generates visualizations for simulated demographic data, including age distribution and gender counts.

## Overview

The script creates a dataset of 200 simulated individuals with:

- **Age**: Normally distributed around 30 years old.
- **Gender**: Categories include Male, Female, and Other with probabilities 45%, 45%, and 10% respectively.

It then produces two charts:

- **Age Distribution Histogram** with KDE.
- **Gender Distribution Bar Chart**.

Both charts are saved as PNG image files.

## Files

- `visualize_demographics.py` — The Python script that generates the data and plots.
- `age_distribution.png` — Histogram of ages.
- `gender_distribution.png` — Bar chart of gender counts.

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib

## Installation

Install required Python packages using pip:

```bash
pip install pandas numpy seaborn matplotlib
