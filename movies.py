import streamlit as st
import pickle

Model = pickle.load(open("movies.pkl", 'rb'))
Simi = pickle.load(open("similarity.pkl", 'rb'))

lst = []

option = st.selectbox('SELECT MOVIES', Model['original_title'].values)

col1, col2 = st.columns(2)

st.subheader('MOVIES RECOMMENDATION SYSTEM')
# intro = 'DEVELOPED BY "AHMED"'
# st.caption(intro)

with col2:
    st.markdown("<h6 style='text-align: right; color: red;'>DEVELOPED BY AHMED</h1>", unsafe_allow_html=True)

def recommend(movie):
    recommended_movies = []
    index = Model[Model['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(Simi[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:16]:
        recommended_movies.append(Model.iloc[i[0]].original_title)
    return recommended_movies

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: white;
    color:red;
}
div.stButton > button:hover {
    background-color: black;
    color:white;
    }
</style>""", unsafe_allow_html=True)

movbut = st.button("RECOMMEND ME MOVIES")

if movbut:
    try : 
        favmov = recommend(option)
        for i in favmov:
            st.write(i)
    except Exception:
        st.write("We Are Sorry To Tell You That !!!... This Movie isn't Available")

