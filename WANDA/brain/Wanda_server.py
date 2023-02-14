from itertools import count
import sys
from tkinter import W
import youtube_dl
sys.path.insert(0,"..")
from brain import *
from command import *
from models.Wanda_DB import Commands
import eel

eel.init('templates')


eel.start('index.html', size=(1000, 600))
plm=0
voice_data = ""
Action.intro(record_audio,wanda_speak)
#Action.start("intro","",wanda_speak)
#wanda_speak('Hello how may i help you')
typename=""

while 1:
    eel.start('index.html', size=(1000, 600))
    user_voice = record_audio()
    print(user_voice)
    try:
        voice_data=user_voice.replace(" ","").lower()
    except:
        voice_data=user_voice
    print(voice_data)
    comlist =[func for func in dir(Action) if callable(getattr(Action, func))]
    arr=[]
    #arr2=[]
    for a in comlist[22:]:
        arr.append(a)
    
    #a = Commands.get_all()
    #for b in a:
    #    arr.append(b.name)

    try:    
        for a in dbmatch(voice_data,arr):
            if a!="list":
                data=str(arr)
                typename=a
                plm=1
            elif plm==0:
                data=a
                plm=1
                typename=""
            else:
                wandaResponse=a
                plm=0
    except:
        wandaResponse="null"
        data="null" 
    if wandaResponse=="create":
        wanda_speak("Do you want to create new command?")
        user_voice = record_audio()
        if "no" in user_voice :
            wandaResponse="null"
            data="null"
 
    if wandaResponse == "null":
        globals()["Action"].__dict__[wandaResponse](data,wanda_speak)
    else:
        globals()["Action"].__dict__["start"](wandaResponse,data,wanda_speak)
    
    wanda_speak("listening")




