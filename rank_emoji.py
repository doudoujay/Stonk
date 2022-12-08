import pandas as pd
import numpy as np
path = '700077347251945472_sentiment.parquet'
df = pd.read_parquet(
   path, 
   engine='auto', 
   columns=None, 
   storage_options=None, 
   use_nullable_dtypes=False
)
# Collect all emoji snd store into array
emoji_all = []
t = df.loc[: ,'reactions']
for row in t:
          for reaction in row:
                    if reaction['emoji']['name'] not in emoji_all:
                              emoji_all.append(reaction['emoji']['name'])

#transfer reaction of each post to 1d array and store into a new column.
#index of array : emoji.  value of array : count
rank_emoji = np.zeros(shape = ( len(t), len(emoji_all) ), dtype = np.uint8)
print("transfer reaction into new column...............")
for i in range(len(t)):
          row = t[i]
          for reaction in row:
                    index = emoji_all.index(reaction['emoji']['name'])
                    rank_emoji[i][index] = reaction['count']
df.insert(12, "Emoji_Rank", rank_emoji.tolist(), True)
print(df.loc[492460:492465, 'Emoji_Rank'])          

#write to pickle file
print("Wrting to picle file.............")
df.to_pickle("emoji_rank.pkl")
print("Done!")