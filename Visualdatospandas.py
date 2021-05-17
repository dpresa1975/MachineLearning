import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import numpy as np

artists_billboard = pd.read_csv("artists_billboard.csv")
print(artists_billboard.columns)
print(artists_billboard["durationSeg"])
print(artists_billboard["genre"])
artists_redux=artists_billboard.drop(["id","mood","tempo","artist_type","anioNacimiento"],axis=1)

print(artists_redux.columns)

#artists_redux[['genre','durationSeg']].plot.hist(bins=5,alpha=0.5)
#artists_redux.set_index('genre')['durationSeg'].plot(kind='bar');
artists_genre=artists_redux[['genre','durationSeg']].groupby(['genre'], as_index=False).agg(['mean'])#, 'count', 'sum'])

#plt.plot(artists_genre['genre'],artists_genre['mean'])
#sb.factorplot(artists_genre)
#sb.factorplot('durationSeg',data=artists_redux,kind="count", aspect=3)
#artists_genre.set_index('genre')['durationSeg'].plot.hist(bins=5,alpha=0.5)
plt.plot(artists_genre)
#plt.bar(artists_genre, artists_genre,color ='maroon',width = 0.4)
#artists_genre.plot.hist(bins=5,alpha=0.5)
#artists_genre.set_index('genre')[artists_genre.mean].plot.pie()
plt.show()
print(type(artists_genre))