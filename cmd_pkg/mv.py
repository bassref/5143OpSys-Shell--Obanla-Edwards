import os
import threading
import sys
import glob
import shutil
from pathlib import Path



#function to move a file
def mv(**kwargs):
	command = ['mv']
	parameter = kwargs['params']
	parameter =kwargs['params']
	flag = kwargs['flags'] 
	directions = kwargs['directions']  
	tag = kwargs['tag']
	length = len(parameter)
	path = os.getcwd()
	#if there are not enough parameters
	if(len(parameter) <2 and len(flag) == 0 and len(directions)== 0 and tag ==False):
		print("not enough arguments given")
	else:
		file1 = parameter[0]
		for x in range(length-1):
			toMove = parameter[x]
			source = path+"/"+toMove			
			destination = path+"/"+parameter[length-1]
			if(os.path.exists(source) & os.path.exists(destination)):
				shutil.move(source,destination)
