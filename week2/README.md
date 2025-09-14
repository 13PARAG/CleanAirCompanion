# Clean-Air Companion: Forecasting Air Quality and Identifying Safe Outdoor Hours

## 📌 Project Overview
This project builds a **Clean-Air Companion** that predicts **Air Quality Index (AQI)** and recommends **safe vs unsafe outdoor hours**.  
The city of focus is **Mumbai**, using data from Kaggle’s *Air Quality Data in India (2015–2020)*.

---

## ✅ Week 1 — Data Preparation & Initial EDA
- Selected **Mumbai hourly dataset** (`city_hour.csv`)
- Cleaned missing values (time interpolation, up to 6h gaps)
- Computed **AQI** using CPCB standards (PM2.5 & PM10)
- Classified **safe vs unsafe hours** (threshold AQI ≤ 100)
- Performed initial EDA:
  - Histograms of pollutants
  - Time series plots of AQI
  - Diurnal variation of AQI

---

## ✅ Week 2 — Advanced EDA & Baseline ML Models
- **Advanced EDA**
  - Correlation heatmap of pollutants vs AQI
  - Weekly seasonal patterns
  - AQI distribution
  - Safe-hour % by weekday
- **Baseline Forecasting Models**
  - Persistence (t+1 = t)
  - Moving Average (24h)
- **Evaluation Metrics**
  - RMSE, MAE, R²
- **Feature Engineering**
  - Lag features: AQI(t-1, t-2, …, t-24)
  - Rolling averages: 3h, 6h, 12h, 24h
  - Time features: hour, weekday, month
- Exported `aqi_features.csv` → for Week 3 ML models

---

## 📂 How to Run
1. Open **`Week2_EDA_and_Baseline.ipynb`** in Google Colab  
2. Upload `city_hour.csv` into Colab runtime  
3. Run all cells (Runtime → Run all)  
4. Outputs:
   - Advanced EDA plots
   - Baseline forecast results
   - Exported dataset: `aqi_features.csv`

---

## 📦 Requirements
See [requirements.txt](requirements.txt).  
Key libraries:  
- pandas, numpy, matplotlib, seaborn, scikit-learn  
- statsmodels, pmdarima  
- plotly, streamlit (for later visualization/dashboard work)
