from flask import Flask, request, jsonify
import pickle
import pandas as pd
from prophet import Prophet

# load the trained model from the saved file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# define the Flask app
app = Flask(__name__)

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
