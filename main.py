from tkinter.filedialog import askopenfilename
from pdfminer.high_level import extract_text
from google.cloud import texttospeech
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = " YOUR GOOGLE KEY"

#Get text from PDF file
text = extract_text(askopenfilename())



#Create textospeech client
client = texttospeech.TextToSpeechClient()
#Make text variable as input
synthesis_input = texttospeech.SynthesisInput(text=text)
#Configure voice
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
#Select MP3 file
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
#Write contents of response into MP3 file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')