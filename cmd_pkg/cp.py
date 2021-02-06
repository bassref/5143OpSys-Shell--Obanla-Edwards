import threading

import sys

import os

import glob

from pathlib import Path


def cp(**kwargs):
    """   
    NAME
        cp
    SYNOPSIS
        file1 file2	copy file1 and call it file2
    DESCRIPTION
       
       cp file1 file2	copy file1 and call it file2
    EXAMPLES
       cd test.txt test2.txt - read test.txt and write to test2.txt
    """
    command = ['cp']

    parameter = kwargs['params']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    if(len(parameter) == 2 and len(flag) == 0 and len(directions) == 0 and tag == False):

        file1 = parameter[0]

        file2 = parameter[1]

        f1path = Path(file1)

        f2path = Path(file2)

        if (os.path.isfile(file1)):

            test1 = os.path.isfile(file1)

            test2 = os.path.isfile(file2)

            permissionf1 = os.access(f1path, os.R_OK)

            permissionf2 = os.access(f2path, os.W_OK)

            if(permissionf1 == True):

                try:

                    f1 = open(file1, "r")

                    f2 = open(file2, "w")

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

    else:

        print("invalid arguments")
