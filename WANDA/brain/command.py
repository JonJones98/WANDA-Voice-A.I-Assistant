
from email.mime import audio
from faulthandler import cancel_dump_traceback_later
from pydoc import classname
from click import command
from numpy import VisibleDeprecationWarning
import speech_recognition as sr
from time import ctime, time
import os
import random
import webbrowser
import urllib.request
import re
from brain import *
from user import Username
from models.Wanda_DB import Commands

all_Commands= Commands.get_all()

class Action():
    #Commands
    def commands():
        global commands_list
        commands_list={}
        for x in all_Commands:
            name=x.name
            cc="""{variables}={result} \n{script}""".format(variables=(x.variables),script=(x.script),result="***")
            commands_list[name]=cc
    def start(wcc,voice_data,wanda_speak):
        print("Running start()")
        a = {wcc:commands_list[wcc].replace("***","'{}'".format(str(voice_data)))}
        print(commands_list[wcc])
        commands_list.update(a)
        print(commands_list[wcc])
        exec(commands_list[wcc])
    def intro(record_audio,wanda_speak):
        class Username:
            def __init__(self,name,todo):
                self.name=name
                self.todo=todo  
        wanda_speak('Hello my name is Wanda. What is your name?')
        voice_data = record_audio()
        print(voice_data)
        try:
            username=voice_data.replace(('name'or'my'or'is'), '')
        except:
            username=voice_data
        print(username)
        global user
        user=Username(username,[])
        wanda_speak('Hello, {}. nice to meet you. How can I help you today?'.format(user.name))
        return(user)
    def null(nul,wanda_speak):
        return