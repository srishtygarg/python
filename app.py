import streamlit as st
st.title('Loan application app')
l=st.number_input("Enter your loan amount")
s=st.number_input("Enter your salary")
c=st.number_input("Enter your credit score")
if s>40000 and c>500:
    st.write("Congratulations")
else:
    st.write("We are sorry")
