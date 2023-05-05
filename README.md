![](./assets/images/banner.png)

Speech to Text App is a [Streamlit](https://streamlit.io/) application that allows users to transcribe speech to text from either an uploaded audio file or a YouTube video. The app uses the [whisper](https://github.com/openai/whisper) speech-to-text library developed by OpenAI.

## Usage

To use the app, simply go to the [Speech to Text App website](azerty-labs.com) and follow the instructions on the page. You can choose to upload an audio file or enter a YouTube link to transcribe. The app will process the audio and display the transcribed text in a text area.

## Installation

To install the app locally, you will need to have Python 3.7 or higher installed on your machine. Clone the repository from GitHub:

```
git clone https://github.com/azerty-labs/speech-to-text-app.git
```

Then, navigate to the project directory and install the required packages using pip:

```
cd speech-to-text-app
python3.8 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

To run the app locally, use the following command:

```
streamlit run app.py
```

## Contributing

Contributions to the project are welcome! If you find any issues or bugs, please open an issue on the GitHub repository. If you would like to contribute code, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
