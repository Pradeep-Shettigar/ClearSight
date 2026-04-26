import streamlit as st
from appUtils.home import homepg
from appUtils.upload import uploadpg
from appUtils.about import aboutpg

st.set_page_config(page_title="Clear Sight", layout="wide")

# Sidebar styling
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

# Default page
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# Sidebar title (no logo now)
st.sidebar.markdown("## 🧠 Clear Sight")

# Navigation function
def nav(label):
    if st.sidebar.button(label, use_container_width=True):
        st.session_state.page = label

# Navigation buttons
nav("🏠 Home")
nav("📤 Upload")
nav("ℹ️ About")

# Page routing
page = st.session_state.page

if page == "🏠 Home":
    homepg()

elif page == "📤 Upload":
    uploadpg()

elif page == "ℹ️ About":
    aboutpg()
