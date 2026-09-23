# pip install SpeechRecognition
# pip install pyttsx3

import sys
import pyaudiowpatch

sys.modules["pyaudio"] = pyaudiowpatch

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# ---------------------------------
# SPEAK FUNCTION
# ---------------------------------

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ---------------------------------
# LISTEN FUNCTION
# ---------------------------------

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.........")

        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

        print("Audio Done")

    try:
        command = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand what you said")
        return ""

    except sr.RequestError as e:
        print("Could not connect to speech recognition service:", e)
        return ""


# ---------------------------------
# PROCESS FUNCTION
# ---------------------------------

speak("Hello, I'm your voice assistant. How can I help you?")

while True:

    command = listen()

    if "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command or "today" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "chatgpt" in command or "chat gpt" in command:

        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "who created you" in command:

        speak("I was created using Python")

    elif "bye" in command or "exit" in command:

        speak("Goodbye. Have a nice day")
        break

    elif command == "":
        pass

    else:

        speak("Sorry, I do not know that command yet")