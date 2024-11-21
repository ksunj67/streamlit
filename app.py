import streamlit as st
 
# Add a title to your app
st.title("My Streamlit App")
 
# Add some text input
user_input = st.text_input("Enter text:")
 
# Display the input
st.write(f"You entered: {user_input}")

