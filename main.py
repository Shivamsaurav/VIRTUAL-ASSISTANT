import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)  # 9


def speak(text):
    """
    This speak function will pronounce the string whichever passed to it.
    """
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir...")

    elif hour >=12 and hour < 18:
        speak("Good afternoon sir ...")

    else:
        speak("Good Evening sir...")

    # speak("I am JARVIS. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query} \n")
    except:
        speak("Say that again please")
        query = None
    return query


def command():
    speak("initializing Jarvis...")
    greet()
    query = takecommand()


    if 'wikipedia' in query.lower():
        speak("Searching...")
        query.replace("wikipedia","")
        result = wikipedia.summary(query, sentences = 2)
        speak(result)

    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")


    elif 'open google' in query.lower():
        webbrowser.open("google.com")

if __name__ == "__main__":
	command()
