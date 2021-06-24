from bs4 import BeautifulSoup
import requests
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# import argparse

BILLBOARD_URL ="https://www.billboard.com/charts/hot-100"
SPOTIFY_ID = os.environ.get('SPOTIFY_ID')
SPOTIFY_KEY = os.environ.get('SPOTIFY_KEY')

date = input("enter the date(YYYY-MM-DD) for which you want the top 100 songs: ")

# date = "2021-06-06"

response = requests.get(f"{BILLBOARD_URL}/{date}")

soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())

songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")


songs_titles = [song.getText() for song in songs]
# print(songs_titles[0])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_KEY,
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]
# print(user_id)
# search_string = f"track:{songs_titles[0]} year:{date.split('-')[0]}"
#
# result = sp.search(search_string)
# pprint.pprint(result)

song_uris = []


for title in songs_titles:
    search_string = f"track:{title} year:{date.split('-')[0]}"
    try:
        result = sp.search(search_string)
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        continue

# pprint.pprint(song_uris)


# def get_args():
#     parser = argparse.ArgumentParser(description='Creates a playlist for user')
#     parser.add_argument('-p', '--playlist', required=True,
#                         help=f"{date} Billboard 100")
#     parser.add_argument('-d', '--description', required=False, default='',
#                         help='Top tracks on that day !!')
#     return parser.parse_args()
#
#
# args = get_args()


playlist_create = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
playlist_id = playlist_create["id"]

sp.playlist_add_items(playlist_id, song_uris)

print("Below is the link for your playlist:")
print(playlist_create['external_urls']['spotify'])


# pprint.pprint(sp.playlist(playlist_id))

# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])



