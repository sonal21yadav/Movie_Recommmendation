import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="Movie Recommender",
    layout="centered"
)

@st.cache_data
def load_data():
    movies_list = pickle.load(open("movies.pkl", "rb"))
    similarity  = pickle.load(open("similarity.pkl", "rb"))
    return movies_list, similarity

movies_list, similarity = load_data()

def recommend(movie):
    movie_index   = movies_list[movies_list["title"] == movie].index[0]
    distances     = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distances)),
                           reverse=True,
                           key=lambda x: x[1])[1:6]
    return [movies_list.iloc[i[0]].title for i in movies_sorted]

st.title("Movie Recommendation System")
st.markdown("---")
st.markdown("Select a movie you like and get 5 similar movie recommendations instantly.")

selected_movie_name = st.selectbox(
    "Choose a movie:",
    movies_list["title"].values
)

if st.button("Get Recommendations", use_container_width=True):
    recommendations = recommend(selected_movie_name)
    st.markdown("---")
    st.subheader(f"Because you liked {selected_movie_name}, try these:")
    st.markdown("")
    for i, movie_name in enumerate(recommendations, 1):
        st.markdown(f"**{i}.** {movie_name}")

st.markdown("---")
st.caption("Built with Python, scikit-learn, and Streamlit | TMDB 5000 Dataset")
