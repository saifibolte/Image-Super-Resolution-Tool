import os
import torch
import zipfile
import numpy as np
import gradio as gr
import shutil
import RRDBNet_arch as arch
from PIL import Image

# Create folders if not exist
os.makedirs("LR", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Check for GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load ESRGAN model
model_path = 'models/RRDB_ESRGAN_x4.pth'
model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path, map_location=device), strict=True)
model.eval()
model = model.to(device)

def upscale_images(image_paths):
    # Clear previous results
    if os.path.exists("LR"):
        shutil.rmtree("LR")
    if os.path.exists("results"):
        shutil.rmtree("results")
    os.makedirs("LR", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    output_images = []

    for idx, img_path in enumerate(image_paths):
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        
        # Open image from file path
        img = Image.open(img_path).convert("RGB")
        img.save(f"LR/{base_name}.png")

        # Convert to tensor
        img_np = np.array(img)
        img_np = img_np[:, :, ::-1]  # RGB to BGR
        img_np = img_np * 1.0 / 255
        img_tensor = torch.from_numpy(np.transpose(img_np, (2, 0, 1))).float().unsqueeze(0).to(device)

        # Inference
        with torch.no_grad():
            output = model(img_tensor).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))  # BGR to RGB
        output = (output * 255.0).round().astype(np.uint8)

        # Save result as PNG (to avoid WebP issue)
        out_img_path = f"results/{base_name}_upscaled.png"
        out_img = Image.fromarray(output)
        out_img.save(out_img_path, format="PNG")
        output_images.append(out_img_path)

    # Create ZIP of results
    zip_filename = "upscaled_images.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in os.listdir("results"):
            zipf.write(os.path.join("results", file), file)

    return output_images, zip_filename


# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 📈 Image Super Resolution Tool")
    
    with gr.Row():
        with gr.Column():
            input_images = gr.File(label="Upload Low-Resolution Images", file_types=["image"], file_count="multiple")
            btn = gr.Button("Upscale Images")
            reset_btn = gr.Button("Reset")
        
        with gr.Column():
            gallery = gr.Gallery(label="Upscaled Images", show_label=True)
            download = gr.File(label="Download All as ZIP")

    btn.click(fn=upscale_images, inputs=input_images, outputs=[gallery, download])
    reset_btn.click(fn=lambda: (None, None), inputs=None, outputs=[gallery, download])

demo.launch(share=True)
