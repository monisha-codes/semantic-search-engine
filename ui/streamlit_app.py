import streamlit as st
import requests

st.title("Semantic Search Engine Demo")

query = st.text_input("Enter search query")

if st.button("Search"):

    keyword = requests.get(
        "http://127.0.0.1:8000/api/search/keyword",
        params={"q": query}
    ).json()

    semantic = requests.get(
        "http://127.0.0.1:8000/api/search/semantic",
        params={"q": query}
    ).json()

    col1, col2 = st.columns(2)

    with col1:
        st.header("Keyword Search")

        for r in keyword:
            st.write(r["title"])
            st.write(r["content"])

    with col2:
        st.header("Semantic Search")

        for r in semantic:
            st.write(r["title"])
            st.write("Score:", r["score"])
            st.write(r["content"])