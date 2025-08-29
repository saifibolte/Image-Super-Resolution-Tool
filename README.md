# 📈 ESRGAN Image Upscaler (Gradio + Hugging Face Spaces)

This project is a **Gradio-based ESRGAN Image Upscaler** deployed on **Hugging Face Spaces**. It uses the **Enhanced Super-Resolution Generative Adversarial Network (ESRGAN)** model to upscale low-resolution images by 4x while preserving details and enhancing quality.

---

## 🚀 Features
✔ Upload multiple low-resolution images  
✔ Automatically upscale using **ESRGAN (x4 factor)**  
✔ Preview upscaled images in the browser  
✔ Download all upscaled images as a **ZIP file**  
✔ Works on **GPU or CPU**  
✔ One-click deployment on Hugging Face Spaces  

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

Download ESRGAN pretrained weights from [Xintao's ESRGAN repo](https://github.com/xinntao/ESRGAN).

---

## 📸 Preview
![ESRGAN Gradio UI](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/gradio-interface.png)

---

### ✅ Credits
- [ESRGAN Original Repository](https://github.com/xinntao/ESRGAN)
- [Gradio](https://gradio.app)
- [Hugging Face Spaces](https://huggingface.co/spaces)
