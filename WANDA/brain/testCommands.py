from models.Wanda_DB import Commands
from brain import *
from user import Username
all_Commands= Commands.get_all()
commands_list={}
variabl_list={}

count=-1
# 
a=["Jon","","play jazz music on youtube","cool music","charlotte","6600 Main st","2+2","Safari","Safari","Jon","commands_list.keys()","Safari"]
for x in all_Commands:
    name=x.name
    count=count+1
    cc="""{variables}=a[{counts}] \n{script}""".format(variables=(x.variables),script=(x.script),counts=count)
    commands_list[name]=cc
    try:
        exec(commands_list[name])
        print(name+" pass")
    except:
        print(name+" failed")
wanda_speak("Test Finish")
exec(commands_list["close"])

