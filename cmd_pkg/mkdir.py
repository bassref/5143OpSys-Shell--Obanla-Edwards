import threading

import sys

import os

import glob

from pathlib import Path



def mkdir(**kwargs):

	command = ['mkdir']

	parameter =kwargs['params']

	flag = kwargs['flags'] 

	directions = kwargs['directions']  

	tag = kwargs['tag']

	path = os.getcwd()

	length = len(parameter)

	if(len(flag) == 0 and len(directions)== 0 and tag ==False and len(parameter) ==0):

		print("enter a directory name")

	elif(len(flag) == 0 and len(directions)== 0 and tag ==False and len(parameter) >1):

		for directoryName in parameter:

			isdir = os.path.isdir(directoryName) 

			permission = os.access(path, os.W_OK)

			newdirectory =os.path.join(path, directoryName)

			if(isdir == False and permission == True):

				try:

					os.mkdir(newdirectory) 

				except OSError as error:  

	    				print(error) 

			elif(isdir == True):

				print('{} already Exist'.format(directoryName))

			elif(permission == False):

				print("No write permission in current directory")