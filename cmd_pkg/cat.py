import os
import threading
import sys
import glob
import shutil
from pathlib import Path
 #If the parameters are just files, print them on the screen
def cat(**kwargs):
	command = ['cat']
	params = kwargs['params']
	flag = kwargs['flags'] 
	directions = kwargs['directions']  
	tag = kwargs['tag']
	length = len(params)
	filecount = 0
	for p in params:
		with open(params[filecount], "r") as f:
			lines = f.read().splitlines()
	for line in lines:
		print(line)
	print(" ")
	filecount+=1