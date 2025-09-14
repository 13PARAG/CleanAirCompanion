# 📖 Clean-Air Companion – Final Project  

This folder contains the **complete end-to-end pipeline** for AQI forecasting & safe-hour identification.  

## Files  
| File | Description |
|------|-------------|
| `Week3_Modeling_Final.ipynb` | Main notebook combining Week 1, Week 2, and Week 3 |
| `aqi_features.csv` | Pre-engineered feature dataset |
| `best_model.pkl` | Best-trained ML model |
| `streamlit_app.py` | Streamlit dashboard for predictions |
| `requirements.txt` | List of dependencies |

## How to Run  
1. Open the notebook in **Google Colab**  
2. Run all cells to retrain the model and regenerate predictions  
3. To view results interactively, launch the Streamlit app  

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Example Output  
- 📊 **Model Performance Table**
- 📈 Actual vs Predicted AQI plot  
- ✅ Safe vs Unsafe hours count  

---

This is the final deliverable for submission.
