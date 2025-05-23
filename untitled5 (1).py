# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1izp0akC7jjCvgg1ynyRrZ4Rx1TbYoW2x
"""

Install required packages
!pip install pandas scikit-learn tensorflow
Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
# Load the dataset from a public URL
url = 'https://files.grouplens.org/datasets/movielens/ml-100k/u.data'
columns = ['user_id', 'movie_id', 'rating', 'timestamp']
df = pd.read_csv(url, sep='\t', names=columns)

df.head()
def recommend_movies(user_id, model, df, movie2movie_encoded, user2user_encoded, num_recommendations=10):
    encoded_user_id = user2user_encoded[user_id]
    all_movie_ids = np.array(list(movie2movie_encoded.values()))

    user_array = np.array([encoded_user_id] * len(all_movie_ids))
    predictions = model.predict([user_array, all_movie_ids])

    movie_pred = list(zip(all_movie_ids, predictions.flatten()))
    movie_pred.sort(key=lambda x: x[1], reverse=True)

    reverse_movie_map = {v: k for k, v in movie2movie_encoded.items()}
    top_movie_ids = [reverse_movie_map[x[0]] for x in movie_pred[:num_recommendations]]

    return df[df['movie_id'].isin(top_movie_ids)][['movie_id']].drop_duplicates()

# Example usage:
recommend_movies(1, model, df, movie2movie_encoded, user2user_encoded)