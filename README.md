# FTSE 100 Index Analysis: Trends, Predictions, and Global Event Impact (2009-2023)

## Overview

This project presents an in-depth analysis of the Financial Times Stock Exchange 100 Index (FTSE 100) over a 15-year period from 2009 to 2023. The analysis examines market trends, evaluates the impact of major global events on stock prices, and implements machine learning models for price prediction.

## Project Objectives

- Study long-term trends in the FTSE 100 Index
- Analyze the impact of major global events on stock market performance
- Develop and evaluate machine learning models for stock price prediction
- Demonstrate proficiency in data preprocessing, exploratory data analysis (EDA), and model development

## Dataset

**Source**: Wall Street Journal (CSV format)  
**Time Period**: 2009-2023  
**Features**:
- **Date**: Date of stock market activity
- **Open Price**: Average price at market open
- **Close Price**: Average price at market close
- **Low Price**: Lowest average price of the day
- **High Price**: Highest average price of the day
- **Volume**: Total number of shares traded

## Analysis Components

### Exploratory Data Analysis (EDA)

#### 1. Scatter Plot Analysis

Visualizes the relationship between opening and closing prices over time.

**Key Findings**:
- Positive trend in mean opening and closing prices over 15 years
- Significant decline after 2020 due to COVID-19 pandemic
- Strong recovery from late 2021 onwards

#### 2. Line Graph Analysis

Plots average high and low prices throughout the analysis period.

**Key Findings**:
- Price increase following the 2008-09 financial crisis
- Notable decline from 2015-2016 (potential Brexit impact)
- Significant drop in early 2020 (COVID-19) followed by recovery

#### 3. Box Plot Analysis

Summarizes data distribution using five-number summary for closing prices and volume.

**Key Findings**:
- Clear price increase post-2010 with declines in 2012, 2015, and 2016
- 2020 box showed higher volatility with more outliers due to COVID-19
- Volume maintained consistent medians despite global events

#### 4. Correlation Heatmap

Illustrates correlations between all price variables.

**Key Findings**:
- Strong positive correlations among all price columns
- Weaker correlation between open and close prices indicates daily fluctuations
- Stronger correlation between high and low prices suggests minor trading variations

## Data Preprocessing

The following preprocessing steps were implemented to prepare data for modeling:

1. Converted 'Date' column to datetime object and set as DataFrame index
2. Omitted 'Volume' column from analysis
3. Resampled data to calculate monthly means for all price columns
4. Formatted date index to 'YYYY-MM' string format

## Machine Learning Models


### Objective
Predict closing prices based on opening prices to identify market correlations.

### Model Architecture

#### First Model
- **Architecture**: Sequential neural network with 3 layers (64, 64, 1 neurons)
- **Activation**: ReLU
- **Loss Function**: Mean Squared Error
- **Optimizer**: Adam (learning rate: 0.001)
- **Performance**: Generally captured trends but tended to overestimate predictions

#### Second Model (Improved)
- **Architecture**: Enhanced with 4 layers (128, 128, 64, 1 neurons)
- **Performance**: Significantly improved prediction accuracy with closer alignment between predicted and actual values

### Data Handling
- Custom training/testing split using TrainTest_CO.py module
- Data normalization for optimal model training

## Key Historical Events Impact

The analysis identified clear market responses to major global events:
- **2008-09 Financial Crisis**: Recovery period visible in early data
- **Brexit (2015-2016)**: Notable market decline
- **COVID-19 Pandemic (2020)**: Significant drop followed by strong recovery

## Technologies Used

- Python
- TensorFlow/Keras (Neural Networks)
- Pandas (Data Manipulation)
- NumPy (Numerical Computing)
- Matplotlib/Seaborn (Data Visualization)
- Custom modules for data splitting

## Team Contributors

- **Tina Azad Arjastan**: Scatter Plot Analysis
- **Fabio Rodrigues**: Line Graph and Box Plot Analysis
- **Camilo Sheldon Barreto**: Correlation Heatmap Analysis
- **Chids Osuala**: Machine Learning Model Implementation

## Results Summary

This comprehensive analysis successfully demonstrates the FTSE 100's resilience and recovery patterns over a 15-year period. The machine learning models show promising results in predicting closing prices based on opening prices, with the enhanced model achieving significantly improved accuracy.

## References

- Exploratory Data Analysis on Stock Market Data
- What is Exploratory Data Analysis?

## Files Structure

```
├── data/
│   └── ftse100_data.csv
├── src/
│   ├── TrainTest_CO.py
│   └── analysis_scripts/
├── visualizations/
└── README.md
```

---

*This project showcases advanced data analysis techniques and machine learning applications in financial market analysis.*
