import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

import warnings
warnings.filterwarnings('ignore')

dataset_path = r'https://storage.googleapis.com/dataset_traffic_accidents_dps/Monatszahlen_Verkehrsunf%C3%A4lle.csv'
# dataset_path = r'../data/raw/Monatszahlen_Verkehrsunfälle.csv'

df = pd.read_csv(dataset_path)
# Process the data
data = df.iloc[:, :5].copy()

data_2020 = data[data["JAHR"]<=2020].reset_index(drop=True)
data_2020.rename(columns={"MONATSZAHL":"Category","AUSPRÄGUNG":"Accident_type","JAHR":"Year","MONAT":"Month","WERT":"Value"}, inplace=True)

data_2020.drop(data_2020[data_2020["Month"]=="Summe"].index,inplace=True)

data_2020['Month'] = pd.to_numeric(data_2020['Month'].astype(str).str[-2:], errors='coerce')

# Categorical features to encode using one hot encoding 
features = ['Category','Accident_type','Year','Month']

# setting input features X and target y 
X = data_2020[features]  # here features are selected from 'object' datatype
y = data_2020['Value']

#category column encoding
cat_mapping = {'Verkehrsunfälle': 0,
                'Alkoholunfälle':1 ,
                'Fluchtunfälle': 2}
X['Category'] = X['Category'].map(cat_mapping)

#Accident_type column mapping

accid_mapping = {'insgesamt': 0,
                'Verletzte und Getötete':1 ,
                'mit Personenschäden': 2}
X['Accident_type'] = X['Accident_type'].map(accid_mapping)
le = LabelEncoder()
X['Year'] = le.fit_transform(X['Year'])
X['Month'] = le.fit_transform(X['Month'])


# train and test split and building baseline model to predict target features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Random Forest Regressor model
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# Save the model
import pathlib
filename = 'model.pkl'
with open(filename, 'wb') as f:
  pickle.dump(rf_model, f)
pickle.dump(rf_model, open(filename, 'wb'))

# regressor=pickle.load(open('model.pkl','rb'))


