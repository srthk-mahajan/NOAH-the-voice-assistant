import pyttsx3
import speech_recognition as sr
import pyttsx3.drivers
import pyttsx3.drivers.sapi5
from datetime import datetime
import pyautogui
import webbrowser
import subprocess
import os #inbuilt op system
import urllib #for url
from time import sleep
import re #url request manage
import requests #url request 
from bs4 import BeautifulSoup #bs4 lib collection n soup one is weather update for accessing html n xml files
import sys 

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #which voice
engine.setProperty('rate', 180) #speed
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello i am No  ahhh. Please tell me how may i help you!")


def takecommand():
            r = sr.Recognizer() #speechrecog as sr
            with sr.Microphone() as source:
                speak('Please speak now...')
                print('Please speak now...')
                r.pause_threshold = 1 #induce pause
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)            
            try:
                speak("Recognizing...")
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                #speak(f"You said: {query}\n")
                print(f"You said: {query}\n")

            except Exception as e:
                    # print(e)    
                speak("Please speak again...")
                print("Please speak again...")
                return "None"
            return query


wishMe()
while True:
    query=takecommand().lower()
    # query=input("Type: ")
    
    if 'open explorer' in query:
        pyautogui.hotkey('win', 'e') #links mouse and keyboard with code-gui

    elif 'open chrome' in query:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                speak("chrome opened")

    elif 'close chrome' in query:
                os.system("TASKKILL /F /IM chrome.exe")
                speak("google chrome is closed")

    elif 'open notepad' in query:
                os.startfile("notepad.exe")
                speak("Notepad is openned")
    elif 'close notepad' in query:
                os.system("TASKKILL /F /IM notepad.exe")
                speak("notepad is closed")
    elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
   
    elif 'search' in query:
        query = query.replace("search", "")
        url = f"https://www.google.com/search?q={query}"
    
    # Try to open in the default web browser using webbrowser module
        try:
            webbrowser.open(url)
            speak("I have searched for you on the web.")
    
    # If webbrowser module fails, use subprocess to open the default browser
        except:
            try:
                subprocess.Popen(['start', url], shell=True)
                speak("I have searched for you on the web.")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't open a web browser for the search.")
    elif 'youtube' in query:
                query = query.replace("play in youtube", "")
                speak("Speak your video name")
                song = takecommand()
                print(song)
                searchkeyword = (song.replace(" ", ""))
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchkeyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=" + video_ids[0])
                speak("your youtube video is openned")
                sleep(5)
    elif "weather" in query:
                search = "weather in Greater Noida"
                url = f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")
                print(f"current {search} is {temp}")
    elif 'marry' in query:
            speak("No you idiot get lost. ")
    elif "shutdown" or "shut down" in query:
                speak("ok sir, have a good day! Also ankur sir is the best")
                sys.exit()