
import streamlit as st
import pandas as pd
import joblib
import os
import gdown

MODEL_PATH = "model_artifact.pkl"
MODEL_DRIVE_ID = "1zwjmAoeneR5yCchbnrGfRTaCQ-JTCJ84"  # <-- REPLACE THIS!

def download_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model from Google Drive..."):
            url = f"https://drive.google.com/uc?id={MODEL_DRIVE_ID}"
            try:
                gdown.download(url, MODEL_PATH, quiet=False)
                st.success("Model downloaded successfully!")
            except Exception as e:
                st.error(f"Failed to download model: {e}")
                st.stop()

# Download the model if not present
download_model()

@st.cache_resource
def load_artifact():
    data = joblib.load(MODEL_PATH)
    return data["model"], data["meta"]

st.title("🌤️ Clean-Air Companion")
st.write("Upload a CSV with engineered AQI features (use provided template).")

model, meta = load_artifact()
expected_features = meta["feature_names"]
medians = meta.get("medians", {})

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    try:
        new_df = pd.read_csv(uploaded)
        for col in ["AQI", "AQI_category", "Datetime", "is_safe_hour"]:
            if col in new_df.columns:
                new_df.drop(columns=col, inplace=True)

        missing = [c for c in expected_features if c not in new_df.columns]
        for c in missing:
            new_df[c] = medians.get(c, 0.0)

        new_df = new_df[expected_features].apply(pd.to_numeric, errors="coerce").fillna(0.0)
        preds = model.predict(new_df)

        st.success(f"Predictions generated for {len(preds)} rows.")
        st.line_chart(pd.Series(preds, name="Predicted AQI"))
        st.metric("✅ Safe Hours", int((preds <= 100).sum()))
        st.metric("⚠️ Unsafe Hours", int((preds > 100).sum()))

        result_df = new_df.copy()
        result_df["predicted_AQI"] = preds
        st.download_button("Download Predictions", result_df.to_csv(index=False), "predictions.csv")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

