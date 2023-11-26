import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ilya Medvedski")
    content = """ 
    I'm a software engineer with 9+ years of experience in IT.
    I've participated in developing end-to-end solutions for Fortune 500
    companies. On top of that, I have experience in managing up to 5 teams
    simultaneously. Over the past few years I've helped set up processes for the entire
    department and was a deputy SM Functional Manager.
    I am always coaching my colleagues, helping them become the best version of
    themselves, and I can easily find common grounds with people regardless of gender or
    nationality.
    My strongest suit is understanding projects from all perspectives - not only from the
    business side, but also from the development team`
    """
    st.info(content)

st.text("Below you can find some of the apps I have built in Python.Feel free to contact me")

col3, col4 = st.columns(2)
data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
