import streamlit as st
from scripts.recommendation import recommend_movies

st.set_page_config(page_title="IMDB Movie Recommender")

st.title("🎬 IMDB Movie Recommendation System (2024)")

storyline = st.text_area(
    "Enter a movie storyline",
    height=150
)

if st.button("Recommend Movies"):
    if storyline.strip() == "":
        st.warning("Please enter a storyline")
    else:
        results = recommend_movies(storyline)

        for _, row in results.iterrows():
            st.subheader(row["Title"])
            st.write(row["Storyline"])
            st.divider()
