import streamlit as st
import torch
from utils.heatmap import generate_heatmap
from utils.predictor import predict_image
from preprocessing.config import class_names
from model.model import load_model
#gpt code just for testing
from streamlit_option_menu import option_menu
st.markdown("""
<style>
/* Page background */
.stApp {
    background: radial-gradient(circle at top, #111827, #020617);
    color: white;
}


/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #b0b3b8;
    margin-bottom: 30px;
}

/* Upload box */
.upload-box {
    border: 2px dashed #4da3ff;
    border-radius: 18px;
    padding: 40px;
    text-align: center;
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(77,163,255,0.25);
}



/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #232caa, #00e5ff, #04225f);
    color: black;
    font-size: 16px;
    border-radius: 12px;
    padding: 10px 25px;
    border: none;
    font-weight: bold;
}
}
.stButton > button {
    cursor: pointer;
    transition: all 0.25s ease;
}


.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s;
}

/* Center everything */
.center {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)
selected = option_menu(
        menu_title=None,
        options=["Home", "Upload", "About"],
        icons=["house", "cloud-upload", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )


st.title("Brain tumor detector and clasifire")


    
if selected == "Home":
    st.markdown(
        "<h1 style='color:#00b4d8; text-align:center;'>Welcome to the CLEAR SIGHT application!</h1>",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1,2,1])

    with center:
        st.markdown("""
        <div class="upload-box">
            <h2 style="color:#00b4d8;">What is CLEAR SIGHT?</h2>
            <p>
            ClearSight is an ML-powered tool designed to assist doctors in detecting brain tumors 
            from MRI scans quickly and accurately using MRI images.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="upload-box">
            <h2 style="color:#00b4d8;">How to Use CLEAR SIGHT</h2>
            <ol>
                <li>Go to the Upload tab</li>
                <li>Upload an MRI scan (JPG / PNG)</li>
                <li>Click Predict to analyze</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

if selected == "Upload":

   st.markdown('<div class="main-title">Upload MRI Scan</div>', unsafe_allow_html=True)
   st.markdown('<div class="sub-title">Upload an MRI image for brain tumor detection</div>', unsafe_allow_html=True)

   st.markdown('<div class="upload-box">', unsafe_allow_html=True)
   model, device = load_model()

   uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])
   label_visibility="collapsed"

   st.markdown('</div>', unsafe_allow_html=True)

   st.write(" ")  # spacing




   if st.button("Predict"):
        predicted_class, confidence, probs = predict_image(uploaded_file, model, device)

        st.subheader("Prediction Result")
        st.write(f"Tumor Type: **{predicted_class.upper()}**")
        st.write(f"Confidence: **{confidence:.2f}**")
        
        st.bar_chart(probs)



   if st.button("Heatmap"):
        predicted_class, _, probs = predict_image(uploaded_file, model, device)
        class_index = class_names.index(predicted_class)

        orig, heat = generate_heatmap(uploaded_file, model, device, class_index)

        st.image(heat, caption="Grad-CAM Heatmap", use_container_width=True)
            
if selected == "About":
    st.title("About Page")
    st.write("Welcome to the About Page!")