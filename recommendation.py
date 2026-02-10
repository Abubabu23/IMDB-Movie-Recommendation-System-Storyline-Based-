import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")

# Load cleaned data
df = pd.read_csv(r"data/imdb_2024_movies.csv")

# Load models
with open("models/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("models/tfidf_matrix.pkl", "rb") as f:
    movie_vectors = pickle.load(f)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def recommend_movies(user_storyline, top_n=5):
    if not user_storyline.strip():
        return pd.DataFrame()

    cleaned = clean_text(user_storyline)
    user_vec = tfidf.transform([cleaned])

    sim_scores = cosine_similarity(user_vec, movie_vectors).flatten()
    sorted_indices = sim_scores.argsort()[::-1]

    seen_titles = set()
    recommendations = []

    for idx in sorted_indices:
        title = df.iloc[idx]["Title"]

        if title in seen_titles:
            continue

        seen_titles.add(title)
        recommendations.append(df.iloc[idx])

        if len(recommendations) == top_n:
            break

    return pd.DataFrame(recommendations).reset_index(drop=True)
