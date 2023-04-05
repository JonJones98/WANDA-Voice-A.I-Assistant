def list(record_audio,wanda_speak):
    wanda_speak('What would you like on the list?')
    voice_data = record_audio()
    try:
        todo_list=(voice_data.replace(('and'or'add'or'on'or'list'), '')).split(" ")
    except:
        todo_list=[]
    print(todo_list)
    Username(todo=todo_list)
    wanda_speak('To list created')
def time(time,wanda_speak):
    a=time
    b=wanda_speak
    time=ctime()
    wanda_speak(ctime())
def play(yt_search,wanda_speak):
    if 'youtube' in yt_search:
        data=yt_search.replace("on youtube","").replace("play","").replace(" ","")
        html2=urllib.request.urlopen("https://www.youtube.com/results?search_query="+data)
        video_ids = re.findall(r"watch\?v=(\S{11})",html2.read().decode())
        ytr=random.randint(1, 2)
        yt_link=("https://www.youtube.com/watch?v="+video_ids[ytr])
        webbrowser.get().open(yt_link)
    wanda_speak("Opening Youtube and playing"+ str(yt_search))
def search(search,wanda_speak):
    url = 'https://google.com/search?q='+search
    webbrowser.get().open(url)
    wanda_speak('Here is what I found for'+search)
def location(location,wanda_speak):
    url = 'https://google.nl/maps/place/'+location+'/&amp;'
    webbrowser.get().open(url)
    wanda_speak('Here is the location of'+location)
def direction(direction,wanda_speak):
    url = 'https://google.nl/maps/search/'+direction+'/&amp;'
    webbrowser.get().open(url)
    wanda_speak('Here is the directions for'+direction)
def solve(problem,wanda_speak):
    #Reference 
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
    equation=[]
    result=[]
    build_equation(problem,equation)
    print (equation)
    solve_equation(equation,result)
    answer=str(result[0])
    wanda_speak(problem+" = "+answer) 
def open(app,wanda_speak):
    os.system("open -a "+app)
    wanda_speak("Opening "+app)
def close(app,wanda_speak):
    os.system("pkill "+app)
    wanda_speak("Closing "+app)
def cancel(data,wanda_speak):
        wanda_speak("Goodbye,{}. It was my pleasure assisting you today.Peace and love fam ,Wanda out.".format(user.name))
        exit()
def create(classname,classfunction):
    a=classname
    b=classfunction
    commandList={}
    loop=True
    count=0
    while loop:
        if count==1:
            loop=False
        def a():
            b
            return()
        count=count+1
    num = len(commandList)+1
def commandsettings(data,wanda_speak):
    wanda_speak("Commands that are available are "+data)

    