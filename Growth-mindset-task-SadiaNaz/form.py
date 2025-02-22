import streamlit as st
st.title("Growth Mindset Challenge GIAC")
st.header("Registration Form")
# st.code("for i in range(1, 5)")

# form
name = st.text_input("Enter your Name: ")
email = st.text_input("Enter your Email: ")
password = st.text_input("Enter your Password: ", type = "password")
city = st.selectbox("Enter your city: ", ("Karachi", "Islamabad", "Lahore", "Hyderabad", "sakkhar"))
button = st.button("Submit")
if button :
   st.write("name: ", name)
   st.write("email: " , email)
   st.write("pass: " , password)
   st.write("city: " , city)
   