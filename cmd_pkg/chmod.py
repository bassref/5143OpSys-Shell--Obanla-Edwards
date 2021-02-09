import os

from os import path


def chmod (**kwargs):
    command = ['chmod']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    answer = ""
    if(len(flag) == 0 and len(parameter) == 0):
        answer = " enter file name and mode"
        return answer
    elif(len(flag) == 0 and len(parameter) >= 2):
        if(len(parameter[0]) == 3 and int(parameter[0]) >= 0 and int( parameter[0] )<= 777 ):
            mode = int(parameter[0],8)
            rext = parameter[1:]
            for item in rext:
                if(os.path.exists(item)):
                    os.chmod(item,mode)
                else:
                    answer = answer + "{} does not exist".format(item)
                    answer = answer +'\n'
            return answer
        else:
            answer = " enter a three digit number between 000 and 777"
            return answer
    else:
        answer = "enter invalid input"
        return answer
