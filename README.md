# 🧠 ClearSight – Brain Tumor Detection

## 📌 Overview

ClearSight is a deep learning–based application designed to detect and visualize brain tumors from MRI images.
It uses convolutional neural networks (CNNs) along with Grad-CAM visualization to highlight important regions influencing the model’s predictions.

---

## 🚀 Features

* Upload MRI images for analysis
* Predict tumor presence using a trained model
* Visualize model attention using heatmaps (Grad-CAM)
* Simple and interactive interface built with Streamlit

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Streamlit
* OpenCV
* NumPy
* Pillow

---

## 📂 Project Structure

```
ClearSight/
│
├── model/
│   ├── __pycache__/
|   |    ├── __init.cpython-312.pyc
|   |    ├── model.cpython-313.pyc
|   |
|   ├── __init__.py
|   ├── model.py
│
├── preprocessing/
|   ├── __pycache__/
|   |   ├── __init.cpython-312.pyc
|   |   ├── model.cpython-313.pyc
|   |
|   ├── __init__.py
|   ├── config.py
│
├── utils/
|   ├── __pycache__/
|   |    ├── __init.cpython-312.pyc
|   |    ├── config.cpython-313.pyc
|   |
|   ├── __init__.py
|   ├── heatmap.py
|   ├── predictor.py
│
├── weights/
|   ├── __init__.py
|   ├── brain_tumor_effnetb0.pth
│
├── LICENSE
│
├── NOTICE
│
├── README.md
│
├── app.py
│
├── pakages.txt
│
└── requirements.txt
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Pradeep-Shettigar/ClearSight.git
cd ClearSight
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes only**.

* It is **NOT a medical diagnostic tool**
* It must **NOT be used for real-world medical decisions**
* Predictions may be inaccurate and should not be relied upon

The author is **not responsible for any misuse, damages, or consequences**
resulting from the use of this software.

---

## 📜 License

This project is licensed under the Apache License 2.0.

---

## 🙏 Acknowledgements

This project is independently developed using standard deep learning techniques and publicly available research.

No code has been directly copied from other repositories.

---

## 👤 Author


    Prakyath K Poojary
    Nishanth VS
    Bharath raj
    Pradeep Shettigar

---
