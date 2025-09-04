# Clean-Air Companion (Week 1)

## Project
**Clean-Air Companion: Forecasting Air Quality and Identifying Safe Outdoor Hours**

This Week-1 notebook processes **Mumbai hourly air quality data** from Kaggle’s
*Air Quality Data in India (2015–2020)* dataset.

## Deliverables
- `Week1_EDA.ipynb` → Jupyter notebook with data cleaning, AQI calculation, safe/unsafe classification, EDA, and export.
- `sample_data_cleaned.csv` → cleaned sample (last 30 days, <=10MB for LMS).
- `requirements.txt` → Python dependencies.

## Dataset
- Kaggle dataset: [Air Quality Data in India (2015–2020, hourly)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
- City: **Mumbai**
- Pollutants: PM2.5, PM10, NO2, O3, CO, SO2
- AQI computed using CPCB methodology.

## How to run
1. Place `city_hour.csv` in the working folder.
2. Run `Week1_EDA.ipynb` from top to bottom.
3. The notebook outputs `sample_data_cleaned.csv`.

## Notes
- Safe Hours = AQI ≤ 100 (Good or Satisfactory).
- Week 2 will build forecasting models (ARIMA, ML, DL) and a Streamlit app.
