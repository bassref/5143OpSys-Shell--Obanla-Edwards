
def sort(**kwargs):


    command = ['sort']

    parameter = kwargs["params"]

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']

    answer =''
    if(len(flag) == 0 and len(parameter) == 1 ):
        line =[]
        if tag == False:
            with open(parameter[0], "r+") as f:
                line = f.read().splitlines()
            line.sort()
        else:
            line = parameter[0].split('\n')
            line.sort()
        for x in line:
            answer = answer + x
            answer = answer +'\n'
        if(len(directions) == 2):
            direct = directions[0]
            file = directions[1]
            f = open(file, direct)
            f.write(answer)
            f.close()
        else:
            return answer
    else:
        answer ='invalid argument'
        return answer
   
        
