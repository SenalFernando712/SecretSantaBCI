import streamlit as st

# Example Lists
ListA = ["Ishan", "Senal", "Rashmi", "Dewmi"]
ListB = ["PASS123", "PASS456", "PASS789", "PASS000"]
ListC = ["GiftA", "GiftB", "GiftC", "GiftD"]

# Streamlit app
st.title("Secret Santa Assignment")

# Input fields for username and passcode
username = st.text_input("Enter your Username:")
passcode = st.text_input("Enter your Passcode:", type="password")

# Button to submit
if st.button("Submit"):
    if username in ListA:
        index = ListA.index(username)
        if ListB[index] == passcode:
            st.success(f"Your Secret Santa assignment is: {ListC[index]}")
        else:
            st.error("Invalid passcode. Please try again.")
    else:
        st.error("Invalid username. Please try again.")
