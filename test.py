import requests
import json

API_KEY = 'add your api key'
your_query = "What is Machine Learning"  # Replace this with your actual query payload

url = 'https://payload.vextapp.com/hook/NL2933PKUA/catch/$(channel_token)'
headers = {
    'Content-Type': 'application/json',
    'Apikey': 'Api-Key ' + API_KEY
}
payload = {
    'payload': your_query
}

response = requests.post(url, headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    print("Request successful.")
    print(response.json())  # Print the response JSON
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)  # Print the error message
