import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,31)
st.write(f"Your age is {age}.")

options = ["Python", "Java", "Perl", "Javascrip"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You Selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Cena", "Roman", "Reigns"],
    "Age": [30, 32, 34, 36],
    "City": ["New York", "Los Angeles", "Tampa", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
