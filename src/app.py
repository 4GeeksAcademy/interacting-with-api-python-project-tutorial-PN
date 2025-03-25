import os
import spotipy
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyOAuth

# load the .env file variables
load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


modest_mouse = 'spotify:artist:1yAwtBaoHLEDWAnWR87hBT'


results = spotify.artist_top_tracks(modest_mouse)

# print(results['tracks'][0])
tracks_data = []

for track in results['tracks'][:10]:
    name = track['name']
    popularity = track['popularity']
    duration = track['duration_ms']
    duration = duration/60000
    tracks_data.append({"name": name, "popularity": popularity, "duration": duration})

df = pd.DataFrame(tracks_data)

print(df)

scatter_plot = sns.scatterplot(data = df, x = "popularity", y = "duration")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")