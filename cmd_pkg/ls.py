import threading

import sys

import os

import glob

import stat

from time import gmtime, strftime

import time

from pathlib import Path







def lslong (filename):

    listanswer =[]

    answer =""

    permission = {

        '0':"---",

        '1':"--x",

        '2':"-w-",

        '3':"-wx",

        '4':"r--",

        '5':"r-x",

        '6':"r-w",

        '7':"rwx"}

    filepath = Path(filename)

    actualPath = filepath.resolve()

    if(os.path.isfile(filename)):

	    answer= answer + "-"

    elif(os.path.isdir(filename)):

	    answer= answer + 'd'

    st = os.stat(filepath)

    t = st.st_mtime

    now = int(time.time())

    recent = now - (6*30*24*60*60) #4 months ago

    if(t<recent) or (t> now):

	    time_fmt = "%b %e %Y"

    else:

        time_fmt = "%b %e %R"

        time_str = time.strftime(time_fmt, time.gmtime(t))

    allpermission = oct(st.st_mode)[-3:]

   

    for item in allpermission:

        answer =answer + "".join(permission[item])

    answer= answer + " "

    numoflinks = str(st.st_nlink)

    answer = answer+ numoflinks

    answer = answer + " "

    if actualPath.exists():

        answer = answer + actualPath.owner()

        answer= answer + " "

        answer = answer + actualPath.group()

        answer= answer + " "

    answer = answer + str(st.st_size)

    answer= answer + " "

    answer = answer + time_str

    return answer

        

def lsh(filename):

    filepath = Path(filename)

    actualPath = filepath.resolve()

    print(actualPath)

    l = os.listdir(actualPath)

    return(l)

def myFunc(e):

  return len(e)



def lsa(filename):

	z = glob.glob('.?*')

	filepath = Path(filename)

	actualPath = filepath.resolve()

	l = os.listdir(actualPath)

	l.extend(z)

	l = list(set(l))

	l.sort(reverse = True ,key =myFunc)

	return (l)

	

    	

def printlist(l):

	

	for i in range(len(l)//3+1):

    		print( "\t " .join(l[i*3:(i+1)*3]) + "\n")



		

def ls(**kwargs):

	

	command = ['ls']

	parameter= kwargs["params"]

	flag = kwargs['flags']

	directions = kwargs['directions']

	tag = kwargs['tag']

	

	if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 0):

		actualPath = os.getcwd()

		

		l = os.listdir(actualPath)

		printlist(l)

		

		

	

	