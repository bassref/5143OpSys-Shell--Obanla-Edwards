import threading
import sys
import os
import glob
from pathlib import Path



def rm(**kwargs):
	command = ['rm']
	parameter =kwargs['params']
	length = len(parameter)
	if('-r' not in parameter and '*' not in parameter):
		for filordir in parameter:
			path = Path(filordir)
			if(os.path.isfile(filordir) and os.access(path, os.R_OK)):
				pathh = path.resolve()
				os.remove(pathh)
				print(' file: {} has been removed'.format(filordir))
			elif(os.path.isdir(filordir) and os.access(path, os.R_OK)):
				pathh = path.resolve()
				dir =os.listdir(pathh)
				if(len(dir) ==0):
					os.rmdir(pathh)
					print(' directory: {} has been removed'.format(filordir))
				else:
					print("directory not empty")
			else:
				print("file does not exisit")
	elif(len(parameter) == 1 and '*' in parameter[0]):
		wildcard = parameter[0]
		dot = '.'
		subWildcard ="".join(c for c in s if c.isalnum())
		if ('*' in wildcard and '.'in wildcard):
			subwildcard1 = dot + subwildcard
			f = glob.glob(subwildcard1)
			for filordir in f:
				path = Path(subWildcard)
				pathh = path.resolve()
				if(os.path.isfile(filordir) and os.access(path, os.R_OK)):
					os.remove(pathh)
					print(' file: {} has been removed'.format(filordir))
				elif(os.path.isdir(filordir) and os.access(path, os.R_OK)):
					pathh = path.resolve()
					dir =os.listdir(pathh)
					if(len(dir) ==0):
						os.rmdir(pathh)
						print(' directory: {} has been removed'.format(filordir))
					else:
						print("directory not empty")
				else:
					print("file does not exisit")
		elif('*' in wildcard and '.' not in wildcard ):
			f = glob.glob(subwildcard)
			for filordir in f:
				path = Path(subWildcard)
				pathh = path.resolve()
				if(os.path.isfile(filordir) and os.access(path, os.R_OK)):
					os.remove(pathh)
					print(' file: {} has been removed'.format(filordir))
				elif(os.path.isdir(filordir) and os.access(path, os.R_OK)):
					pathh = path.resolve()
					dir =os.listdir(pathh)
					if(len(dir) ==0):
						os.rmdir(pathh)
						print(' directory: {} has been removed'.format(filordir))
					else:
						print("directory not empty")
				else:
					print("file does not exisit")