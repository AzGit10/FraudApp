import streamlit as st

st.page_link("App.py", label="Home", icon="🏠")
st.page_link("Homepage.py", label="Page 1", icon="1️⃣")
st.page_link("Reports.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")