import pandas as pd
import streamlit as st
import joblib 


model = joblib.load('xgb_model.jb')

st.title("House Price Prediction")
st.write("Enter the Details Below to predict the house price")

inputs=['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
       'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
       'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
       'CentralAir']

input_data = {}
for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(f"{feature}", options={'Yes','No'}, index=0)
    else:
        input_data[feature] = st.number_input(
            f"{feature}", value=0.0, step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.1
        )
if st.button("Predict Price"):
    input_data['CentralAir'] = 1 if input_data['CentralAir']=='Yes' else 0
    input_df = pd.DataFrame([input_data], columns=inputs)
    predictions = model.predict(input_df)
    st.success(f"Predicted House Price: ${predictions[0]:,.2f}")
        
