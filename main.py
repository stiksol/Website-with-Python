import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ilya Medvedski")
    content = """ 
    Some text about myself should be placed here 
    """
    st.info(content)