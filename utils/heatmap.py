# ClearSight Project
# Licensed under Apache License 2.0
# Author: Pradeep-Shettigar

import torch
from PIL import Image
import numpy as np
import cv2
from preprocessing.config import transform

#os
def generate_heatmap(image_path, model, device, class_index):
    model.eval()

    
    target_layer = model.features[-1]  

    features = []
    gradients = []

    def forward_hook(module, inp, out):
        features.append(out)

    def backward_hook(module, grad_in, grad_out):
        gradients.append(grad_out[0])

    target_layer.register_forward_hook(forward_hook)
    target_layer.register_full_backward_hook(backward_hook)  


    img = Image.open(image_path).convert("RGB")
    input_tensor = transform(img).unsqueeze(0).to(device)
    input_tensor.requires_grad_(True)


    output = model(input_tensor)

  
    assert 0 <= class_index < output.shape[1], f"Invalid class_index={class_index}"


    model.zero_grad()
    score = output[0, class_index]
    score.backward(retain_graph=True)

    if len(features) == 0 or len(gradients) == 0:
        raise RuntimeError("Gradients or features were not captured. Check class index.")

    grad = gradients[0]
    act = features[0]

    weights = torch.mean(grad, dim=(2, 3), keepdim=True)
    cam = torch.sum(weights * act, dim=1).squeeze().cpu().detach().numpy()
    cam = np.maximum(cam, 0)
    cam = cv2.resize(cam, (img.width, img.height))
    cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-8)

    heatmap = cv2.applyColorMap(np.uint8(cam * 255), cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    overlay = (0.5 * heatmap + 0.5 * np.array(img)).astype(np.uint8)

    return np.array(img), overlay