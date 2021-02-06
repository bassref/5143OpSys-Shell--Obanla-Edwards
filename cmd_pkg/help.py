  
from os import path
def help(**kwargs):
    
    parameter = kwargs['params']
    cmd =''
    answer =""
    
    if(len(parameter) ==0):
        cmd ='help'
    elif(len(parameter) ==1):
        cmd = parameter[0]
    else:
        answer ='invalid argument'
        return answer

    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", f"help/{cmd}.txt"))
    with open(filepath,"r") as f:
        text = f.read()
    return text
