import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
# from google import search
# from googlesearch.googlesearch import GoogleSearch
# import urllib3
from googlesearch import search

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello sir! i m your personal assistant jarvis ,how may i assist you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    #speak("i m ironman")
    # speak("")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            wikiSay = "According to Wikipedia "+results
            # speak("According to Wikipedia ")
            speak(wikiSay)

        elif 'open youtube' in query:
            # patha='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            # webbrowser.get(patha).open("youtube.com")
            # print(webbrowser.Chrome)
            # url="youtube.com"
            webbrowser.open("https://www.youtube.com")

        elif 'play music' in query:
            music_dir = 'F:\\z\\Maiz songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR the time is {strtime}")
            print(strtime)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/maiz_bagwala_007")

        elif 'search' in query:
            query = query.replace("search", "")
            for j in search(query, tld="co.in", num=10, stop=1, pause=2):
                print(j)
                webbrowser.open(j)
