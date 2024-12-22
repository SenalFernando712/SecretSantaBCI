import streamlit as st

# Example Lists
ListA = [
    "Anuhas", "Sanjana", "John", "Pasan", "Bewani", "Sahasra", "Shenali", "Roshane",
    "Senal", "Rashmi", "Dewmi", "Imasha", "Mihashi", "Nipuni", 
    "Bawanthi", "Sithmi", "Ranith", "Sewmini", "Adithya", "Sasanga", 
    "Pinky", "Manushi", "Kavindi", "Nimrod", "Linusha", "Shenoli", 
    "Sandali"
]
ListB = ['PDQPRM', 'AUN8KJ', 'CZYRWD', '0B4ZB1', 'DIP31Z', 'XUTXDN', 
         'UW6E8L', '5U2G2S', 'ICTJOE', '94L9N5', 'J5G9A2', 'F9SW0O', 
         '3FZT2X', '1NIJ8Q', 'JU0TKG', 'M6S3W6', 'FP6ZXO', 'R19LG8', 
         'M2X6XY', 'PXAPXN', 'E5ETY5', 'LFI63V', 'SAG91O', '77HGHA', 
         'PR1NAP', 'TNO8R1', 'QXACLG']

ListC = ['Nimrod', 'Dewmi', 'Kavindi', 'Manushi', 'Linusha', 'Sewmini', 
         'Bewani', 'Bawanthi', 'Ranith', 'Senal', 'Sandali', 'Sasanga', 
         'Pinky', 'Shenoli', 'Shenali', 'Roshane', 'Rashmi', 'Anuhas', 
         'Nipuni', 'Pasan', 'Sanjana', 'Sahasra', 'Sithmi', 'John', 
         'Imasha', 'Mihashi', 'Adithya']

# Streamlit app
st.title("BCI Choir | Secret Santa 2024")

# Input fields for username and passcode
username = st.text_input("Enter your Username:")
passcode = st.text_input("Enter your Passcode:", type="password")

# Button to submit
if st.button("Submit"):
    if username in ListA:
        index = ListA.index(username)
        if ListB[index] == passcode:
            st.success(f"You are the Secret Santa of : {ListC[index]}")
        else:
            st.error("Invalid passcode. Please try again.")
    else:
        st.error("Invalid username. Please try again.")
