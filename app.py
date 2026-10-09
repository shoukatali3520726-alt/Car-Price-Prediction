import streamlit as st
import pandas as pd
import pickle

with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)
 
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

 
st.title("🚗 Car Price Prediction By Shoukat Ali")
st.write("Enter your car detail to predict price.")
 
model_name = st.selectbox("Car Model", label_encoders["model"].classes_)
year = st.number_input("Year", min_value=1996, max_value=2024, value=2018)
transmission = st.selectbox("Transmission", label_encoders["transmission"].classes_)
mileage = st.number_input("Mileage", min_value=0, max_value=200000, value=15000)
fuelType = st.selectbox("Fuel Type", label_encoders["fuelType"].classes_)
tax = st.number_input("Tax", min_value=0, max_value=600, value=150)
mpg = st.number_input("MPG (Miles per Gallon)", min_value=0.0, max_value=250.0, value=55.0)
engineSize = st.number_input("Engine Size", min_value=0.0, max_value=6.0, value=1.2)
 
if st.button("Predict Price"):
 
    input_data = pd.DataFrame({
        "model": [label_encoders["model"].transform([model_name])[0]],
        "year": [year],
        "transmission": [label_encoders["transmission"].transform([transmission])[0]],
        "mileage": [mileage],
        "fuelType": [label_encoders["fuelType"].transform([fuelType])[0]],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize],
    })
 
    predicted_price = model.predict(input_data)[0]
 
    st.success(f"Predicted Price: £{predicted_price:,.2f}")