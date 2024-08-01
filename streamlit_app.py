import os

import streamlit as st
from src.youtube_downloader import youtube_downloader
from src.speech_to_text import process_file
from src.file_management import st_save_uploaded_file, create_dir_if_not_exists


def app():
    # Set up page
    st.set_page_config(
        page_title=st.secrets["page"]["page_title"],
        page_icon=st.secrets["page"]["page_icon"],
        layout=st.secrets["page"]["layout"])
    st.markdown(st.secrets["page"]["hide_menu_style"], unsafe_allow_html=True)
    st.markdown(st.secrets["page"]["footer"], unsafe_allow_html=True)

    # Session State Initialization
    if 'processed' not in st.session_state:
        st.session_state['processed'] = False
    if 'file_path' not in st.session_state:
        st.session_state['file_path'] = ""
    if 'done' not in st.session_state:
        st.session_state['done'] = False

    # database path
    database_path = st.secrets["data"]["database_path"]
    create_dir_if_not_exists(database_path)

    # Header
    st.image("./assets/images/banner.png")
    st.markdown(open("./assets/text/introduction.md",
                'r').read(), unsafe_allow_html=True)

    # choose an input method
    choice = st.radio(
        "Choose an input method:",
        ("Enter a YouTube link", "Upload a file"),
        index=0,
        format_func=lambda x: "📁 " + x if x == "Upload a file" else "🔗 " + x
    )

    # Create a file uploader widget
    if choice == "Upload a file":
        uploaded_file = st.file_uploader(
            "Upload a file",
            type=["wav", "flac"],
            accept_multiple_files=False
        )
        if uploaded_file is not None:
            # Save uploaded file to disk
            st_save_uploaded_file(uploaded_file, database_path)
            # Process downloaded file
            if st.button("Process File"):
                with st.spinner('Processing file...'):
                    results = process_file(os.path.join(
                        database_path, uploaded_file.name))
                st.text_area("Speaker's script:", results, height=512)
                st.session_state["done"] = True

    # Create a text area widget for YouTube link
    elif choice == "Enter a YouTube link":
        youtube_link = st.text_input("Enter a YouTube link")
        if youtube_link:
            if not st.session_state['processed']:
                if youtube_link.find("list") == -1:
                    with st.spinner('Donwloading from Youtube'):
                        file_path = youtube_downloader(
                            youtube_link, database_path)
                        st.session_state['file_path'] = file_path
                        st.session_state['processed'] = True
            if youtube_link.find("list") != -1:
                st.warning(
                    "This page doesn't work with playlist, please give simple video url.")

            # Process downloaded file
            if st.session_state['file_path'] != "":
                if st.button("Process File"):
                    with st.spinner('Processing file...'):
                        results = process_file(st.session_state['file_path'])
                    st.text_area("Speaker's script:", results, height=2048)
                    st.session_state["done"] = True


if __name__ == "__main__":
    app()
