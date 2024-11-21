import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    enumerated_list = list(enumerate(similiar[index]))
    distance = sorted(enumerated_list, reverse=True, key=lambda vector: vector[1])[1:11]

    recommended_movies=[]
    for i in distance:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('moviedict.pkl','rb'))

movies=pd.DataFrame(movies_dict)
similiar=pickle.load(open('similiar','rb'))

st.title('Movie-Recommender-System')

selected_movie =st.selectbox(
    'Select your favourite movie',
    movies['title'].values)

if st.button('Recommend'):
    result=recommend(selected_movie)
    for i  in result:
        st.write(i)