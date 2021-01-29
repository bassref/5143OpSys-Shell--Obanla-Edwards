import threading
import os
import cmd_pkg as cp
from cmd_pkg import parameters as par


class CommandHelper(object):
    def __init__(self):
        self.commands = {}
        self.commands['ls'] = cp.ls
        self.commands['cd'] =cp.cd
        self.commands['pwd'] = cp.pwd
        self.commands['mkdir'] =cp .mkdir
        self.commands['cp'] =cp. cp
        self.commands['rm'] =cp. rm
        """ self.commands['cat'] = cat
        self.commands['pwd'] = pwd """
        self.commands['exit'] = exit

        self.possibleflag =par.flag()
        self.possibleDirections = par.direct()
        self.possibleparameters = par.possibleparameters()
        self.pipe = par.piped()

    def parseArgs(self,command,args):
        flags = []
        params =[]
        directions =[]
        pipe =[]
        cmd = command
        if(len(args)>0):
            for i, vals in args(range (0, len(args))):
                if(vals in self.possibleflag[cmd]):
                    flags.append(vals)
                elif(vals in self.possibleDirections):
                    if vals == '>':
                        vals = "w+"
                    elif vals == '>>':
                        vals = "a+"
                    elif vals == '<':
                        vals = "r+"
                    if i > 0 and not (str.isdigit(args[i-1])): #i >0 and the previous argument isn't a number
                        directions.append(args[i-1])
                    directions.append(vals)
                    directions.append(args[i+1])
                elif(vals in self.pipe):
                    pipe.append(args[i-1])
                    pipe.append(vals)
                    pipe.append(args[i+1])
                else:
                     params.append(vals)
        else:
            args = None
        self.invoke(cmd=cmd, flags=flags, params=params, directions=directions,pipe = pipe )



    def invoke(self, **kwargs):
        if 'cmd' in kwargs:
            cmd = kwargs['cmd']
        else:
            cmd = ''

        if 'params' in kwargs:
            params = kwargs['params']
        else:
            params = []

        if kwargs['flags']:
            flags = kwargs['flags']         
        else:
            flags = []

        if kwargs['directions']:
            for item in kwargs['directions']:
                if item == '>':
                    item = "w+"     #write
                elif item == '>>':
                    item = "a+"     #append
                elif item == '<':
                    item = "r+"     #read (but it will make a file if one does not exist)
            directions = kwargs['directions']                       
        else:
            directions = []

        if 'thread' in kwargs:
            thread = kwargs['thread']
        else:
            thread = False

        # One way to invoke using dictionary
        if not thread:
            self.commands[cmd](flags=flags, params=params, directions=directions)
        else:
            # Using a thread ****** broken right now *********
            if len(params) > 0:
                c = threading.Thread(target=self.commands[cmd], args=tuple(kwargs))
            else:
                c = threading.Thread(target=self.commands[cmd])

            c.start()
            c.join()
        
    def exists(self, cmd):
        return cmd in self.commands


if __name__ == '__main__':

    ch = CommandHelper()

    while True:
        # get input from terminal (use input if raw_input doesn't work)
        path = os.getcwd() + '>>'
        
        command_input = input(path)

        # remove command from params (very over simplified)
        command_input = command_input.split()

        # params are all but first position in list
        params = command_input[1:]

        # pull actual command from list
        cmd = command_input[0]

        # if command exists in our shell
        if ch.exists(cmd):
            
            ch.parseArgs(cmd, params)
        else:
            print("Error: command %s doesn't exist." % (cmd))