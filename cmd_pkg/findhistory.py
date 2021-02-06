from os import path


def findhistory(num):
    """   
    NAME
        !x
    SYNOPSIS
        ![INT]
    DESCRIPTION
     Load command x from your history so you can run it again
    EXAMPLES
            !2
            calls command 2 from the history log
       
    """
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..","history.log"))
    histDict = {}
    count = 1

    with open(filepath,'r') as f:
        for lines in f.readlines():
            lines = lines.strip()
            histDict[count] = lines
            count+=1
    return histDict[int(num)]

    
