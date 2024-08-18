from pathlib import Path
from openai import OpenAI
import config

client = OpenAI(api_key=config.open_ai_key)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy", # you can choose different voice model here.
  input="""Enter you text here!"""
)

import inspect

# Print the attributes and methods
#print(inspect.getmembers(response))
response.stream_to_file(speech_file_path)
