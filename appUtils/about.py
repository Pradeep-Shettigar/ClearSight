import streamlit as st
def aboutpg():
    st.title("About")
    st.markdown("""
    <style>
    .section {
        background:#1f2937;
        padding:20px;
        border-radius:12px;
        margin-bottom:15px;
    }
    h1, h2, h3 {
        color:#e2e8f0;
    }
    p, li {
        color:#cbd5e1;
    }
    code {
        color:#38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("# 🧠 ClearSight – Brain Tumor Detection")

    st.markdown("""
    <div class="section">
    <h3>📌 Overview</h3>
    <p>
    ClearSight is a deep learning–based application designed to detect and visualize brain tumors from MRI images.
    It uses CNNs along with Grad-CAM to highlight regions influencing predictions.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h3>🚀 Features</h3>
    <ul>
    <li>Upload MRI images for analysis</li>
    <li>Predict tumor presence</li>
    <li>Visualize attention using Grad-CAM</li>
    <li>Simple Streamlit interface</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h3>🛠️ Tech Stack</h3>
    <ul>
    <li>Python</li>
    <li>PyTorch</li>
    <li>Streamlit</li>
    <li>OpenCV</li>
    <li>NumPy</li>
    <li>Pillow</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📂 Project Structure")

    st.code("""
    ClearSight/
    ├── model/
    ├── preprocessing/
    ├── utils/
    ├── weights/
    ├── app.py
    ├── requirements.txt
    ├── appUtils/
    """)

    st.markdown("### ⚙️ Installation & Usage")

    st.code("""git clone https://github.com/Pradeep-Shettigar/ClearSight.git
    cd ClearSight
    pip install -r requirements.txt
    streamlit run app.py""")

    st.markdown("""
    <div class="section">
    <h3>⚠️ Disclaimer</h3>
    <p>
    This project is for <b>educational purposes only</b>.<br>
    Not a medical diagnostic tool.<br>
    Do not use for real-world decisions.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h3>👤 Author</h3>
    <p><b>Prakyath K Poojary</b></p>
    <p><b>Nishanth VS</b></p>
    <p><b>Bharath raj</b></p>
    <p><b>Pradeep Shettigar</b></p>
    </div>
    """, unsafe_allow_html=True)