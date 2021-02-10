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
    
    if(len(parameter) >= 2 and tag == False):
        keyword = parameter[0]
        for f in files:
            dic = {}
            listlines = []
            if(os.path.isfile(f)):
                with open(f, 'r') as fil:
                    for lines in fil:
                        if(keyword in lines):
                            lisj = []
                            lines = lines.strip('\n')
                            spliedline = lines.split()
                            for i in range(0, len(spliedline)):
                                if(spliedline[i] == keyword):
                                    A = spliedline[i]
                                    s = "\033[91m {}\033[00m" .format(A)
                                    lisj.append(s)
                                else:
                                    lisj.append(spliedline[i])
                            lines = " ".join(lisj)
                            listlines.append(lines)
                dic[f] = listlines
                allLines.append(dic)
            else:
                answer = answer + "{} is a directory".format(f)
                answer = answer + '\n'

        if(len(flag) == 1):
            flag[0] == '-l'
            count = 0
            for ans in allLines:
                key = list(ans.keys())[0]
                if(len(directions) == 0):
                    answer = answer + key
                    answer = answer + '\n'

                elif(len(directions) == 2):
                    direct = directions[0]
                    file = directions[1]
                    with open(file, direct) as f:
                        f.write(key)

            return answer
        else:
            count = 0
            for ans in allLines:
                val = list(ans.values())
                if(len(directions) == 0):
                    if(len(files) > 1):
                        for x in val:
                            key = list(ans.keys())[0]
                            count = count+1
                            for lis in x:
                                answer = answer + "{} : {}".format(key, lis)
                                answer = answer + "\n"

                    else:
                        for ans in allLines:
                            val = list(ans.values())
                            for x in val:
                                for y in x:
                                    answer = answer + y
                                    answer = answer + "\n"

                elif(len(directions) == 2):
                    direct = directions[0]
                    file = directions[1]
                    if(len(files) > 1):
                        for x in val:
                            key = list(ans.keys())[0]
                            count = count+1
                            for lis in x:
                                answer = answer + "{} : {}".format(key, lis)
                                answer = answer + "\n"
                        with open(file, direct) as f:
                            f.write(answer)

                    else:
                        for ans in allLines:
                            val = list(ans.values())
                            for x in val:
                                for y in x:
                                    answer = answer + y
                                    answer = answer + "\n"
                        with open(file, direct) as f:
                            f.write(answer)

            return answer

    elif(len(parameter) >= 2 and tag == True):
        keyword = parameter[0]
        tolook = parameter[1:]
        count =0
       
        listlines = []
        for lines in tolook:
            if(keyword in lines):
                lisj = []
                lines = lines.strip('\n')
                spliedline = lines.split()
                for i in range(0, len(spliedline)):
                    if(spliedline[i] == keyword):
                        count+=1
                        A = spliedline[i]
                        s = "\033[91m {}\033[00m" .format(A)
                        lisj.append(s)
                    else:
                        lisj.append(spliedline[i])
                lines = " ".join(lisj)
                listlines.append(lines)
        
        if(len(directions) == 2):
            direct = directions[0]
            file = directions[1]
            value = "\n".join(listlines)
            with open(file, direct) as f:
                f.write(value)
        else:
            answer = "\n".join(listlines)
            return answer
    elif(len(flag) == 0 and len(parameter) == 1 and len(directions) == 2):
        
        listlines = []
        keyword = parameter[0]
       
        if(os.path.isfile(directions[1])):
            if(directions[0] == 'r+'):
                with open(directions[1], "r+") as fil:
                    for lines in fil:
                        if(keyword in lines):
                            lisj = []
                            lines = lines.strip('\n')
                            spliedline = lines.split()
                            for i in range(0, len(spliedline)):
                                if(spliedline[i] == keyword):
                                    A = spliedline[i]
                                    s = "\033[91m {}\033[00m" .format(A)
                                    lisj.append(s)
                                else:
                                    lisj.append(spliedline[i])
                            lines = " ".join(lisj)
                            listlines.append(lines)
            for item in listlines:
                answer = answer + item
                answer = answer +"\n"  
            return answer
        else:
            answer = answer +"{} is not a file".format(directions[1])
            return answer
        
    else:
        answer = "invalid command"
        return answer
