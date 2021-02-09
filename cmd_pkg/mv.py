import os

from os.path import isfile

import shutil

from pathlib import Path


# function to move a file

def mv(**kwargs):

    command = ['mv']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    length = len(parameter)
    lenm = int(length - 1)

 

    answer = ""

    # if there are not enough parameters

    if(len(parameter) < 2 and len(flag) == 0 and len(directions) == 0 and tag == False):

        answer = "not enough arguments given"

        return answer

    elif(len(parameter) >= 2 and len(flag) == 0 and len(directions) == 0 and tag == False):

        para = parameter[:lenm]

        destination = parameter[-1]

        for source in para:

            if(os.path.exists(source) & os.path.exists(destination)):
                try:

                    shutil.move(source, destination)
                except Exception as e:
                    answer = e       

            else:

                answer = answer + \
                    "{} or {} does not exist".format(source, destination)

        return answer

    else:

        answer = "invalid argument"

        return answer
