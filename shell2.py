import threading

import os

from numpy.core.records import array

import cmd_pkg as cp

from cmd_pkg import parameters as par


import numpy as np


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

        self.possibleflag = par.flag()

        self.possibleDirections = par.direct()

        self.possibleparameters = par.possibleparameters()

        self.pipe = par.piped()

    def parseArgs(self, **kwargs):

        flags = []

        params = []

        directions = []

        cmd = kwargs['cmd']

        args = kwargs['params']

        tag = kwargs['tag']

        indexArray = []

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

                            directions.append(args[i-1])

                            indexArray.append(args[i-1])

                        directions.append(vals)

                        indexArray.append(vals)

                        directions.append(args[i+1])

                        indexArray.append(args[i+1])

                    else:

                        params.append(vals)

        else:

            args = None

        if (tag == True):

            return self.invoke(cmd=cmd, flags=flags, params=params, directions=directions, tag=tag)

        else:

            return self.invoke(cmd=cmd, flags=flags, params=params, directions=directions)

    def invoke(self, **kwargs):

        if 'cmd' in kwargs:

            cmd = kwargs['cmd']

        else:

            cmd = ''

        if 'params' in kwargs:

            params = kwargs['params']

        else:

            params = []

        if 'flags' in kwargs:

            flags = kwargs['flags']

        else:

            flags = []

        if 'directions' in kwargs:

            directions = kwargs['directions']

        else:

            directions = []

        if 'tag' in kwargs:

            tag = kwargs['tag']

        else:

            tag = False

        if 'thread' in kwargs:

            thread = kwargs['thread']

        else:

            thread = False

        # One way to invoke using dictionary

        if not thread:

            return self.commands[cmd](flags=flags, params=params, directions=directions, tag=tag)

        else:

            # Using a thread ****** broken right now *********

            if len(params) > 0:

                c = threading.Thread(
                    target=self.commands[cmd], args=tuple(kwargs))

            else:

                c = threading.Thread(target=self.commands[cmd])

            c.start()

            c.join()

    def exists(self, cmd):

        return cmd in self.commands


if __name__ == '__main__':

    ch = CommandHelper()

    while True:

        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "history.log"))
        path = os.getcwd() + '>>'

        command_input = input(path)
        while len(command_input.rstrip()) < 1:  # Check for empty lines
            print("Error: no command entered")
            command_input = input(">>")

        cmdTest = command_input.split()[0]
        if '!' in cmdTest:
            testhist = cmdTest[1:]
            if(str.isdigit(testhist)):
                command_input = cp.findhistory(testhist)
            else:
                print('invalid entry')

        with open(filepath, "a+") as log:
            log.write(f"{command_input}\n")

        tag = False

        answer = ""

        if('|' in command_input):

            command_input = command_input.split('|')

            length = len(command_input)

            for i in range(0, len(command_input)):

                split2 = command_input[i].split()

                cmd = split2[0]

                params = split2[1:]

                if(i != length - 1):

                    if ch.exists(cmd):

                        answer = ch.parseArgs(cmd=cmd, params=params, tag=tag)

                    else:

                        answer = "Error: command %s doesn't exist." % (cmd)

                        break

                else:

                    if ch.exists(cmd):
                        tag = True
                        params.append(answer)

                        answer = ch.parseArgs(cmd=cmd, params=params, tag=tag)

                    else:

                        answer = "Error: command %s doesn't exist." % (cmd)

                        break

            print(answer)

        else:

            command_input = command_input.split()

            # params are all but first position in list

            params = command_input[1:]

            # pull actual command from list

            cmd = command_input[0]

            # if command exists in our shell

            if ch.exists(cmd):

                answer = ch.parseArgs(cmd=cmd, params=params, tag=tag)

            else:

                answer = "Error: command %s doesn't exist." % (cmd)

            print(answer)
