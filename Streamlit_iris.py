import streamlit as st
#import pickle

st.title('Iris Prediction')

a = st.number_input('Enter Sepal Length ')
b = st.number_input('Enter Sepal Width ')
c = st.number_input('Enter Petal Length ')
d = st.number_input('Enter Petal Width ')

process = st.selectbox('Choose the operations : ', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

if st.button('Good to execute??'):
    if process=='Addition':
        st.write(a+b+c+d)
    elif process=='Multiplication':
        st.write(a*b*c*d)
    else:
        st.write('Development in process')
