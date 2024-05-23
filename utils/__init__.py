from io import BytesIO
import os
import base64

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

def get_markdown_files_in_path(dir: str):
    files = []
    for file in os.listdir(dir):
        if file.endswith(".md"):
            files.append(file)
    return files