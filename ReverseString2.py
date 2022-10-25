#import libaries
import streamlit as st
st.image('UC Logo.jpeg')
st.title('Reverse String')
st.subheader('By Aiden Moses')

#create function to reverse string
def reverse_string(string):
    return string[::-1] #Reverse the sting

tab1, tab2 = st.tabs(["Tab 1", "Tab2"]
tab1.write("this is tab 1")

s = st.text_input("Input String: ")#Allow the user to input their own string
st.button('Reverse string',reverse_string)

    
#Print the reversed string
st.write("The revsered text is:",reverse_string(s))

