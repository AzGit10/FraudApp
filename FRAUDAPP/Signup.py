import streamlit as st
import re 

def signup():
    st.write("Please submit your account details. We will verify and email you back shortly")
    account_details=[]
    pattern_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    pattern_email="^[a-zA-Z0-9._%+-]+@[a-zA0-9.-]+\.[a-zA-Z]{2,}$"

    first_name= st.text_input("Enter your first name: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Enter your first name", disabled=False, label_visibility="visible")
    last_name= st.text_input("Enter your last name: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Enter your first name", disabled=False, label_visibility="visible")
    new_username=st.text_input("Enter your username: ", value="", max_chars=10, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Type here", disabled=False, label_visibility="visible")
    email=st.text_input("Enter your email: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Type here", disabled=False, label_visibility="visible")
    new_password=st.text_input("Enter your password: ", value="", max_chars=None, key=None, type="password", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Password must contain: 8+ characters, a special character, a capital or simple letter and number", disabled=False, label_visibility="visible")
    confirm_password=st.text_input("Enter your password again: ", value="", max_chars=None, key=None, type="password", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Password must contain: 8+ characters, a special character, a capital or simple letter and number", disabled=False, label_visibility="visible")

#https://stackoverflow.com/questions/2990654/how-to-test-a-regex-password-in-python
    validation_password=re.findall(pattern_password,new_password)
#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/   
    validation_email=re.findall(pattern_email,email)

    st.button("Submit details")

    if st.button:
        if len(new_username)<6:
              st.error("Username is too short. Must be 6 characters long")
        elif (validation_email):       
            if len(new_password)<8:
                st.error("Password is too short. Must be 8 characters long")  
            elif (validation_password):   
                if new_password == confirm_password:
                    if all([first_name, last_name, new_username, email, new_password]):
                        account_detail = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "username": new_username,
                        "email": email,
                        "password": new_password  }

                        st.success("Requirements matched! You can now submit your details")
                        account_details.append(account_detail)
                        st.session_state.page = "Home"
                    else:
                        st.error("All fields are required. Please fill in all the fields.")
                else:
                    st.error("Passwords do not match. Please try again.")
            else:
                st.error("Password should contain 'atleast': a special character [@#$%^&+=]")
                st.error("An Uppercase letter: A-Z")
                st.error("A Lowercase letter:a-z")
                st.error("A number:0-9")
        else:
            st.error("Email is not valid. Please enter a valid email address")
