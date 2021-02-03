import threading


import sys


import os


import glob


from pathlib import Path


def mkdir(**kwargs):

    command = ['mkdir']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    path = os.getcwd()

    length = len(parameter)

    answer = ""

    if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 0):

        answer = answer + "enter a directory name"

        return answer

    elif(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) >= 1):

        for directoryName in parameter:

            isdir = os.path.isdir(directoryName)

            permission = os.access(path, os.W_OK)

            newdirectory = os.path.join(path, directoryName)

            if(isdir == False and permission == True):

                try:

                    os.mkdir(newdirectory)

                except OSError as error:

                    answer = error

                    return answer

            elif(isdir == True):

                answer = answer + '{} already Exist'.format(directoryName)

                return answer

            elif(permission == False):

                answer = answer + "No write permission in current directory"

                return answer
