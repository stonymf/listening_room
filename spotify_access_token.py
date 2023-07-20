import requests

client_id = '9f8b5e8f458e4a9c9bf0be9a441d5f78'
client_secret = 'b1c0b21e45a2455f9f317a4502c84c33'

auth_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

auth_response = requests.post(auth_url, data=data)

access_token = auth_response.json().get('access_token')