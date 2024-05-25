import streamlit as st
from PIL import Image
from openai import OpenAI
from utils import image_to_base64
from utils.llm import generated_notes_from_images
from utils.obsidian import append_to_obsidian_file, prepare_obsidian_writepath

api_key = st.secrets["OPENAI_API_KEY"]
openai_base_url = st.secrets.get("OPENAI_BASE_URL")
notion_token = st.secrets["NOTION_API_KEY"]

client = OpenAI(api_key=api_key, base_url=openai_base_url)

st.title('Turn your photos into notes with AI')

with st.sidebar:
    obsidian_db = st.text_input('Obsidian DB', value='/Users/observedobserver/Documents/obsidian-notes/elwynn-library/image-to-notes')
    model = st.selectbox('Model', ['gpt-4o', 'gpt-4-vision'])

# notion_db = st.text_input('Notion DB', value='1ce492388e4a4538bb66f4ac979c9964')
title = st.text_input('Note Title', value='Meetup Notes')

img_files = st.file_uploader('Your photos', accept_multiple_files=True)
all_done = 0
if img_files is not None:
    for img_file in img_files:
        image = Image.open(img_file)
        with st.spinner('Taking notes...'):
            base64_str = image_to_base64(image)
            note_path = prepare_obsidian_writepath(note_title=title, vault_path=obsidian_db, uploaded_file=img_file)

            notes_gen = generated_notes_from_images(client=client, image_base64=base64_str)
            for notes in notes_gen:
                append_to_obsidian_file(content=notes, file_path=note_path)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        all_done += 1
        st.success('Done!')
    if all_done == len(img_files) and all_done > 0:
        st.balloons()

 

