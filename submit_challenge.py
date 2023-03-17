import requests
import json

# Define the URL
url = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge'

# Define the JSON data
data = {
    "github": "https://github.com/spsaikumar/DPS_challenge",
    "email": "corework.singavarapu@gmail.com", 
    "url": "https://spsaikumar-dps-challenge-app-swrm06.streamlit.app/", 
    "notes": "I apologize for the delay in completing the task. I was sick and had pending exams and seminar deadlines. I am working to complete it. Thank you for your understanding. I am looking forward to see you for next round,interviewer call"
}

# Set the headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response status code and message
print(f"Status {response.status_code} {response.reason}")
print(response.json())
