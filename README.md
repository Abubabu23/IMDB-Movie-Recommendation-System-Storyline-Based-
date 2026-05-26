# 🎬 IMDB Movie Recommendation System Using Storylines

A machine-learning powered movie recommender system that suggests similar movies based on **storyline similarity** using **NLP, TF-IDF, and Cosine Similarity**.  
Movie data is scraped directly from IMDb using Selenium, cleaned, processed, and deployed via a user-friendly Streamlit UI.

---

## 🚀 Features

- IMDb movie data scraping using Selenium
- Storyline cleaning + NLP processing
- TF-IDF Vectorization & Cosine Similarity
- Top-5 movie recommendation engine
- Streamlit interactive interface

---

## 📁 Project Structure

├── app.py    
├── imdb_scraper.py
├── nlp_processing.py
├── recommendation.py
├── imdb_2024_movies.csv
├── movie_data.csv
├── tfidf.pkl
├── tfidf_matrix.pkl
├── requirement.txt
├── IMDB_Movie_Recommendation_Project_Report.pdf
└── README.md
---

## ▶️ Run the App

### Install Dependencies

pip install -r requirements.txt

### Run Streamlit
streamlit run app.py

---

## 📝 Future Enhancements

- Add BERT or SentenceTransformer embeddings
- Add genre + cast hybrid filtering
- Include posters and trailer links
- Deploy on Streamlit Cloud or HuggingFace Spaces

---

