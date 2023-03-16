import requests
import json

# Define the URL
url = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge'

# Define the JSON data
data = {
    'github': 'https://github.com/ACCOUNT/REPO', #https://github.com/spsaikumar/DPS_challenge
    'email': 'EMAIL', #corework.singavarapu@gmail.com
    'url': 'DEPLOYED_ENDPOINT',  #https://spsaikumar-dps-challenge-app-swrm06.streamlit.app/
    'notes': 'NOTES' # Not mandatory 
}

# Set the headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response status code and message
print(f"Status {response.status_code} {response.reason}")
print(response.json())
