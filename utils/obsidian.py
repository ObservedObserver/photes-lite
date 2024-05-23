import os
import shutil

def add_markdown_to_obsidian(note_title, content, vault_path, uploaded_file):
    """
    Adds Markdown content and an uploaded image to an Obsidian note. Creates a new note if it doesn't exist.
    
    :param note_title: Title of the Obsidian note.
    :param content: Markdown content to be added.
    :param vault_path: Path to the Obsidian vault.
    :param uploaded_file: File-like object of the uploaded image.
    """
    import os
    import shutil
    
    # Ensure the vault path exists
    if not os.path.exists(vault_path):
        raise FileNotFoundError(f"The specified vault path '{vault_path}' does not exist.")
    
    # Create the full path to the note
    note_filename = f"{note_title}.md"
    note_path = os.path.join(vault_path, note_filename)
    
    # Handle the uploaded file
    image_filename = uploaded_file.name
    image_dir = os.path.join(vault_path, f'assets_{note_title}')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    target_image_path = os.path.join(image_dir, image_filename)
    
    # Save the uploaded file to the vault
    with open(target_image_path, 'wb') as out_file:
        out_file.write(uploaded_file.getbuffer())
    
    # Create the Markdown for the image
    image_markdown = f"![{image_filename}]({image_filename})\n"
    
    # Append the content and image markdown to the note (create the note if it doesn't exist)
    with open(note_path, 'a') as note_file:
        if image_markdown:
            note_file.write(image_markdown + '\n')
        note_file.write(content + '\n')
    
    return note_path


def prepare_obsidian_writepath(note_title, vault_path, uploaded_file):
    """
    Adds Markdown content and an uploaded image to an Obsidian note. Creates a new note if it doesn't exist.
    
    :param note_title: Title of the Obsidian note.
    :param content: Markdown content to be added.
    :param vault_path: Path to the Obsidian vault.
    :param uploaded_file: File-like object of the uploaded image.
    """
    import os
    import shutil
    
    # Ensure the vault path exists
    if not os.path.exists(vault_path):
        raise FileNotFoundError(f"The specified vault path '{vault_path}' does not exist.")
    
    # Create the full path to the note
    note_filename = f"{note_title}.md"
    note_path = os.path.join(vault_path, note_filename)
    
    # Handle the uploaded file
    image_filename = uploaded_file.name
    image_dir = os.path.join(vault_path, f'assets_{note_title}')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    target_image_path = os.path.join(image_dir, image_filename)
    
    # Save the uploaded file to the vault
    with open(target_image_path, 'wb') as out_file:
        out_file.write(uploaded_file.getbuffer())
    
    # Create the Markdown for the image
    image_markdown = f"![{image_filename}]({image_filename})\n"
    
    # Append the content and image markdown to the note (create the note if it doesn't exist)
    with open(note_path, 'a') as note_file:
        if image_markdown:
            note_file.write(image_markdown + '\n')
    
    return note_path


def append_to_obsidian_file(content: str, file_path: str):
    # Open the file in append mode
    with open(file_path, 'a') as f:
        f.write(content)