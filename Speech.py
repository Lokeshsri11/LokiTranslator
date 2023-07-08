import speech_recognition as sr
import subprocess
from googletrans import Translator
from gtts import gTTS
import os

# Function to record audio from the microphone
def record_audio(duration):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        audio = r.record(source, duration=duration)
        print("Finished recording.")
    return audio

# Function to transcribe speech using Google Speech Recognition
def transcribe_speech(audio):
    r = sr.Recognizer()
    try:
        transcription = r.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        print("Unable to transcribe speech.")
    except sr.RequestError as e:
        print("Error:", str(e))

# Function to translate text using Google Translate
def translate_text(text, target_language):
    translator = Translator(service_urls=['translate.google.com'])
    try:
        translated_text = translator.translate(text, dest=target_language).text
        return translated_text
    except Exception as e:
        print("Translation Error:", str(e))

# Function to convert text to speech and save as audio file
def save_audio(text, filename, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

# Function to play the audio file
def play_audio(filename):
    os.system(f"xdg-open {filename}")

# Set the target language for translation
target_language = 'en'  # Change it to your desired language code

# Record audio from the microphone
audio = record_audio(5)  # Record for 5 seconds

# Perform speech recognition
transcription = transcribe_speech(audio)
print("Transcription:", transcription)

# Translate the transcription to the target language
translation = translate_text(transcription, target_language)
print("Translation:", translation)

# Save the translated text as audio
save_audio(translation, 'output.mp3', target_language)

# Play the audio
play_audio('output.mp3')
