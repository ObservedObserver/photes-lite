# image-to-note
Transform your images into notes with ease.

### Overview

This project provides a Streamlit app that converts images into written notes. Currently, the app can only be run locally (or on the device where your note-taking app is running), as it directly writes to the file system.

### Getting Started

To use image-to-note, follow these steps:

1. **Setup Environment**
Create a `.streamlit/secrets.toml` file with the following content:
```toml
[openai]
api_key = "your_openai_api_key"
base_url = "optional_openai_base_url"  # leave blank if not using
```
2. **Run Streamlit App**
Execute the following command to run the app:
```bash
streamlit run main.py --server.enableXsrfProtection false
```
