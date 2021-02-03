import sys
import os


def grep(**kwargs):
    command = ['grep']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']

    files = parameter[1:]
    allLines = []
    answer = ""
    print(parameter)
    print(directions)
    print(type(directions))

    if(len(parameter) >= 2 and len(flag) == 0):
        keyword=parameter[0]
        dic={}
        for f in files:
            listlines=[]
            if(os.path.isfile(f)):
                fil=open(f, 'r')
                for lines in fil:
                    if(keyword in lines):
                        lines=lines.strip('\n')
                        listlines.append(lines)
                dic[f]=listlines
            else:
                print("{} is a directory".format(f))
        allLines.append(dic)
    else:
        print("invalid command")
    if(len(flag) == 1):
        flag[0] == '-l'
        for ans in allLines:
            key=str(ans.keys())
            if(len(directions) == 0):
                answer=answer + key
                answer=answer + "\n"
                return answer
            elif(len(directions) == 2):
                direct=directions[0]
                file=directions[1]
                f=open(file, direct)
                f.write(key)
                f.close()
    else:
        count=0
        for ans in allLines:
            val=list(ans.values())
            if(len(directions) == 0):
                if(len(files) > 1):
                    for x in val:
                        key=list(ans.keys())[count]
                        count=count+1
                        for lis in x:
                           answer=answer + "{} : {}".format(key, lis)
                           answer=answer + "\n"
                    return answer
                else:
                    for ans in allLines:
                        val=list(ans.values())
                        for x in val:
                            for y in x:
                                answer=answer + y
                                answer=answer + "\n"
                    return answer
            elif(len(directions) == 2):
                direct=directions[0]
                file=directions[1]
                if(len(files) > 1):
                    for x in val:
                        key=list(ans.keys())[count]
                        count=count+1
                        for lis in x:
                           answer=answer + "{} : {}".format(key, lis)
                           answer=answer + "\n"
                    f=open(file, direct)
                    f.write(answer)
                    f.close()

                else:
                    for ans in allLines:
                        val=list(ans.values())
                        for x in val:
                            for y in x:
                                answer=answer + y
                                answer=answer + "\n"
                    f=open(file, direct)
                    f.write(answer)
                    f.close()
