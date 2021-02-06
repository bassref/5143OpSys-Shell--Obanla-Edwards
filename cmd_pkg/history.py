from os import path


def history(**kwargs):
    """   
    NAME
        history - History log
    SYNOPSIS
        history
    DESCRIPTION
     show a history of all your commands
    EXAMPLES
       
    """
    redirect = kwargs['directions']
    histdic = {}
    count = 1
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "history.log"))
    answer =""
    f= open(filepath,'r')
    for lines in f:
        histdic[count]=lines
        if(len(redirect) ==0):
            answer = answer + "{}: {}".format(count , lines) +'\n'
        count+=1
    if (len(redirect) ==2):
        direct = redirect[0]
        fil = redirect[1]
        with open(fil,direct) as p :
            for key in histdic.keys():
                p.write(" {} :{}".format(key, histdic[key])) 
    else:
        return answer


    
    
			
		
		
	
