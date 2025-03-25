# 🏠 House Price Prediction - Machine Learning Project

Predict house prices using machine learning and deploy your model with Streamlit! This project walks you through building a robust house price prediction system, from data preprocessing to deploying a user-friendly web application.

![Streamlit Demo](https://img.shields.io/badge/Streamlit-Demo-FF4B4B?logo=streamlit) [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://house-price-predictions0.streamlit.app/)

## 📌 Project Overview
This project leverages the [Kaggle House Prices dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) to build a machine learning model for predicting residential home prices. The deployed Streamlit app allows users to input features and get instant price predictions.

## ✨ Features
- **Exploratory Data Analysis (EDA):** Visualize trends, correlations, and outliers.
- **Data Preprocessing:** Handle missing values, encode categorical variables, and scale features.
- **Model Training:** Test algorithms like Linear Regression, Decision Trees, and **XGBoost** (best-performing model).
- **Model Evaluation:** Metrics include MAE, MSE, RMSE, and R² score.
- **Streamlit Deployment:** Interactive web interface for real-time predictions.

## 🛠️ Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction

 2. **Install dependencies:**    
    ```bash
    pip install -r requirements.txt

 🚀 Usage 
1. Run the Streamlit app locally:

    ```bash
    streamlit run app.py

2. Access the app at http://localhost:8501 and input features to predict house prices.

   
Live Demo: [House Price Predictions App](https://house-price-predictions0.streamlit.app/)



📊 Dataset


The dataset contains 79 features describing residential homes in Ames, Iowa. Key steps include:


Handling missing data (e.g., LotFrontage, GarageYrBlt).


Encoding categorical variables (e.g., MSZoning, Neighborhood).


Feature engineering (e.g., creating TotalSF from 1stFlrSF + 2ndFlrSF).


Download the dataset from Kaggle.








🤖 Model Training


Algorithms Tested:


Linear Regression


Decision Tree Regressor


Random Forest Regressor


XGBoost Regressor (Final Model)



Evaluation Metrics
     
        Model-XGBoost
        
        MAE-12,500
        
        MSE-2.1e+08	
        
        R² Score-0.89
        
        

🌐 Deployment

The model is deployed using Streamlit, a framework for building ML apps quickly. Features of the app:

Input fields for key features (e.g., square footage, bedrooms, neighborhood).

Instant price prediction display.

Responsive UI for all devices.

---

### 🔍 Tips for Customization
1. Replace `yourusername` in the clone URL with your GitHub username.
2. Add screenshots of your EDA or Streamlit app under the Features section.
3. Update the Evaluation Metrics table with your model’s actual performance.
4. Include a `LICENSE` file if you choose a different license.
