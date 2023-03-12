#importing libaries
import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
# from prophet import Prophet
# from fbprophet import Prophet
import warnings
warnings.filterwarnings('ignore')
import logging
logging.getLogger('cmdstanpy').setLevel(logging.WARNING)
logging.getLogger('fbprophet').setLevel(logging.ERROR)

# path_dir = '..\..\data\raw\Monatszahlen_Verkehrsunfälle.csv'
path_dir = r'C:\Users\pavan\OneDrive\Desktop\Projects\DPS_challenge\data\raw\Monatszahlen_Verkehrsunfälle.csv'
# path_dir = 'data\raw\Monatszahlen_Verkehrsunfälle.csv'


df = pd.read_csv(path_dir)
# Process the data
data = df.iloc[:, :5].copy()

# Save the processed data to the processed_data folder
# processed_path_dir = r'C:\Users\pavan\OneDrive\Desktop\Projects\DPS_challenge\data\processed'
# data.to_csv(processed_path_dir, index=False)

# check for non-numeric values
numeric_cols = ['JAHR', 'MONAT', 'WERT']
for col in numeric_cols:
    print(col)
    # replace Non-numeric value and empty values with NaN
    # data[col] = pd.to_numeric(data[col], downcast="integer", errors='coerce').astype('Int64') # to avoid creating copy of it/ new dataframe
    data.loc[:, col] = pd.to_numeric(data[col],downcast="integer", errors='coerce').astype('Int64')   #modifying the original DataFrame and not a copy of it.

# drop rows with missing values in the numeric columns
data = data.dropna(subset=numeric_cols).reset_index(drop=True)


data['MONAT'] = pd.to_datetime(data['MONAT'], format='%Y%m').dt.month



import warnings
warnings.filterwarnings('ignore')
import logging
logging.getLogger('cmdstanpy').setLevel(logging.WARNING)
logging.getLogger('fbprophet').setLevel(logging.ERROR)
# filter the data for the desired category, type, and year
data_filtered = data[(data['MONATSZAHL'] == 'Alkoholunfälle') & (data['AUSPRÄGUNG'] == 'insgesamt') & (data['JAHR'] <= 2020)]

# Aggregate the values for each month for the above filter using groupby and sum
monthly_values = data_filtered.groupby(['JAHR', 'MONAT'])['WERT'].sum().reset_index()

# rename the columns to work with Prophet
monthly_values.rename(columns={'JAHR': 'year', 'MONAT': 'month', 'WERT': 'y'}, inplace=True)
monthly_values['ds'] = pd.to_datetime(monthly_values['year'].astype(str) + monthly_values['month'].astype(str), format='%Y%m' )
from prophet import Prophet

# create a Prophet model and fit it to the data
# model = Prophet( weekly_seasonality=True,daily_seasonality=True )
model = Prophet()

model.fit(monthly_values[['ds', 'y']])


