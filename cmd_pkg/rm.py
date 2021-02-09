import os

import glob

from pathlib import Path


def checkstart(name):

    x = glob.glob(name)

    return x


def deletefile(filename):

    answer = ""
    filepath = Path(filename)

    if(os.path.isfile(filename) and os.access(filepath, os.R_OK)):

        actualPath = filepath.resolve()

        os.remove(actualPath)
        return answer

    elif(os.path.isdir(filename)):

        answer = answer + 'cannot remove {}  directory'.format(filename)
        return answer

    else:

        answer = answer + 'file {} does not exits'.format(filename)
        return answer


def deleteDir(directory):

    p = Path(directory)
    answer = ""

    if(os.path.isdir(directory) and os.access(p, os.R_OK)):

        currentdirectory = Path.cwd()

        x = p.resolve()

        os.chdir(x)

        listd = os.listdir(x)

        for filee in listd:

            pathh = os.path.abspath(filee)

            if(os.path.isfile(filee) and os.access(pathh, os.R_OK)):

                os.remove(pathh)
                
            elif(os.path.isdir(pathh) and os.access(pathh, os.R_OK)):

                dir = os.listdir(pathh)

                if(len(dir) == 0):

                    os.rmdir(pathh)
                    

                else:

                    answer = answer + "contains a directory that is not empty"
                    answer = answer +'\n'
            

        dirlen = os.listdir(x)

        if(len(dirlen) == 0):

            os.rmdir(x)
            os.chdir(currentdirectory)
        return answer

    else:

        answer = answer + "directory does not exist"
        
        return answer


def rm(**kwargs):

    command = ['rm']

    parameter = kwargs['params']

    flag = kwargs['flags']

    directions = kwargs['directions']

    tag = kwargs['tag']
    answer = ""

    if(len(flag) == 0 and len(directions) == 0  and len(parameter) > 0):

        for filename in parameter:

            if('*' in filename):

                listoffiles = checkstart(filename)

                for files in listoffiles:

                    if(os.path.isfile(files)):

                        answer = answer + deletefile(files)

                    else:

                        answer = answer + \
                            'cannot delete a directory {}'.format(files)
                        answer = answer +'\n'
                

            else:

                answer = answer +deletefile(filename)
        return answer

    elif(len(flag) == 1 and len(directions) == 0  and len(parameter) > 0):

        for directory in parameter:

            if('*' in directory):

                listoffiles = checkstart(directory)

                for files in listoffiles:

                    if(os.path.isfile(files)):

                        answer = answer+ deletefile(files)

                    else:

                        answer = answer+ deleteDir(files)

            else:

                answer = answer + deleteDir(directory)
        return answer

    else:

        answer = answer + "not enough arguments"
        return answer
