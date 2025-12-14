# Air Quality Prediction & Analysis

A machine learning–based project developed during the **CELEBAL Technologies Virtual Internship (1 month)**. The project analyzes WHO air quality data, trains multiple regression models, and provides an interactive **Streamlit dashboard** for prediction and visualization of air pollution metrics.

---

## Project Type

Academic Group Project (Virtual Internship)

## Internship Details

* **Organization:** CELEBAL Technologies
* **Duration:** 1 Month
* **Semester:** 7th Semester (B.Tech – CSE)

## My Role

* Data preprocessing and cleaning
* Feature selection and encoding
* Training and evaluating machine learning models
* Model comparison and best-model selection
* Saving trained models for deployment

> **Note:** This was a collaborative internship project. The repository documents my technical contribution and learning outcomes.

---

## Problem Statement

To analyze global air quality data and predict pollution levels using machine learning models, while also providing meaningful visual insights and an easy-to-use prediction interface.

---

## Dataset

* **Source:** WHO Air Quality Dataset
* **Format:** Excel (`AirQuality.xlsx`)
* **Key Features:**

  * PM2.5 (μg/m³)
  * PM10 (μg/m³)
  * NO₂ (μg/m³)
  * WHO Region
  * Country and City
  * Measurement Year

---

## Data Processing

* Removed unnecessary and low-coverage columns
* Handled missing values using mean, forward-fill, and backward-fill strategies
* Outlier removal using IQR method (PM2.5)
* Label encoding for categorical features
* Feature scaling using `StandardScaler`

---

## Machine Learning Models Used

The following regression models were trained and evaluated:

* Linear Regression
* Polynomial Regression (Degree 2)
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

### Evaluation Metrics

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

The best-performing model was selected based on **lowest RMSE** and saved for deployment.

---

## Visualization & Analysis

* Distribution plots for PM2.5, PM10, and NO₂
* Box plots for outlier detection
* Bar charts for WHO region-wise pollution levels
* Correlation heatmap for numeric features
* Pollution index comparison across regions

---

## Streamlit Dashboard

An interactive dashboard was built using **Streamlit** that allows users to:

* Predict PM2.5 levels based on user inputs
* View pollution category and pollution index
* Upload custom datasets (CSV / Excel)
* Perform exploratory data analysis and visualizations

### Dashboard Features

* Real-time prediction
* Pollution category classification
* Interactive charts and heatmaps
* File upload and analysis support

---

## Project Structure

```text
CELEBAL-TECHNOLOGIES/
│
├── AirQualityPrediction.ipynb   # Model training & analysis notebook
├── streamlit_app.py             # Streamlit dashboard
├── AirQuality.xlsx              # Dataset
├── best_model.pkl               # Saved ML model
├── scaler.pkl                   # Feature scaler
├── README.md
```

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit openpyxl
```

### 4. Run Streamlit App

```bash
streamlit run streamlit_app.py
```

The application will run at:

```
http://localhost:8501
```

---

## Learning Outcomes

* End-to-end machine learning workflow
* Feature engineering and model evaluation
* Model persistence using pickle
* Building ML-powered dashboards using Streamlit
* Working with real-world air quality datasets

---

## License

This project was developed as part of an academic internship. The license and usage follow internship and educational guidelines.


