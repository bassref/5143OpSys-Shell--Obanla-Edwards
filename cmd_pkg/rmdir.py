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
    answer =""
    pathh = os.path.abspath(directory)
    if(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):
        currentdirectory = Path.cwd()
        dirlen = os.listdir(pathh)
        if(len(dirlen) == 0):
            os.rmdir(pathh)
            answer =answer + 'directory: {0} has been removed'.format(directory)
            return answer

    else:
        answer =answer +"directory does not exist"
        return answer


def rmdir(**kwargs):
    """   
    NAME
        rmdir
    SYNOPSIS
        rmdir  [file(s)]
    DESCRIPTION
     rmdir -remove a directory
    EXAMPLES
            rmdir  test
            remove directory  test if its empty
       
    """
    command = ['rm']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    answer =""
    if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) > 0):
        for directory in parameter:
            p = Path(directory)
            pathh = os.path.abspath(directory)
            if('*' in directory):
                listoffiles = checkstart(directory)
                for direct in listoffiles:
                    length = doflen(direct)
                    pathh2 = os.path.abspath(direct)
                    if(os.path.isdir(pathh2) and os.access(pathh2, os.R_OK)):
                        if(length == True):
                            deleteDir(direct)
                        else:
                            answer =answer + "{} not empty".format(direct)
                            return answer
                            
                    else:
                        answer =answer + "{} cannot delete file".format(direct)
                        return answer

            else:
                length = doflen(directory)
                if(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):
                    if(length == True):
                        deleteDir(directory)
                else:
                     answer =answer +"{} cannot delete file".format(directory)
                     return answer
    else:
         answer =answer +"not enough arguments"
         return answer
