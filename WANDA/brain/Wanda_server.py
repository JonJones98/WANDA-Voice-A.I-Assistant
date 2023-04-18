from itertools import count
import sys
from tkinter import W
import youtube_dl
sys.path.insert(0,"..")
from brain import *
from command import *
from models.Wanda_DB import Commands
import eel

plm=0
voice_data = ""
typename=""

user_voice = record_audio()
while 1:
    Action.commands()
    try:
        voice_data=user_voice.lower()
    except:
        voice_data=user_voice.lower()
    try: 
        for a in dbmatch(voice_data):
            if plm == 0:
                wandaResponse = a
                plm = plm +1
            else:
                voice_data = a
                plm = 0
    except:
        wandaResponse="null"
        data="null" 

    if wandaResponse == "create":
        wanda_speak("Do you want to create new command?")
        user_voice = record_audio()
        if "no" in user_voice :
            wandaResponse="null"
            data="null"
    if wandaResponse == "null":
        globals()["Action"].__dict__[wandaResponse](data,wanda_speak)
    else:
        print(wandaResponse)
        print(voice_data)
        globals()["Action"].__dict__["start"](wandaResponse,voice_data,wanda_speak)
    
    wanda_speak("Listening...")
    user_voice = record_audio()




