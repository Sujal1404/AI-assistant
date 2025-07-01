import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import wolframalpha
import os

# Initialize TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm your AI Assistant. How can I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🔍 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
    except Exception as e:
        speak("Sorry, I didn't catch that.")
        return "None"
    return query.lower()


def run_assistant():
    wish()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'play music' in query:
            pywhatkit.playonyt("top music")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'date' in query:
            today = datetime.date.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}")

        elif 'search' in query:
            query = query.replace("search", "")
            pywhatkit.search(query)

        elif 'calculate' in query:
            client = wolframalpha.Client("YOUR_WOLFRAM_API_KEY")
            res = client.query(query)
            answer = next(res.results).text
            speak(f"The answer is {answer}")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

        else:
            speak("Let me search that for you.")
            pywhatkit.search(query)


if name == "main":
    run_assistant()
