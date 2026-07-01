import os
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError
from dotenv import load_dotenv

load_dotenv()

try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except (KeyError, StreamlitSecretNotFoundError):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")