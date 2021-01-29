def cd(**kwargs):
	
	command = ['cd']
	parameter =kwargs['params']
	length = len(parameter)
	if(length ==0):
		home = str(Path.home())
		os.chdir(home)
	if(length>0):
		directory = parameter[0]
		directoryLength = len(directory)
		if(directory =='~'):
			home = str(Path.home())
			os.chdir(home)
		if(directory =='..'):
			path = os.getcwd()
			p=Path(path).parent
			if(os.access(p ,os.R_OK)):
				os.chdir(p) 
			else:
				print("permission denied")
		if(directoryLength > 1):
			isdir = os.path.isdir(directory) 
			if(isdir and os.access(directory, os.R_OK)):
				os.chdir(directory)
			else:
				print("no such file or directory")