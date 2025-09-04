Clean-Air Companion 🌍

Forecasting Air Quality and Identifying Safe Outdoor Hours

📌 Project Overview

This project builds a Clean-Air Companion that predicts Air Quality Index (AQI) and identifies safe vs unsafe outdoor hours for human activities.

The project is completed as part of the AICTE Virtual Internship, progressing week by week.

Dataset: Air Quality Data in India (2015–2020, hourly)

Focus City: Mumbai

Pollutants: PM2.5, PM10, NO2, O3, CO, SO2

AQI Standard: CPCB (India)

📂 Repository Structure
Clean-Air-Companion/
 ┣ Week1/
 ┃ ┣ Week1_EDA.ipynb
 ┃ ┣ sample_data_cleaned.csv
 ┃ ┣ README.md
 ┃ ┗ requirements.txt
 ┣ Week2/
 ┃ ┣ Week2_EDA_and_Baseline.ipynb
 ┃ ┣ aqi_features.csv
 ┃ ┣ README.md
 ┃ ┗ requirements.txt
 ┗ README.md   ← (this file)
✅ Week 1 — Data Preparation & Initial EDA

Selected Mumbai hourly dataset (city_hour.csv)

Cleaned missing values (time interpolation, up to 6h gaps)

Computed AQI using CPCB standards (PM2.5 & PM10)

Classified safe vs unsafe hours (threshold AQI ≤ 100)

Performed initial EDA:

Histograms of pollutants

AQI time series plots

Diurnal AQI variation

Deliverables:

Week1_EDA.ipynb

sample_data_cleaned.csv

requirements.txt

✅ Week 2 — Advanced EDA & Baseline Models

Added feature engineering:

Time features (hour, weekday, month)

Lag features (AQI_t-1 … AQI_t-24)

Rolling averages (3h, 6h, 12h, 24h)

Conducted Advanced EDA:

Correlation heatmap

Weekly patterns

Safe-hour analysis

Built baseline ML models:

Persistence model (t+1 = t)

24h Moving Average

Evaluated performance:

Persistence → RMSE ≈ 18.07, R² ≈ 0.93

Moving Average → RMSE ≈ 34.22, R² ≈ 0.77

Exported engineered dataset: aqi_features.csv

Deliverables:

Week2_EDA_and_Baseline.ipynb

aqi_features.csv

requirements.txt

🚀 Next Steps (Week 3 & beyond)

Train advanced ML models (Random Forest, XGBoost, LSTM)

Build a Streamlit dashboard for safe/unsafe hour recommendations

Prepare project PPT & final report

📦 Requirements

Core dependencies:

pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
pmdarima
plotly
streamlit