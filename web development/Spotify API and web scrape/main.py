import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# base url for billboard website
load_dotenv()

# Get environment variables
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")

URL = "https://www.billboard.com/charts/hot-100/"

# find year from input
year = input("what year would you like to travel too? Type in the format YYYY-MM-DD")

# concatenate year and url
year_url = f'{URL}{year}'

# init header
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
# obtain all html from website
text = requests.get(year_url, headers= header).text



# parse and find all titles
soup = BeautifulSoup(text, "html.parser")
titles =soup.select("li ul li h3")


song_titles = [title.get_text(strip=True) for title in titles]




# Initialize the Spotipy client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        redirect_uri='http://example.org',  # Your redirect URI
        scope="playlist-modify-private",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    ),requests_timeout=10, retries=10
)

# Get current user's ID
user_id = sp.current_user()["id"]


song_uris = []
year = year.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    
print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("complete")