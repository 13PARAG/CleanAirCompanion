# 🌱 Clean-Air Companion: Forecasting AQI & Identifying Safe Hours  

An end-to-end data science project to **forecast air quality (AQI)** and **identify safe outdoor hours** using real-world data from Mumbai.  
This is the **final consolidated version** containing all steps (Week 1 + Week 2 + Week 3) in one notebook.  

## Live Demo

Try the Clean-Air Companion app online:

https://cleanaircompanion-ebkheshtnnqxdpgranvmzl.streamlit.app


## 📌 Project Overview  
Urban air pollution impacts millions of people daily.  
Citizens lack real-time, easy-to-use tools to decide when it's safe to go outdoors.  

This project provides:  
- Cleaning & processing of real hourly AQI data  
- AQI computation using **CPCB methodology**  
- Identification of safe/unsafe hours  
- Machine learning models for AQI forecasting  
- Streamlit dashboard for public use  

## 📂 Repository Structure  

final_project/
├── Week3_Modeling_Final.ipynb   # Main notebook (data cleaning → feature engineering → modeling)
├── aqi_features.csv             # Pre-engineered features dataset
├── best_model.pkl               # Saved best model (Random Forest / XGBoost)
├── streamlit_app.py             # Streamlit app for prediction visualization
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation

## 🛠 Tech Stack  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost  
- **Deployment:** Streamlit  
- **Version Control:** GitHub  

## 📊 Results  
| Model | RMSE | MAE | R² |
|------|------|------|----|
| Persistence | ~18.07 | ~11.07 | ~0.93 |
| Moving Avg (24h) | ~34.22 | ~22.99 | ~0.77 |
| Random Forest | **Best** | Lowest | Highest |
| XGBoost | Slightly higher RMSE | – | – |

✅ **Random Forest** selected as final model → saved as `best_model.pkl`

## 🚀 How to Run  
Clone this repository:  
```bash
git clone https://github.com/13PARAG/CleanAirCompanion.git
cd CleanAirCompanion/final_project
```

Run the notebook in **Google Colab** or Jupyter Notebook:  
1. Upload `aqi_features.csv` if not already in the folder  
2. Run all cells top-to-bottom  

Optional: Launch Streamlit app for visualization  
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🎯 Future Scope  
- Live AQI API integration  
- City-wise generalization across India  
- Push notifications for safe hours via a mobile/web app  
