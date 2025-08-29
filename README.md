# 📈 Image Super Resolution Tool

This project is a **Gradio-based ESRGAN Image Upscaler** deployed on **Hugging Face Spaces**. It uses the **Enhanced Super-Resolution Generative Adversarial Network (ESRGAN)** model to upscale low-resolution images by 4x while preserving details and enhancing quality.

---

## 🚀 Features
- Upload multiple low-resolution images  
- Automatically upscale using **ESRGAN (x4 factor)**  
- Preview upscaled images in the browser  
- Download all upscaled images as a **ZIP file**  
- Works on **GPU or CPU**  
- One-click deployment on Hugging Face Spaces - [View Live Demo](https://huggingface.co/spaces/saifibolte/TinyLlama-AI-Assistant) *(Runs on CPU, so generation may be slower)*

- Note: This Hugging Face Space is running on CPU, which means the image upscaling process can take longer compared to GPU-based environments, especially for high-resolution images. To ensure a smooth experience and faster results, we recommend testing with smaller or low-resolution images. For your convenience, we have provided a set of sample images in the low_res folder. You can use these images to quickly test the upscaling functionality on this Space. 

---

## 🛠 Requirements

For Hugging Face Spaces (Gradio template), add these dependencies in `requirements.txt`:

```
torch
torchvision
numpy
pillow
opencv-python
gradio
```

---

## ✅ Usage
- **Step 1:** Upload one or more low-resolution images.
- **Step 2:** Click **Upscale Images**.
- **Step 3:** View the upscaled images in the gallery.
- **Step 4:** Download the ZIP file containing all upscaled images.
- **Step 5:** Click **Reset** to process new images.

---

## 📌 Model Details
- Model: **ESRGAN (RRDBNet architecture)**  
- Pretrained weights: `RRDB_ESRGAN_x4.pth`  
- Scaling: **x4 super-resolution**

Download ESRGAN pretrained weights from [link]([https://github.com/xinntao/ESRGAN](https://drive.google.com/file/d/1eoWN613w5pjL4Uyh5XnYMuBIXL52CZ4z/view?usp=sharing)).

---

## 📸 Preview
![Gradio UI](https://github.com/saifibolte/Image-Super-Resolution-Tool/blob/c65089f49e783e0e2daa011b1dfb8d992e78aa38/figures/UI.png)

---

### ✅ Credits
- [ESRGAN Original Repository](https://github.com/xinntao/ESRGAN)
