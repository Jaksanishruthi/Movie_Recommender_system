import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# Load your API key securely
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
print(f"TMDB API key loaded: {api_key}")

# Function to fetch movie poster from TMDB
def fetch_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        print(f"TMDB API RESP: {data}")  # Debug: print the response
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            # Return a placeholder image if no poster is available
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_names.append(movies.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_names, recommended_posters

# Streamlit app UI
st.header("🎬 Movie Recommender System Using Machine Learning")

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie to get recommendations", movie_list)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
