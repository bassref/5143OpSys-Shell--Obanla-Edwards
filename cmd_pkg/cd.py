import sys

import os

from pathlib import Path


def cd(**kwargs):

    tag = kwargs['tag']

    if (tag == True):

        cdwithtag(**kwargs)

    else:

        cdwithouth(**kwargs)


def cdwithtag(**kwargs):

    command = ['cd']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 0):

        home = str(Path.home())

        return os.chdir(home)

    elif(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 1):

        directory = parameter[0]

        isdir = os.path.isdir(directory)

        if(isdir and os.access(directory, os.R_OK)):

            return os.chdir(directory)

        else:

            print("no such file or directory")

    elif(len(flag) == 1 and len(directions) == 0 and tag == False and len(parameter) == 0):

        if(flag[0] == '..'):

            path = os.getcwd()

            p = Path(path).parent

            if(os.access(p, os.R_OK)):

                return os.chdir(p)

            else:

                print("permission denied")

        elif(flag[0] == '~'):

            home = str(Path.home())

            return os.chdir(home)

    elif(len(flag) == 0 and len(directions) > 0 and tag == False and len(parameter) == 1):

        home = str(Path.home())

        return os.chdir(home)

    else:

        print("invalid parameters")


def cdwithouth(**kwargs):

    command = ['cd']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 0):

        home = str(Path.home())

        os.chdir(home)

    elif(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 1):

        directory = parameter[0]

        isdir = os.path.isdir(directory)

        if(isdir and os.access(directory, os.R_OK)):

            os.chdir(directory)

        else:

            print("no such file or directory")

    elif(len(flag) == 1 and len(directions) == 0 and tag == False and len(parameter) == 0):

        if(flag[0] == '..'):

            path = os.getcwd()

            p = Path(path).parent

            if(os.access(p, os.R_OK)):

                os.chdir(p)

            else:

                print("permission denied")

        elif(flag[0] == '~'):

            home = str(Path.home())

            os.chdir(home)

    elif(len(flag) == 0 and len(directions) > 0 and tag == False and len(parameter) == 1):

        home = str(Path.home())

        os.chdir(home)

    else:

        print("invalid parameters")
