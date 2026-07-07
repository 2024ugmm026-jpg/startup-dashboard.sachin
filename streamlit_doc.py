import streamlit as st
import pandas as pd
import time

st.title('Stratup Dashboard')
st.header('I am loving streamlit')
st.subheader('And I am loving it')

st.write('This is normal text')

st.markdown("""
### My Favourit movies
- Race 3
- Humshakals
- Housfull
""")

st.code("""
def foo(input):
     return foo**2

x == foo(2)
     """)

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name': ['Sachin', 'Nitish', 'Ajay'],
    'Marks': [50, 60, 80],
    'Package': [10, 12, 14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')

st.json({'name': ['Sachin', 'Nitish', 'Ajay'],
         'Marks': [50, 60, 80],
         'Package': [10, 12, 14]})

st.image('WhatsApp Image 2025-04-02 at 18.55.06_d05a73cd.jpg')

st.sidebar.title('Sidebar Ka Title')

col1, col2 = st.columns(2)

with col1:
    st.image('WhatsApp Image 2025-04-02 at 18.55.06_d05a73cd.jpg')

    with col2:
        st.image('WhatsApp Image 2025-04-02 at 18.55.06_d05a73cd.jpg')

st.error('Login Failed')

st.success('Login Successful')

st.info('Login Successful')

st.warning('Login Successful')

bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.1)
    bar.progress(i)

st.text_input('Enter Your Name')
st.number_input('Enter your age')

email = st.text_input('Enter Your Email')
password = st.text_input('Enter Your Password')
gender = st.selectbox('select your gender', ['male', 'female', 'others'])

btn = st.button('Login kro')

if btn:
    if email == 'sachin@gmail.com ' and password == '1234':
        st.success('Login Successful')
        st.balloons()
        st.write('gender')
    else:
        st.error('Login Failed')

file = st.file_uploader('upload your file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
