#import libaries
import streamlit as st
st.image('UC Logo.jpeg')
st.title('Reverse String')
st.subheader('By Aiden Moses')

#create function to reverse string
def reverse_string(string):
    return string[::-1] #Reverse the sting


s = st.text_input("Input String: ")#Allow the user to input their own string

#Print the reversed string
btn = st.write("The reversed text is:",reverse_string(s))

st.button('Reverse string',btn)

    


