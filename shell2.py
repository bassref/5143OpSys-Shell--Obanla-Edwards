import threading

import os

import sys

from numpy.core.records import array

import cmd_pkg as cp

from cmd_pkg import parameters as par

import numpy as np

import getch as gt

from time import sleep

import concurrent.futures

import re


class CommandHelper(object):

    def __init__(self):

        self.commands = {}

        self.commands['ls'] = cp.ls

        self.commands['cd'] = cp.cd

        self.commands['pwd'] = cp.pwd

        self.commands['mkdir'] = cp .mkdir

        self.commands['cp'] = cp. cp

        self.commands['rm'] = cp. rm

        self.commands['cat'] = cp.cat

        self.commands['mv'] = cp.mv

        self.commands['rmdir'] = cp.rmdir

        self.commands['exit'] = cp.exit

        self.commands['wc'] = cp.wc

        self.commands['grep'] = cp.grep

        self.commands['history'] = cp.history

        self.commands['findhistory'] = cp.findhistory

        self.commands['help'] = cp.help

        self.commands['tail'] = cp.tail

        self.commands['head'] = cp.head

        self.commands['who'] = cp.who

        self.commands['sort'] = cp.sort

        self.commands['chmod'] = cp.chmod

        self.commands['less'] = cp.less



        self.possibleflag = par.flag()

        self.possibleDirections = par.direct()

        self.possibleparameters = par.possibleparameters()

        self.pipe = par.piped()

    # divides parameters into redirect,flag and parameters
    def parseArgs(self, **kwargs):

        flags = []

        params = []

        directions = []

        cmd = kwargs['cmd']

        args = kwargs['params']

        tag = kwargs['tag']

        thread =True

        indexArray = []

        readT = False

        if(len(args) > 0):

            for vals, i in zip(args, range(0, len(args))):

                if(vals not in indexArray):

                    if(vals in self.possibleparameters[cmd]):

                        indexArray.append(vals)

                        flags.append(vals)

                    elif(vals in self.possibleDirections):

                        if vals == '>':

                            vals = "w+"

                        elif vals == '>>':

                            vals = "a+"

                        elif vals == '<':

                            vals = "r+"
                            

                        directions.append(vals)

                        indexArray.append(vals)
                        
                        directions.append(args[i+1])

                        indexArray.append(args[i+1])

                    else:
                        
                            params.append(vals)

        else:

            args = None

        if (tag == True):

            return self.invoke(cmd=cmd, flags=flags, params=params, directions=directions,tag=tag)

        else:
           
            return self.invoke(cmd=cmd, flags=flags, params=params, directions=directions,thread =thread)

    #calls the appopriate function 
    def invoke(self, **kwargs):

        if 'cmd' in kwargs:

            cmd = kwargs['cmd']

        else:

            cmd = ''
            kwargs['cmd'] = cmd

        if 'params' in kwargs:

            params = kwargs['params']

        else:

            params = []
            kwargs['params'] = params

        if 'flags' in kwargs:

            flags = kwargs['flags']

        else:

            flags = []
            kwargs['flags'] =  flags 

        if 'directions' in kwargs:

            directions = kwargs['directions']

        else:

            directions = []
            kwargs['directions'] = directions

        if 'tag' in kwargs:

            tag = kwargs['tag']

        else:

            tag = False
            kwargs['tag'] = tag

        if 'thread' in kwargs:

            thread = kwargs['thread']

        else:

            thread = False

        # One way to invoke using dictionary

        if not thread:
            
            answer = self.commands[cmd](
                flags=flags, params=params, directions=directions, tag=tag)
            return answer

        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.commands[cmd],**kwargs )
                answer = future.result()
            return answer

           

            

    def exists(self, cmd):

        return cmd in self.commands




    #splits the command if it has a pipe 
    def splitcmd(self, cmd):
        
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "history.log"))

        while len(cmd.rstrip()) < 1:  # Check for empty lines
            print("Error: no command entered")
            cmd = input()
            

        cmdTest = cmd.split()[0]
        if  cmd == 'exit':
            sys.exit()

        if '!' in cmdTest:

            testhist = cmdTest[1:]

            if(str.isdigit(testhist)):

                cmd = cp.findhistory(testhist)
                print_cmd(cmd)

            else:

                print('invalid entry')

        with open(filepath, "a+") as log:
            log.write(f"{cmd}\n")

        tag = False
        
        answer = None

        if('|' in cmd):

            cmd2 = cmd.split('|')
            fmcmd = cmd2[0]
            length = len(cmd2)
            for i in range(0, len(cmd2)):
                split2 = cmd2[i].split()
                
                cmd = split2[0]
                
                
                params = split2[1:]
                
                if(i != length - 1):

                    if ch.exists(cmd):
                        
                        answer = self.parseArgs(
                            cmd=cmd, params=params, tag=tag)

                    else:
                        
                        answer = "Error: command %s doesn't exist." % (cmd)

                        break

                else:

                    if ch.exists(cmd):
                        tag = True
                        
                        if 'ls' in fmcmd:
                            answer = answer.replace('\n',',')
                            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                            result = ansi_escape.sub('', answer) 
                            splitedans = result.split("\t")
                            valin =[]
                            for item in splitedans:
                                if ',' in item:
                                    result = item.split(",")
                                    splitedans.remove(item)
                                    valin.extend(result)
                            splitedans.extend(valin)
                            
                            
                        else:
                            splitedans = answer.split("\n")
                        for item in splitedans:
                            params.append(item)
                       
                        answer = self.parseArgs(
                            cmd=cmd, params=params, tag=tag)

                    else:
                        
                        answer = "Error: command %s doesn't exist." % (cmd)

                        break
            
            if(answer == None):
                print('\r')
            else:
                print('\r')
                print(answer)

        else:

            cmd = cmd.split()

            params = cmd[1:]

            cmd = cmd[0]

            if ch.exists(cmd):
                
                answer = self.parseArgs(cmd=cmd, params=params, tag=tag)

            else:

                answer = "Error: command %s doesn't exist." % (cmd)
            
            if(answer == None):
                print('\r')
            else:
                print('\r')
                print(answer)



getch = gt.Getch() 
prompt = os.getcwd() + '>>' 
def print_cmd(cmd):
    """ This function "cleans" off the command line, then prints

        whatever cmd that is passed to it to the bottom of the terminal.

    """
    prompt = os.getcwd() + '>>'
    padding = " " * 80
    sys.stdout.write("\r"+padding)
    sys.stdout.write("\r"+prompt+cmd)
    sys.stdout.flush()

if __name__ == '__main__':
    cmd = ""
    print_cmd(cmd)
    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, "history.log"))
    currpos = -1
    index = len(cmd)
    ch = CommandHelper()
    while True:

        char = getch()  # read a character (but don't print)

        if char == '\x03' or cmd == 'exit': # ctrl-c
            raise SystemExit("\r")
        
        elif char == '\x7f':                # back space pressed
            cmd = cmd[:-1]
            print_cmd(cmd)
            
        elif char in '\x1b':                # arrow key pressed
            null = getch()                  # waste a character
            direction = getch()             # grab the direction
            
            if direction in 'A':            # up arrow pressed
                # get the PREVIOUS command from your history (if there is one)
                # prints out '↑' then erases it (just to show something)
                lastLine = ""
                with open(filepath, 'r') as f:
                    lastLine = f.readlines()[currpos]
                currpos -= 1
                cmd = lastLine
               
                cmd = cmd[:-1]
                
                
                
            if direction in 'B':            # down arrow pressed
                # get the NEXT command from history (if there is one)
                # prints out '↓' then erases it (just to show something)
                mrLine = ""
                if(currpos != -1):
                    with open(filepath, 'r') as f:
                        mrLine = f.readlines()[currpos]
                    currpos += 1
                    cmd = mrLine

                else:
                    cmd = ""
                cmd = cmd[:-1]
            
            if direction in 'C':            # left arrow pressed    
                # move the cursor to the LEFT on your command prompt line
                # prints out '←' then erases it (just to show something)
                
                direction='\033[<1>C'
                

            if direction in 'D':            # right arrow pressed
                # moves the cursor to the RIGHT on your command prompt line
                # prints out '→' then erases it (just to show something)
                direction='\033[<1>D'
               
            
            print_cmd(cmd)                  # print the command (again)

        elif char in '\r':                  # return pressed 
            
            # This 'elif' simulates something "happening" after pressing return
            if(cmd !=''):
            	ch.splitcmd(cmd)                  
                
            cmd = ""                        # reset command to nothing (since we just executed it)
            print_cmd(cmd)                  # now print empty cmd prompt
        else:
            cmd += char                     # add typed character to our "cmd"
            print_cmd(cmd)                  # print the cmd out
            
