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

    if(len(parameter) >= 2):
        keyword = parameter[0]
        dic = {}
        for f in files:
            listlines = []
            if(os.path.isfile(f)):
                fil = open(f, 'r')
                for lines in fil:
                    if(keyword in lines):
                        lines = lines.strip('\n')
                        listlines.append(lines)
                dic[f] = listlines
            else:
                print("{} is a directory".format(f))
        allLines.append(dic)
    else:
        print("invalid command")
    if(len(flag) == 1):
        flag[0] == '-l'
        for ans in allLines:
            key = str(ans.keys())
            print(key)

    else:

        count = 0
        for ans in allLines:
            val = list(ans.values())
            if(len(files) > 1):
                for x in val:
                    key = list(ans.keys())[count]
                    count = count+1
                    for lis in x:
                        print("{} : {}".format(key, lis))
            else:
                for ans in allLines:
                    val = list(ans.values())
                    for x in val:
                        print(*x)
