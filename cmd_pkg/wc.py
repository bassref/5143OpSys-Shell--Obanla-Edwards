
import os
def wc(**kwargs):
    command = ['wc']
    parameter = kwargs['params']
    flag = kwargs['flags']
    directions = kwargs['directions']
    tag = kwargs['tag']
    lsitall = []
    total_lines = 0
    total_char = 0
    total_words = 0
    lflag = False
    mflag = False
    wflag = False
    aflag = False
    el = False

    answer = ""
    if(len(flag) >= 0 and len(parameter) > 0):
        for fname in parameter:
            listed = {}
            num_lines = 0
            num_words = 0
            num_chars = 0
            if(tag == True):

                newlist = fname.split('\n')

                for tags in newlist:
                    if(tags != ""):
                        words = tags.split()
                        num_lines += 1
                        num_words += len(words)
                        num_chars += len(tags)

                    total_lines = total_lines+num_lines
                    total_char = total_char+num_chars
                    total_words = total_words+num_words
                    listed['fname'] = fname
                    listed['num_lines'] = num_lines
                    listed['num_words'] = num_words
                    listed['num_chars'] = num_chars + num_lines
                    lsitall.append(listed)

            else:
                if (os.path.isfile(fname)):

                    with open(fname, 'r') as f:
                        for line in f:
                            words = line.split()
                            num_lines += 1
                            num_words += len(words)
                            num_chars += len(line)
                        total_lines = total_lines+num_lines
                        total_char = total_char+num_chars
                        total_words = total_words+num_words
                    listed['fname'] = fname
                    listed['num_lines'] = num_lines
                    listed['num_words'] = num_words
                    listed['num_chars'] = num_chars
                    lsitall.append(listed)

                else:
                    el = True
                    answer = "{} , is not a file".format(fname)
                    answer = answer + "0  0  0"
                    answer = answer + '\n'


        if(len(parameter) > 1 and el == False):

            for item in lsitall:
                key = item['fname']
                if(len(flag) == 1):
                    aflag = True
                    if(flag[0] == '-l'):
                        lflag = True
                        answer = answer + "{} {}".format(item['num_lines'], key)
                        answer = answer + "\n"
                    elif(flag[0] == '-m'):
                        mflag = True
                        answer = answer + "{} {}".format(item['num_chars'], key)
                        answer = answer + "\n"

                    elif(flag[0] == '-w'):
                        wflag = True
                        answer = answer + "{} {}".format(item['num_words'], key)
                        answer = answer + "\n"
                    else:
                        answer = "invalid arg"

                if(aflag == False):
                    answer = answer + "{} {} {} {}".format(
                        item['num_lines'], item['num_words'], item['num_chars'], item['fname'])
                    answer = answer + "\n"

            if(aflag == False):
                answer = answer + "{} {} {} Total ".format(
                    total_lines, total_words, total_char)
                answer = answer + "\n"
            if(lflag == True):
                answer = answer + " {} Total ".format(total_lines)
                answer = answer + "\n"
            elif(mflag == True):
                answer = answer + "{} Total ".format(total_char)
                answer = answer + "\n"
            elif(wflag == True):
                answer = answer + "{} Total ".format(total_words)
                answer = answer + "\n"

            if(len(directions) == 2):

                direct = directions[0]
                fil = directions[1]
                with open(fil, direct) as f:
                    f.write(answer)
                
            else:

                return answer
        elif(len(parameter) == 1 and el == False):
            fname = parameter[0]
            dic1 = lsitall[0]
            if(len(flag) == 1):
                if(flag[0] == '-l'):
                    answer = answer + " {}".format(dic1['num_lines'])
                    answer = answer + "\n"
                elif(flag[0] == '-m'):
                    answer = answer + " {}".format(dic1['num_chars'])
                    answer = answer + "\n"
                elif(flag[0] == '-w'):
                    answer = answer + "{}".format(dic1['num_words'])
                    answer = answer + "\n"
                else:
                    answer = answer + "invalid argument"

            else:
                lis = list(dic1.values())

                answer = answer + "{} {} {} {}".format(lis[1], lis[2], lis[3], lis[0])
                answer = answer + "\n"
            if(len(directions) == 2):
                direct = directions[0]
                fil = directions[1]
                with open(fil, direct) as f:
                    f.write(answer)
                
            else:
                return answer
    elif(len(flag) == 0 and len(parameter) == 0 and len(directions) == 2):
        num_lines = 0
        num_words = 0
        num_chars = 0
        answer =''
        if(os.path.isfile(directions[1])):
            if(directions[0] == 'r+'):
                with open(directions[1], "r+") as file:
                    for line in file:
                        words = line.split()
                        num_lines += 1
                        num_words += len(words)
                        num_chars += len(line)
            answer = answer + "{} {} {} {}".format(num_lines, num_words,num_chars, directions[0])
            return answer
        else:
            answer = answer +"{} is not a file".format(directions[1])
            return answer
    else:
        answer = 'invalid argument'