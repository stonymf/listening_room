import requests
import json

def convert_spotify_to_youtube(playlist_url):
    # Get the playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]

    # Make a request to the Spotify API to get the playlist details
    spotify_api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        "Authorization": "Bearer YOUR_SPOTIFY_ACCESS_TOKEN"
    }
    response = requests.get(spotify_api_url, headers=headers)
    playlist_data = response.json()

    # Extract the track names and artists from the playlist data
    tracks = playlist_data['tracks']['items']
    track_names = [track['track']['name'] for track in tracks]
    artists = [track['track']['artists'][0]['name'] for track in tracks]

    # Search for the corresponding YouTube videos
    youtube_playlist = []
    for i in range(len(tracks)):
        query = f"{track_names[i]} {artists[i]} official music video"
        youtube_api_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key=YOUR_YOUTUBE_API_KEY"
        response = requests.get(youtube_api_url)
        search_results = response.json()
        video_id = search_results['items'][0]['id']['videoId']
        youtube_playlist.append(video_id)

    # Return the YouTube playlist
    return youtube_playlist

# Example usage
spotify_playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
youtube_playlist = convert_spotify_to_youtube(spotify_playlist_url)
print(youtube_playlist)
