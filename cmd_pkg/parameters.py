def possibleparameters():

    ppFlag ={}

    ppFlag['ls'] = ['-a','-l','-h']

    ppFlag['mkdir'] =[]

    ppFlag['cd'] =['~','..']

    ppFlag['pwd'] =[]

    ppFlag['cp'] =[]

    ppFlag['mv'] =[]

    ppFlag['rm'] =['-r']

    ppFlag['rmdir'] =[]

    ppFlag['cat'] =[]

    ppFlag['less'] =[]

    ppFlag['tali'] =['-n']

    ppFlag['head'] =['-n']

    ppFlag['grep'] = ['-l']

    ppFlag['tail'] =['-n']

    ppFlag['wc'] =['-l','-m','-w']

    ppFlag['help'] =[]

    ppFlag['who'] =[]

    ppFlag['sort'] =[]

    ppFlag['chmod'] =[]





    return ppFlag

def flag():

    flags =['~','*','-a','-b','-l','-h','-r','-m','-w','..','-n']

    return flags



def direct():

    directions = ['>','>>','<', '&']

    return directions



def piped():

    pipe =['|']

    return pipe