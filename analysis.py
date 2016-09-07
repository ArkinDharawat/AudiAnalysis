import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

Data=open("md.txt","rb")
track_analysis=pickle.load(Data)
Data.close()
#print track_analysis[(track_analysis.keys()[0])]

Audiodata={}
Audiodata["tracks"]=track_analysis.keys()

Attributes=[u'energy', u'liveness', u'tempo',u'speechiness', u'acousticness', u'danceability', u'time_signature', u'duration_ms', u'loudness',u'valence',u'instrumentalness']

for a in Attributes:
	Audiodata[a]=[]
	for key in track_analysis.keys():
		Audiodata[a].append(float(track_analysis[key][a]))

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Audiodata["energy"],Audiodata["loudness"],Audiodata["speechiness"])
ax.set_xlabel('energy')
ax.set_ylabel('loudness')
ax.set_zlabel('speechiness')
"""

for i in range(len(Attributes)):
	for j in range(i+1,len(Attributes)):
		plt.figure().add_subplot(111)
		plt.plot(Audiodata[Attributes[i]],Audiodata[Attributes[j]],"ro")
		plt.xlabel(Attributes[i])
		plt.ylabel(Attributes[j])

plt.show()