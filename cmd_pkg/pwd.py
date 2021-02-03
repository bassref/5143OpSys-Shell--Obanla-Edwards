import threading

import sys

import os

import glob

from pathlib import Path


def pwd(**kwargs):
    directions = kwargs['directions']

    answer = ""

    path = os.getcwd()
    answer = answer + "current working directory: " + str(path)
    if(len(directions) == 0):

        return answer
    elif(len(directions) == 2):
        direct = directions[0]
        file = directions[1]
        f = open(file, direct)
        f.write(answer)
        f.close()
