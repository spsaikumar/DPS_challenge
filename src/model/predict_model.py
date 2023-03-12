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