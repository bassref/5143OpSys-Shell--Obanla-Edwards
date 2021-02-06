from os import path


def findhistory(num):
 
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

    
