# ClearSight Project
# Licensed under Apache License 2.0
# Author: Pradeep-Shettigar

import torch
import torch.nn as nn
from PIL import Image
import numpy as np
import streamlit as st
from preprocessing.config import transform,class_names
def predict_image(image, model, device):
    img = Image.open(image).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img_tensor)
        probs = torch.softmax(output, dim=1)[0].cpu().numpy()

    class_id = np.argmax(probs)
    confidence = probs[class_id]

    return class_names[class_id], confidence, probs
