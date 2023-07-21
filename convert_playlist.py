import requests
import json

from youtubesearchpython import VideosSearch

def convert_spotify_to_youtube(playlist_url, spotify_access_token):
    # Get the playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]
    print(playlist_id)

    # Make a request to the Spotify API to get the playlist details
    spotify_api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        'Authorization': 'Bearer {}'.format(spotify_access_token)
    }
    response = requests.get(spotify_api_url, headers=headers)
    if response.status_code == 200:
        playlist_data = response.json()
        # Rest of the code
    else:
        # Handle the case when the request is not successful
        print("Error: Failed to retrieve playlist data from Spotify API")
        print(response.content)
        playlist_data = {}

    # print(playlist_data)

    # Extract the track names and artists from the playlist data
    tracks = playlist_data['tracks']['items']
    track_names = []
    artists = []

    # Search for the corresponding YouTube videos
    youtube_playlist = []
    for track in tracks:
        track_name = track['track']['name']
        artist = track['track']['artists'][0]['name']
        query = f"{track_name} {artist}"
        videosSearch = VideosSearch(query, limit = 1)
        result = videosSearch.result()
        if result['result']:
            video_id = result['result'][0]['id']
            youtube_playlist.append(video_id)
            track_names.append(track_name)
            artists.append(artist)
        else:
            # Handle the case when no search results are found
            print(f"Error: No search results found on YouTube for {query}") 
    # Return the YouTube playlist
    return youtube_playlist, track_names, artists
