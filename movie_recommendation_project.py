# -*- coding: utf-8 -*-
"""movie-recommendation-project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ebRAa4w0kaZGYOjxvw0QcI8NrwbecHgl
"""

import pandas as pd
import numpy as np

# prompt: upload file

from google.colab import files
uploaded = files.upload()
# for fn in uploaded.keys():
#   print('User uploaded file "{name}" with length {length} bytes'.format(
#       name=fn, length=len(uploaded[fn])))
#
# df = pd.read_csv(io.BytesIO(uploaded['filename.csv']))

movies = pd.read_csv('dataset.csv')

movies.head()

movies.columns

movies.info()

movies['tags'] = movies['genre'] + movies['overview']

movies.head()

new_df = movies[['id', 'title', 'genre', 'overview', 'tags']]

new_df.head()

new_df = new_df.drop(columns=['genre','overview'])

new_df.head()

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=10000, stop_words='english')

cv

vec = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()

vec

vec.shape

from sklearn.metrics.pairwise import cosine_similarity

sim = cosine_similarity(vec)

sim

new_df[new_df['title']=='The Shawshank Redemption']

dist = sorted(list(enumerate(sim[0])),reverse=True,key=lambda vec:vec[1])

for i in dist[0:5]:
    print(new_df.iloc[i[0]].title)

def recommend(movies):
    index = new_df[new_df['title']==movies].index[0]
    distance = sorted(list(enumerate(sim[index])),reverse=True,key=lambda vec:vec[1])
    for i in distance[0:5]:
        print(new_df.iloc[i[0]].title)

recommend('Iron Man')

recommend('The Shawshank Redemption')

recommend('The Godfather')

