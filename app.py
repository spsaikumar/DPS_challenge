import numpy as np
import pandas as pd
import pickle 
import streamlit as st
import json

regressor=pickle.load(open('src/model.pkl','rb'))
#regressor=pickle.load(pickle_a) # our model

def predict_chance(Category, Accident_type, Year, Month):
    #prediction=regressor.predict([[Category, Accident_type, Year, Month]]) #predictions using our model
    
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

    prediction=regressor.predict([[Category, Accident_type, Year, Month]]) #predictions using our model     


    return prediction[0] 


def main():
    st.title("Monthly figures for traffic accidents Value prediction APP using Random Forest model") #simple title for the app
    html_temp="""
        <div>
        <h2>Accident Value prediction APP</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    Category=st.selectbox('Category', ("Verkehrsunfälle","Alkoholunfälle","Fluchtunfälle"))
    Accident_type=st.selectbox('Accident_type',("insgesamt" ,"Verletzte und Getötete","mit Personenschäden"))
    data = st.text_input("Enter input data (Year and Month) in JSON format: ")
    try:
        data_dict = json.loads(data)
        # Category = data_dict['Category']
        # Accident_type = data_dict['Accident_type']
        Year = data_dict['year']
        Month = data_dict['month']
    except:
        st.warning("Invalid input format. Please enter a valid JSON object.")
        return
    result = predict_chance(Category, Accident_type, Year, Month) # result will be displayed
    output_dict = {"prediction": round(result)}
    st.json(output_dict)

if __name__=='__main__':
    main()
