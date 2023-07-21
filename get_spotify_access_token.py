import requests

# you can get your client id and secret at https://developer.spotify.com/dashboard

client_id = '<your_spotify_client_id>'
client_secret = '<your_spotify_client_secret>'

auth_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

auth_response = requests.post(auth_url, data=data)

access_token = auth_response.json().get('access_token')

print(access_token)