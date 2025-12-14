# Content-Based Recommendation System
# CodSoft AI Internship - Task 4

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
data = pd.read_csv("movies.csv")

# Convert genres to vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(data["genre"])

# Compute similarity
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title):
    if movie_title not in data["title"].values:
        print("Movie not found in database.")
        return

    index = data[data["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for '{movie_title}':")
    for i in scores[1:4]:
        print("-", data.iloc[i[0]]["title"])

if __name__ == "__main__":
    print("Available movies:")
    for movie in data["title"]:
        print("-", movie)

    choice = input("\nEnter a movie name: ")
    recommend(choice)
