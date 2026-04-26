import streamlit as st
from utils.heatmap import generate_heatmap
from utils.predictor import predict_image
from preprocessing.config import class_names
from model.model import load_model
def uploadpg():
    st.markdown("### 📥 Upload & Analyze MRI")

    with st.expander("⬇️ Click to Upload MRI Image", expanded=True):

        uploaded_file = st.file_uploader(
            "Upload MRI Image",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        if uploaded_file:
            allowed_types = ["image/jpg", "image/jpeg", "image/png"]

            if uploaded_file.type not in allowed_types:
                st.error("Unsupported file type. Please upload (JPG, JPEG, PNG only)")
                uploaded_file = None

        st.image(uploaded_file, caption="MRI Preview", use_container_width=True)

    if "model" not in st.session_state:
        st.session_state.model, st.session_state.device = load_model()

    model = st.session_state.model
    device = st.session_state.device

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🧠 Classification", use_container_width=True):
            if not uploaded_file:
                st.error("Upload image first")
            else:
                pred, conf, probs = predict_image(uploaded_file, model, device)
                st.success(f"Prediction: {pred.upper()}")

    with col2:
        if st.button("📊 Confidence Graph", use_container_width=True):
            if not uploaded_file:
                st.error("Upload image first")
            else:
                _, _, probs = predict_image(uploaded_file, model, device)
                st.bar_chart(probs)

    with col3:
        if st.button("🔥 Heatmap", use_container_width=True):
            if not uploaded_file:
                st.error("Upload image first")
            else:
                pred, _, _ = predict_image(uploaded_file, model, device)
                idx = class_names.index(pred)
                _, heat = generate_heatmap(uploaded_file, model, device, idx)
                st.image(heat, caption="Grad-CAM", use_container_width=True)