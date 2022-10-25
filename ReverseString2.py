#import libaries
import streamlit as st

#create function to reverse string
def reverse_string(string):
    return string[::-1] #Reverse the sting

s = st.text_input("Input String: ")#Allow the user to input their own string
n = st.number_input("How many times to print string: ")#Allow the user to input their own string


#Print the reversed string
st.write("The revsered text is:",reverse_string(s*n))
