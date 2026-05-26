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
```
├── data/
│   └── imdb_2024_movies.csv
├── models/
│   ├── tfidf.pkl
│   ├── tfidf_matrix.pkl
│   └── similarity.pkl
├── scripts/
│   ├── scraping.py
│   ├── nlp_processing.py
│   └── recommendation.py
├── streamlit_app/
│   └── app.py
└── README.md
```

---

## ▶️ Run the App
### Install Dependencies
```
pip install -r requirements.txt
```

### Run Streamlit
```
streamlit run app.py
```

---

## 📝 Future Enhancements
- Add BERT or SentenceTransformer embeddings  
- Add genre + cast hybrid filtering  
- Include posters and trailer links  
- Deploy on Streamlit Cloud or HuggingFace Spaces  

---

⭐ **If you like this project, consider giving it a star on GitHub!**
