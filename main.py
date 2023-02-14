
from email.mime import audio
from faulthandler import cancel_dump_traceback_later
from numpy import VisibleDeprecationWarning
import speech_recognition as sr
from time import ctime, time
import time
import playsound
import os
import random
import pyttsx3
from gtts import gTTS
import webbrowser
import urllib.request
import re


r = sr.Recognizer()
def wanda_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file= 'audio-'+str(r)+ '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
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
class Username:
    def __init__(self,name):
        self.name=name   

def record_audio(ask=False):
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
            print("a")
        except sr.RequestError:
            wanda_speak('Sorry, my speech service is down')
        return voice_data
def respond(voice_data):
    if voice_data=="1":
        wanda_speak('Hello my  name is Wanda. What is your name?')
        voice_data = record_audio()
        username=voice_data.replace(('name'or'my'or'is'), '')
        print(username)
        user=Username(username)
        wanda_speak('Hello, {}. nice to meet you. How can I help you today?'.format(user.name))
        return(user)
    elif 'rap' in voice_data:
        rap=voice_data.replace('rap','')
        wanda_speak(rap)
    elif 'what time is it' in voice_data:
        wanda_speak(ctime())
    elif 'play' in voice_data:
        if 'YouTube' in voice_data:
            predata=(voice_data[4:])
            data=predata.replace('on YouTube', '')
            yt_search=(data.replace(" ",""))
            print(yt_search)
            html2=urllib.request.urlopen("https://www.youtube.com/results?search_query="+yt_search)
            video_ids = re.findall(r"watch\?v=(\S{11})",html2.read().decode())
            ytr=random.randint(1, 2)
            yt_link=("https://www.youtube.com/watch?v="+video_ids[ytr])
            webbrowser.get().open(yt_link)
            wanda_speak("Opening Youtube and playing"+ str(data))
    elif 'search' in voice_data:
        search=(voice_data[6:])
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        wanda_speak('Here is what I found for'+search)
    elif 'where is' in voice_data:
        location=(voice_data[8:])
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        wanda_speak('Here is the location of'+location)
    elif 'what is the directions for the closest' in voice_data:
        direction=(voice_data[26:])
        url = 'https://google.nl/maps/search/'+direction+'/&amp;'
        webbrowser.get().open(url)
        wanda_speak('Here is the directions for'+direction)
    elif "solve" in voice_data:
        problem=(voice_data[5:])  
        equation=[]
        result=[]
        build_equation(problem,equation)
        print (equation)
        solve_equation(equation,result)
        answer=str(result[0])
        #answer=str(eval(problem))
        wanda_speak(problem+" = "+answer) 
    elif "open" in voice_data:
        app=voice_data.replace('open','')
        os.system("open -a "+app)
        wanda_speak("Opening "+app)
    elif "close" in voice_data:
        app=voice_data.replace('close','')
        os.system("pkill "+app)
        wanda_speak("Closing "+app)
    elif 'cancel' in voice_data:
        wanda_speak("Goodbye,{}. It was my pleasure assisting you today.Peace and love fam ,Wanda out.".format(user.name))
        exit()
# Addition
def add(a,b):
    return a+b 
# Subtraction
def sub(a,b):
    return a-b
# Multiplication
def mul(a,b):
    return a*b
# Division
def div(a,b):
    return a/b
# Remainder
def mod(a,b):
    return a%b
#Build Equation
def build_equation(problem,equation):
    placement=-1
    num=""
    for sign in problem:
        placement=+1
        if sign == "+":
            a=placement
            equation.append(float(num))
            equation.append(sign)
            num=""
        elif sign == "-":
            s=placement
            equation.append(float(num))
            equation.append(sign)
            num=""
        elif sign == "*":
            m=placement
            equation.append(float(num))
            equation.append(sign)
            num=""
        elif sign == "/":
            d=placement
            equation.append(float(num))
            equation.append(sign)
            num=""
        elif sign == " ":
            d=placement
        else:
            num=num+sign
    equation.append(float(num))
def solve_equation(equation,result):
    x=len(equation)
    calc=0
    for check in range(0,x):
        if check%2:
            if equation[check]=="+":
                a=equation[check-1]
                b=equation[check+1]
                calc=calc+add(a,b)
                a=0
                b=0
            elif equation[check]=="-":
                a=equation[check-1]
                b=equation[check+1]
                calc=calc+sub(a,b)
                a=0
                b=0
            elif equation[check]=="*":
                a=equation[check-1]
                b=equation[check+1]
                calc=calc+mul(a,b)
                a=0
                b=0
            elif equation[check]=="/":
                a=equation[check-1]
                b=equation[check+1]
                calc=calc+div(a,b)
                a=0
                b=0
    result.append(calc)

time.sleep(1)

voice_data = "1"
while 1:
    if voice_data=="1":
        respond(voice_data)
        username=voice_data
    voice_data = record_audio()
    respond(voice_data)
    
