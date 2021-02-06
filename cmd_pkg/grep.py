import sys
import os


def grep(**kwargs):
    """   
    NAME
        grep 'keyword' file	search a file(s) files for keywords and print lines where pattern is found
    SYNOPSIS
        grep 'keyword' file
    DESCRIPTION
    grep -l	only return file names where the word or pattern is found
    EXAMPLES
        grep -l count test.tXt
            searches for count in test.txt
    """
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
                with open(f, 'r') as fil:
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
                with open(file, direct) as f:
                    f.write(key)
                
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
                    with open(file, direct) as f:
                        f.write(answer)
                   

                else:
                    for ans in allLines:
                        val=list(ans.values())
                        for x in val:
                            for y in x:
                                answer=answer + y
                                answer=answer + "\n"
                    with open(file, direct) as f:
                        f.write(answer)
                    
        return answer
