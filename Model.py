#Importing Library
import numpy as np 
import pandas as pd 

# Dataset from importing
anime = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Django project Anime Recommendation System/anime.csv')


#Data Cleaning
anime = anime[['anime_id','name','genre','type']]
anime['genre']=anime['genre'].fillna("")
anime['type']=anime['type'].fillna("")
anime['genre'] = anime['genre'].apply(lambda x:x.split())
anime['type'] = anime['type'].apply(lambda x:x.split())
anime['tags'] = anime['genre']+anime['type']
anime['Anime_name']=anime['name']
new_df=anime[['anime_id','Anime_name','tags']]
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.head()

#####Imporint feature extractor################

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new_df['tags']).toarray()

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y =[]

  for i in text.split():
    y.append(ps.stem(i))

  return " ".join(y)
new_df['tags']=new_df['tags'].apply(stem)

similarity = cosine_similarity(vector)
sorted(list(enumerate(similarity[0])),reverse=True,key = lambda x: x[1])[1:6]

######OUTPUT####

def recommend(movie):
    anime_index = new_df[new_df['Anime_name'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    for i in anime_list:
        print(new_df.iloc[i[0]].Anime_name)
recommend('onepiece')
