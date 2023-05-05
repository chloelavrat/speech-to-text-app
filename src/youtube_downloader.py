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
import os, yt_dlp
# ------------------------------------------------------------------------------
def youtube_downloader(link, dir_path):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': os.path.join(dir_path,'%(id)s.wav')}) as audio:
        info_dict = audio.extract_info(link, download = True)
        id = info_dict['id']
        audio.download(link)
    return os.path.join(dir_path,str(id)+".wav")
# ------------------------------------------------------------------------------