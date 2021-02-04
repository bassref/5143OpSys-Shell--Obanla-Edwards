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
        
        keyword=parameter[0]
        for f in files:
            dic={}
            listlines=[]
            if(os.path.isfile(f)):
                fil=open(f, 'r')
                for lines in fil:
                    if(keyword in lines):
                        lines=lines.strip('\n')
                        listlines.append(lines)
                dic[f]=listlines
                allLines.append(dic)
            else:
               answer =  "{} is a directory".format(f)
               return answer
    else:
        answer = "invalid command"
        return answer
    if(len(flag) == 1):
        flag[0] == '-l'
        count =0
        for ans in allLines:
            key=list(ans.keys())[0]
            if(len(directions) == 0):
                answer=answer + key+ "\n"
               
            elif(len(directions) == 2):
                direct=directions[0]
                file=directions[1]
                f=open(file, direct)
                f.write(key)
                f.close()
        return answer
    else:
        count=0
        for ans in allLines:
            val=list(ans.values())
            if(len(directions) == 0):
                if(len(files) > 1):
                    for x in val:
                        key=list(ans.keys())[0]
                        count=count+1
                        for lis in x:
                           answer=answer + "{} : {}".format(key, lis)
                           answer=answer + "\n"
                    
                else:
                    for ans in allLines:
                        val=list(ans.values())
                        for x in val:
                            for y in x:
                                answer=answer + y
                                answer=answer + "\n"
                    
            elif(len(directions) == 2):
                direct=directions[0]
                file=directions[1]
                if(len(files) > 1):
                    for x in val:
                        key=list(ans.keys())[0]
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
        return answer
