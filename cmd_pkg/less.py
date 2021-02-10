import os
import shutil
import getch as gt
from os import system, name 
from time import sleep 

def printline (l, start,end):
    answer =""
    if(end > len(l)):
        end = len(l)
    for i in range(start,end):
        answer = answer + l[i]
        answer = answer + '\n'
    return answer
def deleline(l,maxline,end):
    answer =""
    goto = end -maxline
    for i in range(0,goto):
        answer = answer + l[i]
        answer = answer + '\n'
    return answer

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def less(**kwargs):
    answer = ''
    termSize = shutil.get_terminal_size()
    maxLine = termSize[1]
    getch = gt.Getch()
    params = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    answer =''
    lines =[]
    currLine = 0
    pagenum =0
    
    if(len(params) == 1 and len(flag) ==0 ):
        if(len(directions) ==2 and directions[0] =='r+'):
            files = directions[1]
        else:
            files = params[0]
        with open(files, "r") as f:
            lines = f.read().splitlines()
        TnumofpPages = len(lines)/maxLine
        answer = printline(lines,0,maxLine)
        if(len(directions) == 2 and (directions[0] =='a+' or directions[0] =="w+")):
            direct = directions[0]
            file = directions[1]
            f = open(file, direct)
            f.write(answer)
            f.close()
        else:
            print(answer)
            pagenum +=1
            currLine = maxLine
            char =''
            while char != 'q' or "Q":
                char = getch()
                if char == 'q' or char == 'Q': # ctrl-c
                    clear()
                    return
                elif char in '\x1b':                # arrow key pressed
                    null = getch()                  # waste a character
                    direction = getch()             # grab the direction
                    
                    if direction in 'A':            # up arrow pressed
                        # get the PREVIOUS command from your history (if there is one)
                        # prints out '↑' then erases it (just to show something)
                        if(pagenum !=1):
                            answer = deleline(lines,maxLine,currLine)
                            currLine = currLine -maxLine
                            clear()
                            print(answer)
                            pagenum-=1
                        else:
                            pass
                    if direction in 'B':            # down arrow pressed
                        # get the NEXT command from history (if there is one)
                        # prints out '↓' then erases it (just to show something)
                        if(pagenum < TnumofpPages):
                            answer = printline(lines,currLine,currLine+maxLine)
                            currLine = currLine +maxLine
                            pagenum+=1
                            print(answer)
                        else:
                            
                            pass
    elif(len(params) > 1 and len(flag) ==0 ):
        lines = params
        TnumofpPages = len(lines)/maxLine
        answer = printline(lines,0,maxLine)
        if(len(directions) == 2 and (directions[0] =='a+' or directions[0] =="w+")):
            direct = directions[0]
            file = directions[1]
            f = open(file, direct)
            f.write(answer)
            f.close()
        else:
            print(answer)
            pagenum +=1
            currLine = maxLine
            char =''
            while char != 'q' or "Q":
                char = getch()
                if char == 'q' or char == 'Q': # ctrl-c
                    clear()
                    return
                elif char in '\x1b':                # arrow key pressed
                    null = getch()                  # waste a character
                    direction = getch()             # grab the direction
                    
                    if direction in 'A':            # up arrow pressed
                        # get the PREVIOUS command from your history (if there is one)
                        # prints out '↑' then erases it (just to show something)
                        if(pagenum !=1):
                            answer = deleline(lines,maxLine,currLine)
                            currLine = currLine -maxLine
                            clear()
                            print(answer)
                            pagenum-=1
                        else:
                            pass
                    if direction in 'B':            # down arrow pressed
                        # get the NEXT command from history (if there is one)
                        # prints out '↓' then erases it (just to show something)
                        if(pagenum < TnumofpPages):
                            answer = printline(lines,currLine,currLine+maxLine)
                            currLine = currLine +maxLine
                            pagenum+=1
                            print(answer)
                        else:
                            
                            pass

            
    else:
        answer = 'invalid command'