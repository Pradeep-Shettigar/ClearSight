import streamlit as st
from utils.heatmap import generate_heatmap
from utils.predictor import predict_image
from preprocessing.config import class_names
from model.model import load_model
from appUtils.home import homepg
from appUtils.upload import uploadpg
from appUtils.about import aboutpg
import os
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "logo.png")

with open(logo_path, "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

st.set_page_config(page_title="Clear Sight", layout="wide")

st.markdown("""
<style>

section[data-testid="stSidebar"] {
    width: 280px !important;
    background: linear-gradient(180deg, #0f172a, #1e293b, #020617);
}

section[data-testid="stSidebar"] h1 {
    font-size: 34px !important;
    font-weight: 900 !important;
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    text-align: left;
    padding: 12px 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    background: rgba(255,255,255,0.05);
    color: white;
    border: none;
    transition: all 0.3s ease;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    transform: translateX(5px) scale(1.02);
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
}

section[data-testid="stSidebar"] .stButton > button:focus {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    box-shadow: 0 0 15px rgba(59,130,246,0.6);
}

* {
    transition: all 0.2s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

st.sidebar.markdown("""
<div style="display:flex; align-items:center; gap:10px;">
    <img src="data:image/png;base64,{}" width="40">
    <h2 style="margin:0;">Clear Sight</h2>
</div>
""".format(
    base64.b64encode(open("logo.png", "rb").read()).decode()
), unsafe_allow_html=True)

def nav(label):
    if st.sidebar.button(label, use_container_width=True):
        st.session_state.page = label

nav("🏠 Home")
nav("📤 Upload")
nav("ℹ️ About")


page = st.session_state.page

if page == "🏠 Home":
    
    homepg();
        

elif page == "📤 Upload":
    uploadpg();

elif page == "ℹ️ About":
    aboutpg();
