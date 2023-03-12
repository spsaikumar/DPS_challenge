# This will be replaced with your bucket name after running the `sed` command in the tutorial
# BUCKET = "gs://neat-domain-341912-bucket"

import glob
import sys
import logging
import pickle
from google.cloud import storage
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prophet import Prophet

logging.getLogger('cmdstanpy').setLevel(logging.WARNING)

#need to read paramters from CONFIG.ini

def get_data_preprocess():
    """  
    
    """
    file_path = r'C:\Users\pavan\OneDrive\Desktop\Projects\DPS_challenge\data\raw\Monatszahlen_Verkehrsunfälle.csv'
    df = pd.read_csv(file_path)
    # Process the data
    data = df.iloc[:, :5].copy()

    # Save the processed data to the processed_data folder
    # processed_path_dir = r'C:\Users\pavan\OneDrive\Desktop\Projects\DPS_challenge\data\processed'
    # data.to_csv(processed_path_dir, index=False)

    # check for non-numeric values
    numeric_cols = ['JAHR', 'MONAT', 'WERT']
    for col in numeric_cols:
        # replace Non-numeric value and empty values with NaN
        # data[col] = pd.to_numeric(data[col], downcast="integer", errors='coerce').astype('Int64') # to avoid creating copy of it/ new dataframe
        data.loc[:, col] = pd.to_numeric(data[col],downcast="integer", errors='coerce').astype('Int64')   #modifying the original DataFrame and not a copy of it.

    # drop rows with missing values in the numeric columns
    data = data.dropna(subset=numeric_cols).reset_index(drop=True)


    data['MONAT'] = pd.to_datetime(data['MONAT'], format='%Y%m').dt.month

    # filter the data for the desired category, type, and year
    data_filtered = data[(data['MONATSZAHL'] == 'Alkoholunfälle') & (data['AUSPRÄGUNG'] == 'insgesamt') & (data['JAHR'] <= 2020)]

    # Aggregate the values for each month for the above filter using groupby and sum
    monthly_values = data_filtered.groupby(['JAHR', 'MONAT'])['WERT'].sum().reset_index()

    # rename the columns to work with Prophet
    monthly_values.rename(columns={'JAHR': 'year', 'MONAT': 'month', 'WERT': 'y'}, inplace=True)
    monthly_values['ds'] = pd.to_datetime(monthly_values['year'].astype(str) + monthly_values['month'].astype(str), format='%Y%m' )
    return monthly_values

def generate_futute_data():
    
    """
    
    """
    monthly_values = get_data_preprocess()
    # create a Prophet model and fit it to the data
    model = Prophet( weekly_seasonality=True,daily_seasonality=True )
    model = Prophet()

    model.fit(monthly_values[['ds', 'y']])
    # print(dict(model))

    # create a dataframe with the dates for which we want to forecast the values
    future_dates = model.make_future_dataframe(periods=1, freq='MS', include_history=False)

    # get the forecasted values
    forecast = model.predict(future_dates)

    # get the forecasted value for the given year and month
    forecasted_value = forecast[(forecast['ds'].dt.year == 2021) & (forecast['ds'].dt.month == 1)]['yhat'].values[0]

    return str(forecasted_value)


# print('The forecasted number of accidents for Alkoholunfälle (insgesamt) in January 2021 is:', round(forecasted_value,3))

# artifact_filename_lr = 'model.pkl'
# # save the model as a pickle file
# # Save model artifact to local filesystem (doesn't persist)
# local_path = artifact_filename_lr
# with open(local_path, 'wb') as f:
#   pickle.dump(model, f)

# Upload model artifact to Cloud Storage
# model_directory = os.environ['AIP_MODEL_DIR']
# storage_path = os.path.join(model_directory, artifact_filename_lr)
# blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
# blob.upload_from_filename(local_path)

from flask import Flask

app = Flask(__name__)


@app.route('/future')
def model():
    return generate_futute_data()
