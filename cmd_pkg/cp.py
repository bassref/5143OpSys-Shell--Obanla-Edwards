import os
import shutil
from pathlib import Path
from os.path import isfile


def cp(**kwargs):
    command = ['cp']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    length = len(parameter)
    answer = ''
    value =''
    lenm = int(length - 1)
    if("" in parameter):
        parameter.remove("")
   
    if(len(flag) == 0 and length >= 2):
        para = parameter[:-1]
        destination = parameter[-1]
        for source in para:
            if(os.path.exists(source) & os.path.exists(destination)):
                try:
                    shutil.copy(source, destination)
                except Exception as e:
                    answer = e                    
            else:
                answer = answer + \
                    "{} or {} does not exist".format(source, destination)
                answer = answer + '\n'
        if(len(directions) == 2):
            direct = directions[0]
            fil = directions[1]
            if(os.path.isfile(destination)):
                with open(destination, 'r') as d:
                    value = d.read()
                with open(fil, direct) as f:
                        f.write(value)
            else:
                answer = answer + "{} was a file".format(destination)
        return answer

    else:
        answer = "invalid parameters"
        return answer
