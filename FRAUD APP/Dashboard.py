import streamlit as st
import Login as login_page
import Homepage as homepage

def dashboard():

   d_pages=["Dashboard","Transactions","Reports","Account"]
   selection_d=st.sidebar.radio("Explore within Dashboard",d_pages)

   st.title("Dashboard")
   st.write("Welcome to your dashboard!")

   st.file_uploader("Enter transaction data to be checked", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
   
   if st.button("Logout"):
        st.success("Logout successful!")
        st.session_state.authenticated=False
        st.session_state.page = "Home"
    