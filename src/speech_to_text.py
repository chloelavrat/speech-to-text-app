import whisper


def process_file(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    result = result['text']
    return result
