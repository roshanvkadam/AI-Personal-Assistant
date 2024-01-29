import pyttsx3
import speech_recognition as sr
import os
from bs4 import BeautifulSoup
import datetime

import webbrowser
from time import sleep
import pywhatkit as kit
from datetime import timedelta
from datetime import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',200)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voice into text
def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("listening...")
      r.pause_threshold = 1
      audio = r.listen(source, timeout=10, phrase_time_limit=5)


    try:
       print("Recognizing...")
       query = r.recognize_google(audio,language='en-in')
       print(f"user said :{query}")

    except Exception as e:
       speak("say that again please...")
       return"none"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
   speak("who do wan to meassage")
   a= int(input('''roshan kadam 1- 1
     kaka 2- 2
     mayur kadam 3- 3'''))
   
   if a==1:
      speak("whats the message")
      message=str(input("Enter the message-"))
      kit.sendwhatmsg("+918459177014", message,time_hour=strTime,time_min=update)
      speak("message send succesfully")
   elif a==2:
      speak("whats the message")
      message=str(input("Enter the message-"))
      kit.sendwhatmsg("+919823015434", message,time_hour=strTime,time_min=update)
      speak("message send succesfully")
   elif a==3:
      speak("whats the message")
      message=str(input("Enter the message-"))
      kit.sendwhatmsg("+919326281144", message,time_hour=strTime,time_min=update)
      speak("message send succesfully")
      