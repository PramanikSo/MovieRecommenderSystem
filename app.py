import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=eb1ba5c02652d76a32a7459325587120&language=en-US".format(movie_id))
    data = response.json()
    # return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    # Check if poster_path is available in the API response
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        # If poster_path is not available, return a default placeholder image URL
        return "https://example.com/placeholder.jpg"  # Replace with your placeholder image URL


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies=[]
    recommend_movies_poster =[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_poster.append(fetch_poster(movies_id))
    return recommend_movies,recommend_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('simialrity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be connected?',
    (movies['title'].values)
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    recommend(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)
    # st.text(names[1])
    # st.image(posters[1])

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])




