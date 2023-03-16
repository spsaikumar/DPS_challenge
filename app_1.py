import numpy as np
import pandas as pd
import pickle 
import streamlit as st
from streamlit.server import Server

regressor = pickle.load(open('src/model.pkl','rb'))

def predict_chance(Category, Accident_type, Year, Month):
    # Pre-processing user input    
    if Category == "Verkehrsunfälle":
        Category = 0
    elif Category == "Alkoholunfälle":
        Category = 1
    elif Category == "Fluchtunfälle":
        Category = 2

    if Accident_type == "insgesamt":
        Accident_type = 0
    elif Accident_type == "Verletzte und Getötete":
        Accident_type = 1
    elif Accident_type == "mit Personenschäden":
        Accident_type = 2   

    prediction = regressor.predict([[Category, Accident_type, Year, Month]])
    return int(prediction[0])

def app():
    st.set_page_config(layout="wide")
    st.title("Accident Value prediction APP using ML")

    input_json = st.text_input("Input JSON", value='{"year":2020, "month":10}')

    if st.button("Predict"):
        input_dict = json.loads(input_json)
        year = input_dict["year"]
        month = input_dict["month"]
        prediction = predict_chance("Verkehrsunfälle", "insgesamt", year, month)
        output_json = json.dumps({"prediction": prediction})
        st.write(output_json)

if __name__ == "__main__":
    server = Server()
    server.start(app)
