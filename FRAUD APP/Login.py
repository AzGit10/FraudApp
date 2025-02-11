import streamlit as st
import Dashboard as dashboard_page
import Homepage as homepage

#Login page
def login():
    
    st.sidebar.title("Navigation")
    pages = st.sidebar.radio("Explore", ["Home", "Signup"])

    if pages == "Home":
        homepage.home()

    username=st.text_input("Enter your username: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Type here", disabled=False, label_visibility="visible")
    password=st.text_input("Enter your password: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Type here", disabled=False, label_visibility="visible")
    login_button=st.button("Login ")

    if login_button:
        if username == "admin" and password == "admin123":  # Replace with your authentication logic
            st.success("Login successful!")
            st.session_state.authenticated=True
        else:
            st.error("Invalid username or password")
            st.session_state.authenticated=False

    
