import streamlit as st
from PIL import Image
from openai import OpenAI
from utils import image_to_base64
from utils.llm import generated_notes_from_images
from utils.obsidian import append_to_obsidian_file, prepare_obsidian_writepath
from utils.ocr import ocr

api_key = st.secrets["OPENAI_API_KEY"]
openai_base_url = st.secrets.get("OPENAI_BASE_URL")
notion_token = st.secrets["NOTION_API_KEY"]

default_vault_path = '/Users/observedobserver/Documents/obsidian-notes/elwynn-library/image-to-notes'
client = OpenAI(api_key=api_key, base_url=openai_base_url)

with st.sidebar:
    import qrcode
    from io import BytesIO
    from streamlit.web.server import server_util
    internal_ip = st.net_util.get_internal_ip()
    url = server_util.get_url(internal_ip)
    img = qrcode.make(url)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    st.image(img_bytes, caption=f"scan to open {url}", use_column_width=True)
    obsidian_db = st.text_input('Obsidian DB', value=default_vault_path)
    model = st.selectbox('Model', ['gpt-4o', 'gpt-4-vision'])

    ocr_enhance = st.toggle('Use OCR Enhance', False)

st.title('Turn your photos into notes with AI')
title = st.text_input('Note Title', value='New Notes')

img_files = st.file_uploader('Your photos', accept_multiple_files=True)

all_done = 0
if img_files is not None:
    for img_file in img_files:
        image = Image.open(img_file)
        # save image to local and get the path

        with st.spinner('Taking notes...'):
            base64_str = image_to_base64(image)
            note_path = prepare_obsidian_writepath(note_title=title, vault_path=obsidian_db, uploaded_file=img_file)
            ocr_result = None
            if ocr_enhance:
                image.save(f'./{img_file.name}')
                ocr_result = ocr(f'./{img_file.name}')
            notes_gen = generated_notes_from_images(client=client, image_base64=base64_str, ocr_enhance_info=ocr_result, model=model)
            for notes in notes_gen:
                append_to_obsidian_file(content=notes, file_path=note_path)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        all_done += 1
        st.success('Done!')
    if all_done == len(img_files) and all_done > 0:
        st.balloons()

 

