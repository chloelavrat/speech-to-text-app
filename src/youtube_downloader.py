import os
import yt_dlp


def youtube_downloader(link, dir_path):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': os.path.join(dir_path, '%(id)s.wav')}) as audio:
        info_dict = audio.extract_info(link, download=True)
        id = info_dict['id']
        audio.download(link)
    return os.path.join(dir_path, str(id)+".wav")
