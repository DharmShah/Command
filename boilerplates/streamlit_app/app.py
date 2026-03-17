import streamlit as st
from config import settings

st.set_page_config(page_title="Streamlit Boilerplate", layout="centered")
st.title("Streamlit Boilerplate")
st.write("Provider:", settings.model_provider)

if st.button("Run Demo"):
    st.success("App is connected to env config successfully.")
