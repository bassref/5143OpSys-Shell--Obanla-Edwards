import threading
import sys
import os
import glob
from pathlib import Path



def mkdir(**kwargs):
	command = ['mkdir']
	parameter =kwargs['params']
	path = os.getcwd()
	length = len(parameter)
	if(length ==0):
		print("enter a name ")
	else:
		directoryName = parameter[0]
		isdir = os.path.isdir(directoryName) 
		permission = os.access(path, os.W_OK)
		newdirectory =os.path.join(path, directoryName)
		if(isdir == False and permission == True):
			try:
				os.mkdir(newdirectory) 
				os.chdir(newdirectory)
			except OSError as error:  
    				print(error) 
		elif(isdir == True):
			print("directory already Exist")
		elif(permission == False):
			print("No write permission in current directory")