# from google.cloud import aiplatform

# endpoint = aiplatform.Endpoint(
#     endpoint_name="projects/630236181889/locations/us-central1/endpoints/4518561781601271808"
# )

# # A test example we'll send to our model for prediction
# test_mpg = test_mpg = [1, 2, 3, 2, -2, -1, -2, -1, 0]


# response = endpoint.predict([test_mpg])

# print('API response: ', response)

# print('Predicted MPG: ', response.predictions[0][0])



# create a dataframe with the dates for which we want to forecast the values
future_dates = model.make_future_dataframe(periods=1, freq='MS', include_history=False)

# get the forecasted values
forecast = model.predict(future_dates)

# get the forecasted value for the given year and month
forecasted_value = forecast[(forecast['ds'].dt.year == 2021) & (forecast['ds'].dt.month == 1)]['yhat'].values[0]

print('The forecasted number of accidents for Alkoholunfälle (insgesamt) in January 2021 is:', round(forecasted_value,3))

import pickle
import pandas as pd
from flask import Flask, jsonify, request
# define the Flask app
app = Flask(__name__)

# @app.route('/future')
# def model():
#     return generate_futute_data()

# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
# define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # parse the input JSON data
    data = request.json
    year = data['year']
    month = data['month']

    # create a dataframe with the input date
    input_date = pd.to_datetime(str(year) + '-' + str(month), format='%Y-%m')
    input_data = pd.DataFrame({'ds': [input_date]})

    # make the prediction using the trained model
    forecast = model.predict(input_data)

    # extract the predicted value
    prediction = forecast['yhat'].values[0]

    # return the prediction as a JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)