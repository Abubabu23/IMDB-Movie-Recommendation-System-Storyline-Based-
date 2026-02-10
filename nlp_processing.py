import os
import re
import pickle
import pandas as pd
import nltk
from pathlib import Path
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")

os.makedirs("models", exist_ok=True)
os.makedirs("data", exist_ok=True)

csv_path = Path(r"C:\Users\Abuthahir\project\IMDb Movie\movie_data.csv")

df = pd.read_csv(csv_path)


df = df.drop_duplicates(subset=["Title", "Storyline"])
df = df.reset_index(drop=True)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["clean_storyline"] = df["Storyline"].apply(clean_text)


tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["clean_storyline"])


with open("models/tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

with open("models/tfidf_matrix.pkl", "wb") as f:
    pickle.dump(tfidf_matrix, f)

similarity = cosine_similarity(tfidf_matrix)

with open("models/similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

df.to_csv("data/imdb_2024_movies.csv", index=False)

print("✅ NLP processing completed successfully")
