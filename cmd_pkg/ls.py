import threading

import sys
import colorama
from colorama import Fore, Style,Back
import os

import glob

import stat

from time import gmtime, strftime

import time

from pathlib import Path

import ntpath


def path_leaf(path):

    head, tail = ntpath.split(path)

    return tail or ntpath.basename(head)


def lslong(filename, islsah):

    answer = ""

    permission = {

        '0': "---",

        '1': "--x",

        '2': "-w-",

        '3': "-wx",

        '4': "r--",

        '5': "r-x",

        '6': "r-w",

        '7': "rwx"}

    filepath = Path(filename)

    fp = os.path.abspath(filename)

    actualPath = os.path.dirname(os.path.abspath(filename))

    name = path_leaf(actualPath)

    if(os.path.isfile(filename)):

        answer = answer + "-"

    elif(os.path.isdir(filename)):

        answer = answer + 'd'

    st = os.stat(fp)

    t = st.st_mtime

    if(islsah == True):

        size = st.st_size

    else:

        size = st.st_size

        if(size >= 1024 and size <= 1000000):

            size = size/1000

            size = (str(size)[:3])

            size = size + "K"

    now = int(time.time())

    recent = now - (6*30*24*60*60)  # 6 months ago

    if(t < recent) or (t > now):

        time_fmt = "%b %e %Y"

        time_str = time.strftime(time_fmt, time.gmtime(t))

    else:

        time_fmt = "%b %e %R"

        time_str = time.strftime(time_fmt, time.gmtime(t))

    allpermission = oct(st.st_mode)[-3:]

    for item in allpermission:

        answer = answer + "".join(permission[item])

    answer = answer + " "

    numoflinks = str(st.st_nlink)

    answer = answer + numoflinks

    answer = answer + " "

    if filepath.exists():

        answer = answer + filepath.owner()

        answer = answer + " "

        answer = answer + filepath.group()

        answer = answer + " "

    answer = answer + str(size)

    answer = answer + " "

    answer = answer + time_str

    answer = answer + " "

    answer = answer + filename

    return answer


def lsh(filename):

    actualPath = os.getcwd()

    listed = os.listdir(actualPath)

    return(listed)


def myFunc(e):

    return len(e)


def lsa(filename):

    z = glob.glob('.?*')

    filepath = Path(filename)

    actualPath = os.path.dirname(os.path.abspath(filename))

    l = glob.glob(os.path.join(actualPath, '*'))

    for i in range(len(l)):

        l[i] = path_leaf(l[i])

    l.extend(z)

    l = list(set(l))

    l.sort(reverse=True, key=myFunc)

    return (l)


def printlist(l):
    colorama.init(autoreset=True)
    answer = ""

    for i in range (0,len(l)):
        if(os.path.isdir(l[i])):
            l[i] = (Fore.BLUE + l[i] + Style.RESET_ALL ) 
    for i in range(len(l)//3+1):
        answer = answer + "\t " .join(l[i*3:(i+1)*3]) + "\n"
    return answer



def ls(**kwargs):


    command = ['ls']

    parameter = kwargs["params"]

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    actualPath = os.getcwd()

    filename = path_leaf(actualPath)

    l = glob.glob(os.path.join(actualPath, '*'))
    answer = ""

    if(len(flag) == 0 and len(parameter) == 0):

        listed = os.listdir(actualPath)

        answer = printlist(listed)
        return answer

    elif(len(flag) == 1 and len(parameter) == 0):

        longlist = []

        fl =flag[0]

        if(fl == '-l'):

            for files in l:

                name = path_leaf(files)

                val = lslong(name, True)

                longlist.append(val)

            for item in longlist:
                answer = answer + item
                answer = answer + "\n"
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        elif(fl == '-a'):

            val = lsa(filename)

            answer = printlist(val)
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        elif(fl == '-h'):

            val = lsh(filename)
            answer = printlist(val)
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        else:
            answer = "invalid parameter"
            return answer

    elif(len(flag) == 2 and len(parameter) == 0):

        longlsit = []

        if('-l' in flag and '-a' in flag):

            alla = lsa(filename)

            for file in alla:

                path = Path(file)

                pathh = path.resolve()

                filename2 = path_leaf(pathh)

                lsl = lslong(filename2, True)

                longlsit.append(lsl)

            for item in longlsit:
                answer = answer + item
                answer = answer + "\n"
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        elif('-a' in flag and '-h' in flag):

            val = lsh(filename)

            answer = printlist(val)
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        elif('-h' in flag and '-l' in flag):

            for files in l:

                name = path_leaf(files)

                val = lslong(name, False)

                longlsit.append(val)

            for item in longlsit:
                answer = answer + item
                answer = answer + "\n"
            if(len(directions) == 2):
                direct = directions[0]
                file = directions[1]
                f = open(file, direct)
                f.write(answer)
                f.close()
            else:
                return answer

        else:

            answer = "invalid flags"
            return answer

    else:

        answer = "invalid command"
        return answer
