import sys

import os

from pathlib import Path


def cd(**kwargs):
   
    command = ['cd']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']
    answer =""
    if(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 0):

        home = str(Path.home())
        os.chdir(home)
        return answer
    elif(len(flag) == 0 and len(directions) == 0 and tag == False and len(parameter) == 1):

        directory = parameter[0]

        isdir = os.path.isdir(directory)

        if(isdir and os.access(directory, os.R_OK)):

            os.chdir(directory)
            
        else:
            answer= answer + "no such file or directory"
            answer=answer + "\n"
        return answer
    elif(len(flag) == 1 and len(directions) == 0 and tag == False and len(parameter) == 0):

        if(flag[0] == '..'):

            path = os.getcwd()

            p = Path(path).parent

            if(os.access(p, os.R_OK)):

                os.chdir(p)
            else:
                answer= answer + "permission denied"
                answer=answer + "\n"
            return answer
        elif(flag[0] == '~'):

            home = str(Path.home())
            os.chdir(home)
        return answer
           

    elif(len(flag) == 0 and len(directions) > 0 and tag == False and len(parameter) == 1):

        home = str(Path.home())
        os.chdir(home)
        return answer
      

    else:
        answer= answer + "invalid parameters"
        answer=answer + "\n"
        return answer
        
