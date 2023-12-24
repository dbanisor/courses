from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import sys
import pprint

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri=REDIRECT_URI, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]


DATE = input("What year you would like to travel to? Type the date in this format: YYYY-MM-DD\n")
URL = f"https://www.billboard.com/charts/hot-100/{DATE}/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.select("li h3")
song_names = [song_titles[num].getText().strip() for num in range(0, 100)]


YEAR = DATE.split('-')[0]
all_songs = []
song_uris = []

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    for each_song in song_names:
        result = sp.search(q=f"track:{each_song} year:{YEAR}", type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{each_song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)

playlist_id = playlist['id']

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)






