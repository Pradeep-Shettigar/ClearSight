import streamlit as st
def homepg():
    st.markdown("""
        <style>
        
        /* Gradient background */
        .main {
            background: linear-gradient(135deg, #0f172a, #1e293b, #020617);
            background-size: 400% 400%;
            animation: gradientMove 12s ease infinite;
        }

        @keyframes gradientMove {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* Card style */
        .card {
            padding: 20px;
            border-radius: 16px;
            background: linear-gradient(145deg, #1f2937, #111827);
            transition: all 0.3s ease;
            box-shadow: 0 0 0 rgba(0,0,0,0);
            height: 150px;
        }

        /* Hover animation */
        .card:hover {
            transform: translateY(-8px) scale(1.03);
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            background: linear-gradient(145deg, #2563eb, #1e40af);
        }

        .card h4 {
            margin-bottom: 10px;
        }

        .card p {
            font-size: 14px;
            color: #cbd5e1;
        }

        /* Title glow */
        .title {
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        </style>
        """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🧠 Clear Sight</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray; font-size:18px;'>AI-Powered Brain Tumor Detection</p>", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div style='
        padding:25px;
        border-radius:16px;
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        margin-bottom:20px;
    '>
    <h3>🔍 Smart MRI Analysis</h3>
    <p>Upload scans, detect tumors, and visualize AI decisions instantly.</p>
    </div>
    """, unsafe_allow_html=True)

 
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>📤 Upload</h4>
        <p>Securely upload MRI scans.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🧠 Analyze</h4>
        <p>Run deep learning model.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h4>📊 Visualize</h4>
        <p>See Grad-CAM heatmaps.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <h4>⚡ Predict</h4>
        <p>Get tumor classification.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

        
    if st.button("🚀 Start Analysis", use_container_width=True):
        st.session_state.page = "📤 Upload"
        st.rerun()

    st.write("")

       
    st.warning("⚠️ For educational use only. Not a medical diagnosis tool.")

    st.write("")

       
    st.markdown("### 🧬 Learn About Tumor Types")

    col1, col2, col3 = st.columns(3)

    # Initialize state
    if "tumor_info" not in st.session_state:
        st.session_state.tumor_info = None

    with col1:
        if st.button("🧠 Glioma", use_container_width=True):
            st.session_state.tumor_info = "glioma"

    with col2:
        if st.button("🧬 Meningioma", use_container_width=True):
            st.session_state.tumor_info = "meningioma"

    with col3:
        if st.button("⚡ Pituitary", use_container_width=True):
            st.session_state.tumor_info = "pituitary"

    st.write("")

       
    if st.session_state.tumor_info == "glioma":
        st.info("""
        🧠 **Glioma**
            
        - Tumor that originates in brain glial cells  
        - Can be low-grade or high-grade  
        - Common symptoms: headaches, seizures, vision issues  
        """)

    elif st.session_state.tumor_info == "meningioma":
        st.info("""
        🧬 **Meningioma**
        
        - Arises from meninges (brain covering)  
        - Usually benign and slow-growing  
        - Symptoms depend on tumor location  
        """)

    elif st.session_state.tumor_info == "pituitary":
        st.info("""
        ⚡ **Pituitary Tumor**
            
        - Occurs in pituitary gland  
        - Affects hormone production  
        - Can cause vision problems and hormonal imbalance  
        """)