# app.py
from convert_playlist import convert_spotify_to_youtube

def main():
    spotify_playlist_url = "https://open.spotify.com/playlist/1AtALs0N6vfbcWWk6QBW65"
    youtube_playlist, track_names, artists = convert_spotify_to_youtube(spotify_playlist_url)

    # Generate the HTML page
    html = f"""
<!DOCTYPE html>
<html>
<body>
    <div id="player"></div>
    <ul id="playlist"></ul>

    <script>
    // Load the IFrame Player API code asynchronously.
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    var playlist = {youtube_playlist};
    var trackNames = {track_names};
    var artists = {artists};
    var player;
    var currentVideoIndex = 0;

    function onYouTubeIframeAPIReady() {{
        player = new YT.Player('player', {{
        height: '390',
        width: '640',
        videoId: playlist[currentVideoIndex],
        events: {{
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange,
            'onError': onPlayerError
        }}
        }});

        // Create the playlist element
        var playlistElement = document.getElementById('playlist');
        for (var i = 0; i < playlist.length; i++) {{
        var listItem = document.createElement('li');
        listItem.textContent = trackNames[i] + ' - ' + artists[i];
        listItem.id = 'track-' + i;
        listItem.onclick = (function(index) {{
            return function() {{ skipToTrack(index); }};
        }})(i);
        playlistElement.appendChild(listItem);
        }}

        // Highlight the current track
        document.getElementById('track-' + currentVideoIndex).style.fontWeight = 'bold';
    }}

    function onPlayerReady(event) {{
        event.target.playVideo();
    }}

    function onPlayerError(event) {{
        // If an error occurs, skip to the next video
        nextVideo();
    }}

    function nextVideo() {{
        // Unhighlight the current track
        document.getElementById('track-' + currentVideoIndex).style.fontWeight = 'normal';

        currentVideoIndex++;
        if (currentVideoIndex < playlist.length) {{
            player.loadVideoById(playlist[currentVideoIndex]);

            // Highlight the new current track
            document.getElementById('track-' + currentVideoIndex).style.fontWeight = 'bold';
        }}
    }}

    function skipToTrack(index) {{
        // Unhighlight the current track
        document.getElementById('track-' + currentVideoIndex).style.fontWeight = 'normal';

        currentVideoIndex = index;
        player.loadVideoById(playlist[currentVideoIndex]);

        // Highlight the new current track
        document.getElementById('track-' + currentVideoIndex).style.fontWeight = 'bold';
    }}

    function onPlayerStateChange(event) {{
        // When the video has ended
        if (event.data == YT.PlayerState.ENDED) {{
            nextVideo();
        }}
    }}
    </script>
</body>
</html>
"""
    # Write the HTML page to a file
    with open('player.html', 'w') as f:
        f.write(html)

if __name__ == '__main__':
    main()