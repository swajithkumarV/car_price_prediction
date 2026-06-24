import numpy as np
import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

st.header("Car Price Prediction ML Model")

car_dataset = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

car_dataset['name'] = car_dataset['name'].apply(get_brand_name)

name = st.selectbox(
    "Select the Car Name",
    car_dataset['name'].unique()
)

year = st.slider(
    "Select the Year",
    int(car_dataset['year'].min()),
    int(car_dataset['year'].max()),
    step=1
)

km_driven = st.slider(
    "Select the Kms Driven",
    1,
    200000
)

fuel = st.selectbox(
    "Select the Fuel Type",
    car_dataset['fuel'].unique()
)

seller_type = st.selectbox(
    "Select the Seller Type",
    car_dataset['seller_type'].unique()
)

transmission = st.selectbox(
    "Select the Transmission Type",
    car_dataset['transmission'].unique()
)
owner = st.selectbox(
    "Select the Owner Type",
    car_dataset['owner'].unique())


mileage = st.slider('car mileage',10,40)
engine = st.slider(
    'car engine', 500, 5000
)
max_power = st.slider(  
    'car max power', 50, 500
)
seats = st.slider(
    'car seats', 2, 10
)   

if st.button("Predict Price"):

    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type,
          transmission, owner, mileage, engine,
          max_power, seats]],
        columns=[
            'name', 'year', 'km_driven', 'fuel',
            'seller_type', 'transmission', 'owner',
            'mileage', 'engine', 'max_power', 'seats'
        ]
    )

    # Fuel Encoding
    input_data_model['fuel'].replace(
        ['Diesel', 'Petrol', 'LPG', 'CNG'],
        [1, 2, 3, 4],
        inplace=True
    )

    # Seller Type Encoding
    input_data_model['seller_type'].replace(
        ['Individual', 'Dealer', 'Trustmark Dealer'],
        [1, 2, 3],
        inplace=True
    )

    # Transmission Encoding
    input_data_model['transmission'].replace(
        ['Manual', 'Automatic'],
        [1, 2],
        inplace=True
    )

    # Owner Encoding
    input_data_model['owner'].replace(
        ['First Owner', 'Second Owner', 'Third Owner',
         'Fourth & Above Owner', 'Test Drive Car'],
        [1, 2, 3, 4, 5],
        inplace=True
    )

    # Brand Encoding
    input_data_model['name'].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota',
         'Ford', 'Renault', 'Mahindra', 'Tata',
         'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
         'Mitsubishi', 'Audi', 'Volkswagen', 'BMW',
         'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG',
         'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
         'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
        list(range(1, 32)),
        inplace=True
    )

    st.write("Encoded Input Data")
    st.dataframe(input_data_model)

    car_price = model.predict(input_data_model)

    st.success(f"Predicted Car Price: ₹ {car_price[0]:,.0f}")