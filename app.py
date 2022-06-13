import streamlit as st
import pickle

st.header('📽 Sistema de recomendación de Películas 🍿')

movie_list = pickle.load(open('model/movies.pkl', 'rb'))
similarity_model = pickle.load(open('model/similarity_model.pkl', 'rb'))


def recommended_movies(movie):
    index = movie_list[movie_list['title'] == movie].index[0]
    long = sorted(list(enumerate(similarity_model[index])), reverse=True, key=lambda x: x[1])
    movie_names = []
    for i in long[1:10]:
        title = movie_list.iloc[i[0]].title
        movie_names.append(title)
    return movie_names


selected_movie = st.selectbox(
     "Selcciona Una Película",
    movie_list
)

if st.button('Mostrar Recomendaciones Similares'):
    recommended_movies = recommended_movies(selected_movie)
    for movie in recommended_movies:
         st.markdown(f'- __{movie}__')
