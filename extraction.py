import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint,billboard,json,requests,re
import pickle

client_credentials_manager = SpotifyClientCredentials("b0dd29c37009465aaac3e5f6d87460f7","af33faec768c4335b2ddefe36d8b2cd9")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

def obtain_audio_data():
	chart = billboard.ChartData("dance-electronic-songs")
	songs=[]
	for song in chart:
		song_title=song.title.replace(" ","%20")
		songs.append(song_title)


	songs_ids=[]

	for song in songs:
		R=requests.get("https://api.spotify.com/v1/search?q="+song+"&type=track&limit=1")
		Resp_str=R.text.encode("utf-8")
		M=re.search("https:\/\/open\.spotify\.com\/track\/(.*)",Resp_str)
		ID=M.groups()[0][0:len(M.groups()[0])-1]
		songs_ids.append(ID)

	Audio_Features=sp.audio_features(songs_ids)
	
	Data_Dict={}

	for i in range(len(songs)):
		Data_Dict[songs[i].replace("%20"," ")]=Audio_Features[i]
	Data=open("md.txt","ab+")
	pickle.dump(Data_Dict,Data)
	Data.close()

obtain_audio_data()