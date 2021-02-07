import os
from pathlib import Path
from os import path

def tail(**kwargs):

    command = ['tail']

    parameter = kwargs['params']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']
    answer = ''
    if(len(flag) >= 0 and len(parameter) > 0 and tag == False):
        if(len(flag) == 1 and flag[0] =='-n'):
            num = parameter[0]
            filename = parameter[1]
        else:
            num = 10
            filename = parameter[0]
        if(os.path.isfile(filename)):
            with open(filename) as file: 
                for line in (file.readlines() [-num:]): 
                    answer = answer + line.strip()
                    answer = answer +'\n'
                    num-=1
        else:
            answer = answer +"{} is not a file".format(filename)
        if(len(directions) == 2):
                    direct = directions[0]
                    fil = directions[1]
                    with open(fil, direct) as f:
                        f.write(answer)
                
        else:
            return answer
    elif(len(flag) >= 0 and len(parameter) == 1 and tag == True):
        lis = parameter[0].split('\n')
        length = len(lis)
        num =10
        if(len(flag) ==1 and flag[0] == '-n'):
            num = flag[0]
        elif(length <num ):
            num = length
        for i in range(length-num+1 ,length):
            answer = answer + lis[i]
            answer = answer + '\n'
        if(len(directions) == 2):
            direct = directions[0]
            fil = directions[1]
            with open(fil, direct) as f:
                f.write(answer)
                
        else:
            return answer
    else:
        answer ="invalid command"

       



