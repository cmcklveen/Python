import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    'Content-Type': 'applicaton/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write python script for Hello World",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {str(response.status_code)}")