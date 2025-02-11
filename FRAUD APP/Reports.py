import streamlit as st
st.set_page_config(page_title="Reports")
st.title("Reports Page")

def reports():

   r_pages=["Dashboard","Transactions","Reports","Account"]
   selection_r=st.sidebar.radio("Explore within Dashboard",[d_pages[0],d_pages[1],d_pages[2], d_pages[3]])
