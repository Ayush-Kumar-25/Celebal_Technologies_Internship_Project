import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# Load Saved Model and Scaler
# ---------------------------------------
model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ------------------------------------------------------
# Streamlit Page Configuration
# ------------------------------------------------------
st.set_page_config(
    page_title="Air Quality Prediction Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Advanced Air Quality Prediction Dashboard")
st.write("This dashboard predicts PM2.5 levels, visualizes air pollution trends, and analyzes uploaded air quality datasets.")

st.markdown("---")

# ======================================================
# Sidebar - User Inputs
# ======================================================
st.sidebar.header("🔧 Input Parameters for Prediction")

region_list = [
    "African Region",
    "Eastern Mediterranean Region",
    "European Region",
    "Region of the Americas",
    "South East Asia Region",
    "Western Pacific Region"
]

region = st.sidebar.selectbox("Select WHO Region", region_list)
country = st.sidebar.text_input("Enter Country Name", "India")
city = st.sidebar.text_input("Enter City Name", "Delhi")

pm10 = st.sidebar.number_input("PM10 (μg/m³)", min_value=0.0, max_value=600.0, value=50.0)
no2 = st.sidebar.number_input("NO₂ (μg/m³)", min_value=0.0, max_value=200.0, value=30.0)
year = st.sidebar.number_input("Measurement Year", min_value=2000, max_value=2035, value=2022)

# Encoding categorical inputs
region_encoded = {r: i for i, r in enumerate(region_list)}[region]
country_encoded = hash(country) % 10000
city_encoded = hash(city) % 10000

# ======================================================
# Prediction Button
# ======================================================
if st.sidebar.button("Predict PM2.5"):

    input_df = pd.DataFrame({
        "PM10 (μg/m3)": [pm10],
        "NO2 (μg/m3)": [no2],
        "Measurement Year": [year],
        "WHO Region": [region_encoded],
        "WHO Country Name": [country_encoded],
        "City or Locality": [city_encoded]
    })

    # Normalize inputs
    scaled_input = scaler.transform(input_df)

    # Predict PM2.5
    predicted_pm25 = model.predict(scaled_input)[0]

    # ---------------------------------
    # Pollution Category
    # ---------------------------------
    if predicted_pm25 <= 12:
        category = "Good 😊"
        color = "green"
    elif predicted_pm25 <= 35:
        category = "Moderate 🙂"
        color = "orange"
    elif predicted_pm25 <= 55:
        category = "Unhealthy for Sensitive Groups 😐"
        color = "red"
    else:
        category = "Unhealthy 😷"
        color = "darkred"

    # ---------------------------------
    # Pollution Index (Combined Score)
    # ---------------------------------
    pollution_index = (predicted_pm25 + pm10 + no2) / 3

    st.subheader("📊 Prediction Results")
    st.metric("Predicted PM2.5 (μg/m³)", f"{predicted_pm25:.2f}")
    st.metric("Pollution Index", f"{pollution_index:.2f}")

    st.markdown(
        f"<h3 style='color:{color}; text-align:center;'>Air Quality Category: {category}</h3>",
        unsafe_allow_html=True
    )

    st.success("Prediction Successful!")

else:
    st.info("Fill the sidebar inputs and click *Predict PM2.5*.")

# ======================================================
# Section B — File Upload & Dataset Analysis
# ======================================================
st.markdown("---")
st.header("📁 Upload Your Own Air Quality Dataset")

uploaded_file = st.file_uploader("Upload an Excel/CSV file", type=["xlsx", "csv"])

if uploaded_file:
    # Load dataset
    df_uploaded = pd.read_excel(uploaded_file) if uploaded_file.name.endswith("xlsx") else pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Dataset Preview")
    st.dataframe(df_uploaded.head())

    st.write("### Missing Value Summary:")
    st.write(df_uploaded.isnull().sum())

    # ------------------------------
    # Dataset Visualizations
    # ------------------------------
    if "PM2.5 (μg/m3)" in df_uploaded.columns:
        st.subheader("📊 PM2.5 Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df_uploaded["PM2.5 (μg/m3)"], kde=True, ax=ax)
        st.pyplot(fig)

    if "PM10 (μg/m3)" in df_uploaded.columns:
        st.subheader("📊 PM10 Distribution")
        fig, ax = plt.subplots()
        sns.boxplot(x=df_uploaded["PM10 (μg/m3)"], ax=ax)
        st.pyplot(fig)

    if len(df_uploaded.columns) > 1:
        st.subheader("🔥 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(df_uploaded.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

# ======================================================
# Section C — Built-in Charts for User Input
# ======================================================
st.markdown("---")
st.header("📈 Visual Insights From Your Inputs")

col1, col2 = st.columns(2)

with col1:
    st.subheader("PM10 vs NO2")
    fig, ax = plt.subplots()
    ax.bar(["PM10", "NO2"], [pm10, no2], color=["blue", "purple"])
    st.pyplot(fig)

with col2:
    st.subheader("Pollution Index Components")
    fig, ax = plt.subplots()
    ax.bar(["PM2.5 (Predicted)", "PM10", "NO2"],
           [predicted_pm25 if 'predicted_pm25' in locals() else 0, pm10, no2],
           color=["red", "green", "orange"])
    st.pyplot(fig)

# ======================================================
# Footer
# ======================================================
st.markdown("---")
st.caption("🌍 Developed using WHO Air Quality Data • Machine Learning • Streamlit Dashboard")