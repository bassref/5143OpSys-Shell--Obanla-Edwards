import os
import threading
import sys
import glob
import shutil
from pathlib import Path

def cat(**kwargs):
    command = ['cat']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    length = len(parameter)
    answer = ''
    if(len(flag) == 0 and length > 0):

        if(tag == False):
            for p in parameter:
                lines = []
                with open(p, "r") as f:
                    lines = f.read().splitlines()
                for line in lines:
                    answer = answer + line
                    answer = answer + '\n'
            if(len(directions) == 2):
                direct = directions[0]
                fil = directions[1]
                with open(fil, direct) as f:
                    f.write(answer)
            else:
                return answer
        else:
            files = parameter
            for fil in files:
                lines =[]
                if(os.path.isfile(fil)):
                    with open(fil,'r') as f:
                        lines = f.read().splitlines()
                    for line in lines:
                        answer = answer + line
                        answer = answer +'\n'
                    if(len(directions) == 2):
                        direct = directions[0]
                        fil = directions[1]
                        with open(fil, direct) as fi:
                            fi.write(answer)
                    
                else:
                    answer = answer+ "{} is not a file".format(fil)
            return answer

    else:
        answer = "invalid parameters"
        return answer
			

