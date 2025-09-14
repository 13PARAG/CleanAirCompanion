
import streamlit as st, pandas as pd, joblib, os

@st.cache_resource
def load_artifact():
    data = joblib.load("model_artifact.pkl")
    return data["model"], data["meta"]

st.title("🌤️ Clean-Air Companion")
st.write("Upload a CSV with engineered AQI features (use provided template).")

if not os.path.exists("model_artifact.pkl"):
    st.error("model_artifact.pkl not found. Please run Week 3 notebook.")
    st.stop()

model, meta = load_artifact()
expected_features = meta["feature_names"]
medians = meta.get("medians", {})

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    try:
        new_df = pd.read_csv(uploaded)
        for col in ["AQI", "AQI_category", "Datetime", "is_safe_hour"]:
            if col in new_df.columns: new_df.drop(columns=col, inplace=True)

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
