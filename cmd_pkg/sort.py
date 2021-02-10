import os

def sort(**kwargs):

    command = ['sort']

    parameter = kwargs["params"]

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    answer = ''
    if(len(flag) == 0 and len(parameter) >= 1):
        line = []
        if tag == False:
            with open(parameter[0], "r+") as f:
                line = f.read().splitlines()
            line.sort()
        else:
            line = parameter
            line.sort()
        for x in line:
            answer = answer + x
            answer = answer + '\n'
        if(len(directions) == 2):
            direct = directions[0]
            file = directions[1]
            f = open(file, direct)
            f.write(answer)
            f.close()
        else:
            return answer
    elif(len(flag) == 0 and len(parameter) == 0 and len(directions) == 2):
        line =[]
        if(os.path.isfile(directions[1])):
            if(directions[0] == 'r+'):
                with open(directions[1], "r+") as f:
                    line = f.read().splitlines()
                line.sort()
                for x in line:
                    answer = answer + x
                    answer = answer + '\n'
            return answer
        else:
            answer = answer +"{} is not a file".format(directions[1])
            return answer
    else:
        answer = 'invalid argument'
        return answer
