import streamlit as st
import Login as login_page
import Dashboard as dashboard_page
import Signup as signup_page

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False 
if "page" not in st.session_state:
    st.session_state.page = "Home"

def home():
    st.sidebar.title("Navigation")
    pages = st.sidebar.radio("Explore", ["Home", "Contact Us"])
    st.markdown('<h1 style="text-align: center;">Fraud Guard</h1><h2 style="text-align: center;">Check for fraud</h2>', unsafe_allow_html=True)
    login_section = st.button("Login")  
    signup_button = st.button("Signup")  
    st.write("Credit card fraud within the next 5 years will cause many global losses. Another study revealed that as many as 80% of the US credit cards currently in use have been compromised.")
    st.write("However, thanks to machine learning (ML), credit card fraud detection is becoming easier and more efficient. ML-based fraud detection solutions can track patterns and prevent abnormal transactions.")

    if login_section:
        st.session_state.page = "Login"
        
    if signup_button:
        st.session_state.page = "Signup"

if st.session_state.page == "Home":
    home()

elif st.session_state.page == "Login":
    if st.session_state.authenticated:
        dashboard_page.dashboard()
    else:
        login_page.login()   
elif st.session_state.page == "Login":
    if st.session_state.authenticated:
        dashboard_page.dashboard()
    else:
        login_page.login()

elif st.session_state.page == "Signup":
    signup_page.signup()

