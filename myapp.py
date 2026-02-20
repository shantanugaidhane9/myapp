import streamlit as st
import numpy as np 
import pandas as pd

st.title("Hello, streamlit ")
st.write("Streamlit : this is your first streamlit app")
st.text("Lets get started ")

name =st.text_input("Enter your name : ")
if st.button("submit"):
    st.success("Hello, your there !")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['A', 'B']   
)


st.line_chart(df)
st.bar_chart(df)


st.sidebar.title("Navigation")


st.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/2e/Rohit_Sharma_2019.jpg",
    caption="Sample Image"
)


st.video("https://youtu.be/ZIQH5m-dZDc?si=NvXSDxGi3ddxQfzt")

upload_file = st.file_uploader("Upload a CSV file", type='csv')

# Read and display CSV
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("This is the Main Title")


st.header("This is a Header")

st.subheader("This is a Subheader")


st.caption("This is a caption text")

st.text("This is normal text")


st.markdown("### This is Markdown Header")
st.markdown("**Bold text**")
st.markdown("*Italic text*")


st.markdown("<h1 style='color:blue;'>Blue Title</h1>", unsafe_allow_html=True)