import os
from pathlib import Path


def cp(**kwargs):

    command = ['cp']

    parameter = kwargs['params']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']
    answer =''

    if(len(parameter) == 2 and len(flag) == 0 and len(directions) == 0 and tag == False):

        file1 = parameter[0]

        file2 = parameter[1]

        f1path = Path(file1)

        if (os.path.isfile(file1)):
            
            permissionf1 = os.access(f1path, os.R_OK)

            if(permissionf1 == True):
                f1 = open(file1, "r")

                f2 = open(file2, "w")

                for x in f1:

                    f2.write(x)

                f1.close()

                f2.close()

            else:

               answer = "insufficient permmision"
            return answer

        else:

            answer = "{} file does not exisit".format(file1)
            return answer

    else:
        answer = "invalid arguments"
        return answer
