# Air Quality Prediction System

A machine learning–based air quality prediction and analysis system developed using WHO air quality data. This project was completed as part of a **CELEBAL Technologies Virtual Internship** during the 7th semester of B.Tech (CSE).

The goal of the project is to analyze air quality indicators and predict pollution levels using multiple machine learning models, followed by deployment through a simple Streamlit web interface.

---

## Project Type

**Academic Group Project (Virtual Internship)**

---

## My Contribution

* Performed data cleaning, preprocessing, and exploratory data analysis (EDA)
* Trained and evaluated multiple machine learning models
* Compared model performance using R² Score, MAE, and RMSE metrics
* Selected and saved the best-performing model for deployment
* Assisted in integrating the trained model with the Streamlit application

---

## Features

* Data preprocessing and feature analysis
* Multiple ML model comparison
* Model performance evaluation
* Interactive Streamlit-based UI for predictions
* Saved trained model using pickle

---

## Machine Learning Models Used

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Streamlit

---

## Project Structure

```
CELEBAL-TECHNOLOGIES/
│── AirQualityPrediction.ipynb
│── streamlit_app.py
│── model.pkl
│── requirements.txt
│── README.md
```

---

## How to Run the Project Locally

1. Clone the repository

```bash
git clone https://github.com/Ayush-Kumar-25/Celebal_Technologies_Internship_Project.git
```

2. Navigate to the project directory

```bash
cd Celebal_Technologies_Internship_Project
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

The application will be available at `http://localhost:8501/`.

---

## Dataset

* WHO Air Quality Dataset
* Dataset was used strictly for academic and learning purposes

---

## Notes

* This project was developed for learning and internship evaluation purposes
* It does not represent a production-grade system
* Future improvements may include real-time data ingestion and advanced model optimization

---

## License

This project is licensed under the **MIT License**.
