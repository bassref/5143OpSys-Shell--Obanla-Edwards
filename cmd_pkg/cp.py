import threading
import sys
import os
import glob
from pathlib import Path


def cp(**kwargs):
	command = ['cd']
	parameter =kwargs['params']
	length = len(parameter)
	if(length <2):
		print("two files required to copy")
	else:
		
		file1 = parameter[0]
		file2 = parameter[1]
		f1path = Path(file1)
		f2path = Path(file2)
		permissionf1 = os.access(f1path, os.R_OK)
		permissionf2 = os.access(f2path, os.W_OK)
		if (os.path.isfile(file1) and os.path.isfile(file2)):
			test1= os.path.isfile(file1)
			print(test1)
			test2 = os.path.isfile(file2)
			print(test2)
			if(permissionf1 == True and permissionf2 == True):
				try:
					f1 = open(file1,"r")
					f2 = open(file2,"w")
					for x in f1:
						f2.write(x)
					f1.close()
					f2.close()
					print("copy complete")
				except IOError as error:
					print(error)
			else:
				print("insufficient permmision")
		else:
			
			print("file does not exisit")