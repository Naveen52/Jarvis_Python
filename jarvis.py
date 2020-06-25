import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good after noon')
    else:
        speak('good evening')
    speak("hello sir iam jarvis , how may i help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please")
        return 'None'
    return query

if __name__ == '__main__':
    Wish_me()
    # while(True):
    if 1:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack over flow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\navee\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")




