import threading
import sys
import os
import glob
from pathlib import Path

def ls(**kwargs):
	parameter= kwargs["params"]
	PParameter = ['-a','-h','-l']
	redirect = ['|','<','>','>>']
	if(len(parameter)==0):
		for py in glob.glob("*"):
			print(py)
