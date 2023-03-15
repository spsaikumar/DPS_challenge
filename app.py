import numpy as np
import pandas as pd
import pickle 
import streamlit as st

regressor=pickle.load(open('src/model/model_dt.pkl','rb'))
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


    return prediction 


def main():
    st.title("Accident Value prediction APP using ML") #simple title for the app
    html_temp="""
        <div>
        <h2>Accident Value prediction APP</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    Category=st.selectbox('Category', ("Verkehrsunfälle","Alkoholunfälle","Fluchtunfälle"))
    Accident_type=st.selectbox('Accident_type',("insgesamt" ,"Verletzte und Getötete","mit Personenschäden"))
    Year=st.text_input("Year")
    Month=st.text_input("Month") #giving inputs as used in building the model
    result=""
    if st.button("Predict"):
        result=predict_chance(Category,Accident_type,Year,Month) #result will be displayed if button is pressed
    st.success("The  Number of accidents are  {} ".format(result))
        
if __name__=='__main__':
    main()