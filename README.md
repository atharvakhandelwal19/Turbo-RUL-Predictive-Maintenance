<div align="center">

# 🛫 TurboRUL

### Deep Learning Framework for Predictive Maintenance of Aircraft Turbofan Engines

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NASA C-MAPSS](https://img.shields.io/badge/Dataset-NASA%20C--MAPSS-green.svg)](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/yourusername/TurboRUL-Predictive-Maintenance)

<p align="center">
  <img src="reports/figures/project_banner.png" alt="TurboRUL Banner" width="800"/>
</p>

**A comprehensive machine learning and deep learning framework for predicting Remaining Useful Life (RUL) of aircraft turbofan engines using NASA's C-MAPSS dataset, featuring advanced feature engineering, ensemble methods, attention-based neural networks, and explainable AI techniques.**

[📖 Documentation](#documentation) •
[🚀 Quick Start](#quick-start) •
[📊 Results](#results) •
[🎯 Demo](#interactive-dashboard) •
[📝 Citation](#citation)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Methodology](#methodology)
- [Models Implemented](#models-implemented)
- [Results](#results)
- [Explainability](#explainability)
- [Interactive Dashboard](#interactive-dashboard)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

**Predictive maintenance** is a critical component in aviation safety and operational efficiency. This project presents a comprehensive framework for predicting the **Remaining Useful Life (RUL)** of aircraft turbofan engines—the number of operational cycles an engine can perform before requiring maintenance or facing failure.

### Problem Statement

Aircraft engine failures can have catastrophic consequences. Traditional maintenance strategies include:

| Strategy | Description | Limitation |
|----------|-------------|------------|
| **Reactive** | Fix after failure | Dangerous, costly downtime |
| **Preventive** | Fixed schedule maintenance | Wasteful, doesn't account for actual condition |
| **Predictive** | Condition-based maintenance | Requires accurate RUL prediction |

This project develops **state-of-the-art predictive models** that analyze multi-sensor time-series data to accurately forecast engine RUL, enabling:

- ✅ **Optimal maintenance scheduling**
- ✅ **Reduced unexpected failures**
- ✅ **Minimized maintenance costs**
- ✅ **Enhanced operational safety**

### Research Objectives

1. Develop robust feature engineering pipelines incorporating domain knowledge
2. Implement and compare multiple ML/DL architectures for RUL prediction
3. Address the challenge of multiple operating conditions and fault modes
4. Provide uncertainty quantification for reliable predictions
5. Create interpretable models with explainable AI techniques
6. Build a real-time monitoring and prediction system

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔧 Data Processing
- Automated data loading for all C-MAPSS subsets
- Operating condition clustering and normalization
- Comprehensive missing value handling
- Train-validation-test splitting by engine

</td>
<td width="50%">

### 📊 Feature Engineering
- 50+ engineered features per sensor
- Rolling statistics (mean, std, min, max, skew, kurtosis)
- Physics-based efficiency indicators
- Frequency domain features (FFT, spectral entropy)

</td>
</tr>
<tr>
<td width="50%">

### 🤖 Machine Learning Models
- Baseline models (Linear, SVR, KNN)
- Ensemble methods (Random Forest, XGBoost, LightGBM, CatBoost)
- Stacking and weighted ensembles
- Bayesian hyperparameter optimization

</td>
<td width="50%">

### 🧠 Deep Learning Models
- LSTM and Bidirectional LSTM
- 1D CNN and Temporal Convolutional Networks
- CNN-LSTM Hybrid architectures
- Transformer with self-attention
- Attention mechanism visualization

</td>
</tr>
<tr>
<td width="50%">

### 📈 Advanced Techniques
- Uncertainty quantification (MC Dropout)
- Custom asymmetric loss functions
- Piecewise linear RUL formulation
- Transfer learning across datasets

</td>
<td width="50%">

### 🔍 Explainability
- SHAP (SHapley Additive exPlanations)
- Feature importance analysis
- Attention weight visualization
- Sensor contribution analysis

</td>
</tr>
</table>

---

## 📁 Project Structure