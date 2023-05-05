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
import whisper

def process_file(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    result = result['text']
    return result