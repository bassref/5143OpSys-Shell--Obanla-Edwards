import threading
import sys
import os
import glob
from pathlib import Path


def checkstart(name):
    x = glob.glob(name)
    return x


def doflen(name):
    pathh = os.path.abspath(name)
    dirlen = os.listdir(pathh)
    if(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):
        if(len(dirlen) == 0):
            return True
    else:
        return False


def deleteDir(directory):
    p = Path(directory)
    answer = ""
    pathh = os.path.abspath(directory)
    if(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):
        currentdirectory = Path.cwd()
        dirlen = os.listdir(pathh)
        if(len(dirlen) == 0):
            os.rmdir(pathh)
            answer = answer + \
                'directory: {0} has been removed'.format(directory)
            
        return answer

    else:
        answer = answer + "directory does not exist"
    return answer


def rmdir(**kwargs):

    command = ['rm']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    answer = ""
    if(len(flag) == 0 and len(directions) == 0  and len(parameter) > 0):
        for directory in parameter:
            p = Path(directory)
            pathh = os.path.abspath(directory)
            if('*' in directory):
                listoffiles = checkstart(directory)
                for direct in listoffiles:
                    pathh2 = os.path.abspath(direct)
                    if(os.path.isdir(pathh2) and os.access(pathh2, os.R_OK)):
                        length = doflen(direct)
                        if(length == True):
                            answer = answer + deleteDir(direct)
                        else:
                            answer = answer + "{} not empty".format(direct)
                            answer = answer +'\n'
                       
                    else:
                        answer = answer + \
                            "{} cannot delete file".format(direct)
                        answer = answer +'\n'
                
                        

            else:

                if(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):
                    length = doflen(directory)
                    if(length == True):
                        answer = answer + deleteDir(directory)
                    else:
                        answer = answer + "{} not empty".format(directory)
                        answer = answer +'\n'
                else:
                    answer = answer + "{} cannot delete file".format(directory)
                    answer = answer +'\n'
            return answer
    else:
        answer = answer + "not enough arguments"
    return answer
