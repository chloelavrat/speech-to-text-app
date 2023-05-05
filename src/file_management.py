# ------------------------------------------------------------------------------
# Speech to Text App
# ------------------
#
# This Streamlit app allows you to convert speech to text from either an uploaded 
# audio file or a YouTube video.The app uses whisper speech-to-text library 
# that openai developped.
#
# The page and the model integration has been developed by Azerty-Labs
# 
# <Copyright 2023 - Azerty-Labs>
# ------------------------------------------------------------------------------
import os
from pathlib import Path
# ------------------------------------------------------------------------------
def st_save_uploaded_file(uploaded_file, path, name=None):
    if name == None:
        with open(os.path.join(path ,uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getvalue())

    if isinstance(name, str):
        with open(os.path.join(path , name + "." + uploaded_file.name.split(".")[-1]),"wb") as f:
            f.write(uploaded_file.getvalue())
    
    pass
# ------------------------------------------------------------------------------
def create_dir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print("Directory created:", dir_path)
    else:
        print("Directory already exists:", dir_path)
# ------------------------------------------------------------------------------
def get_list_of_file(folder, exts):
    path = Path(folder)
    assert path.exists(), 'folder does not exist'

    files = [file for ext in exts for file in path.glob(f'**/*.{ext}')]

    return files
# ------------------------------------------------------------------------------