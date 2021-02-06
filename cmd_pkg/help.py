



def help(**kwargs):
    cmd = kwargs['cmd']
    parameter = kwargs['params']
    if(len(parameter) ==1):
        tohelp = parameter[0]
        answer = tohelp.__doc__
        return answer

