# imported modules
import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import subprocess
import pyttsx3
from bs4 import BeautifulSoup
import numpy as np

chatStr = ""
def google():
    
    user_query = query

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='Z0LcW XcVN5d').get_text()
    print(result)
      
def say(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e: 
            return "Some Error Occurred. Sorry from my side"

if __name__ == '__main__':
    print('Welcome sir')
    say("This is personal  assistant max")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        greet = [['hi','hi'],['hello','hello'],['good morning','good morning'],['good afternoon','good afternoon']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        for greets in greet:
            if f"{greets[0]}".lower() in query.lower():
                say(f"{greets[0]} sir... hope you are doing fine. how may i assist you")
        if "play music" in query:
            musicPath = r"C:\Users\mayan\Music\new_192_05 - Duniyaa - PagalSongs.com.mp3"
            os.startfile(musicPath)
            if "next" in query:
                musicPath = r"C:\Users\mayan\Music\Malang Sajna_192(PaglaSongs).mp3"
                os.startfile(musicPath)
        elif "how are you" in query:
            say("i am doing well sir. how can i assist you")
        elif "vs code" in query:
            musicPath = r"C:\Users\mayan\Desktop\Visual Studio Code.lnk"
            os.startfile(musicPath)
        elif "next" in query:
            musicPath = r"C:\Users\mayan\Music\Malang Sajna_192(PaglaSongs).mp3"
            os.startfile(musicPath)

        elif "regular" in query:
            musicPath = r"C:\Users\mayan\Music\new_192_05 - Duniyaa - PagalSongs.com.mp3"
            abhishek = r"C:\Users\mayan\Desktop\Visual Studio Code.lnk"
            music = r"https://youtu.be/HcOc7P5BMi4?si=_BBfdz0rBk2s2W-k"
            os.startfile(musicPath)
            webbrowser.open(music)
            os.startfile(abhishek)
        elif "figma" in query:
            musicPath = r"C:\Users\mayan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Figma.lnk"
            os.startfile(musicPath)
        elif "frontend" in query:
            musicPath = r"https://youtu.be/HcOc7P5BMi4?si=_BBfdz0rBk2s2W-k"
            webbrowser.open(musicPath)
        elif "playlist" in query:
            musicPath = "https://youtu.be/tRScKDcYxlk?si=ZUsa03qzZOSJX8uj"
            webbrowser.open(musicPath)
        elif "jiocinema" in query:
            musicPath = "https://www.jiocinema.com/"
            webbrowser.open(musicPath)
        elif "camera" in query:
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif "close camera" in query:
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} and {min} minutes")
        elif "stop" in query:
            say("as you wish sir")
            break
        elif "hackerrank" in query:
            musicPath = "https://www.hackerrank.com/"
            say("yes sir..")
            webbrowser.open(musicPath)
            
        else:
            print("Chatting...")
            try:
                google()
            except Exception:
                
                print('Sorry no result, please be clear')
                say('Sorry no result, please be clear')

