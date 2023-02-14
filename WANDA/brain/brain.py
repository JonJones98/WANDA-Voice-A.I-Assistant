
from email.mime import audio
from faulthandler import cancel_dump_traceback_later
from numpy import VisibleDeprecationWarning
import speech_recognition as sr
import playsound
import os
import random
import pyttsx3
from gtts import gTTS
from command import *
import shutil


r =sr.Recognizer()
mic_Check=0
def wanda_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file= 'audio-'+str(r)+ '.mp3'
    tts.save("WANDA/audio/"+audio_file)
    playsound.playsound("WANDA/audio/"+audio_file)
    print(audio_string)
    os.remove("WANDA/audio/"+audio_file)
    #shutil.rmtree("WANDA/audio/")
def wanda_speak1(audio_string):
    ptts = pyttsx3.init()
    #Rate
    rate=ptts.getProperty('rate')
    print(rate)
    ptts.setProperty('rate',250)
#Voice
    voices=ptts.getProperty('voices')
    print(voices)
    ptts.setProperty('voice',voices[1].id)
    ptts.say(audio_string)
    ptts.runAndWait()
    print(audio_string)  
def record_audio(ask=False):
    try:
        with sr. Microphone() as source:
            if ask:
                wanda_speak(ask)
            audio = r.listen(source)
            voice_data=' '
            try:
                if audio==' ':
                    audio = r.listen(source)
                else:
                    voice_data = r.recognize_google(audio)
                    print(voice_data)
            except sr.UnknownValueError:
                print("I didn't get that")
                voice_data=input("Type command here:")
                return voice_data
            except sr.RequestError:
                wanda_speak('Sorry, my speech service is down')
            return voice_data
    except:
            wanda_speak('No Microphone found.Please connect input device type or type command below')
            voice_data=input("Type command here:")
def dbmatch(voice_data,arr):
    x = voice_data
    print("dbmatch arr "+arr)
    result = binary_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", str(result))
        global data
        data=str(arr[result])
        global wandaResponse
        if result==30:
            data=voice_data
        else:
            wandaResponse=voice_data.replace(data,"")
        return wandaResponse,data

    else:
        wandaResponse="null"
        data="null"
        wanda_speak("Command is not found")     
def binary_search(arr, low, high, x):
    print("High="+high)
    print("Low="+low)
    print("Arr="+arr)
    print("x="+x)
    if high>= low:
        mid =(high+low)//2
        if arr[mid] in x :
            return mid
        elif arr[mid]>x:
            return binary_search(arr, low, mid -1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

