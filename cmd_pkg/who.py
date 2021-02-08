import getpass



def who(**kwargs):
    directions = kwargs['directions']
    answer = ""
    answer = getpass.getuser()
    if(len(directions) == 0):
        return answer
    elif(len(directions) == 2):
        direct = directions[0]
        file = directions[1]
        f = open(file, direct)
        f.write(answer)
        f.close()
    
    