import joblib 
import pandas as pd
import streamlit as st

model= joblib.load("E:/University (UTA)/First Sem/DATA 3401/Honors Contract/Used_Car_Price_Pipeline.pkl")

st.title("Used Car Price Prediction")


# User Input
milage= st.number_input("Enter the milage of your Car (in miles)")

choice_fuel_type= ['E85 Flex Fuel', 'Gasoline', 'Hybrid', 'Diesel', 'Plug-In Hybrid','not supported']
fule_type= st.selectbox("Select the fuel type of the car.", options=choice_fuel_type, index=None)

chocie_transmission_type= ['Automatic', 'Other', 'Manual', 'CVT']
transmission= st.selectbox("Select the mode of transmission of the car.", options=chocie_transmission_type, index=None)

choice_accident=['None reported', 'At least 1 accident or damage reported']
accident= st.selectbox('Any accident or damge reports of the car?', options=choice_accident, index=None)

choice_clean_title= ['Yes', 'No']
clean_title= st.selectbox('Does the car have clean title?', options=choice_clean_title)

horse_power= st.number_input("Enter the Horse Power (HP)")

engine_capacity= st.number_input("Enter the capacity of engine (in Liters)",step=1., format="%.2f")

cylinder_number= st.number_input("Number of cylinders in the car")

age= st.number_input("What is the age of your car? (Just Year)")




#Converting user inputs into data frame:
car= pd.DataFrame({
    'milage': [milage],
    'fuel_type': [fule_type],
    'transmission': [transmission],
    'accident': [accident],
    'clean_title': [{'Yes': True, 'No': False}[clean_title]],
    'horse_power': [horse_power],
    'engine_capacity': [engine_capacity],
    'cylinder_number': [cylinder_number],
    'age': [age]
})


#For Price Prediction
if (st.button('Predict')):
    if not milage or not fule_type or not transmission or not accident or not clean_title or not horse_power or not engine_capacity or not cylinder_number or not age:
        st.error(f"Opps! The Feature(s) can't be let empty.")
    else:
        prediction= model.predict(car)[0]
        st.success(f"Estimated Price of the Car: ${prediction:,.2f}")
