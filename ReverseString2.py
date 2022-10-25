#import libaries
import streamlit as st

st.title('Reverse String')
st.header('By Aiden Moses')

#create function to reverse string
def reverse_string(string):
    return string[::-1] #Reverse the sting

s = st.text_input("Input String: ")#Allow the user to input their own string
st.button('Reverse string',reverse_string)

#Print the reversed string
st.write("The revsered text is:",reverse_string(s))
st.image('UC Logo.jpeg')
