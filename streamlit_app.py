import requests

BREVO_API_KEY = 'your_actual_brevo_api_key'
BREVO_API_URL = 'https://api.brevo.com/v3/smtp/email'

headers = {
    'accept': 'application/json',
    'api-key': BREVO_API_KEY,
    'content-type': 'application/json'
}

response = requests.get(BREVO_API_URL, headers=headers)
print(response.status_code)
print(response.json() 
