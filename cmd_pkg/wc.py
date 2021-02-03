import sys
import os


def wc(**kwargs):
    command = ['rm']
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
    if(len(flag) >= 0 and len(directions) == 0 and tag == False and len(parameter) > 0):
        for fname in parameter:
            if (os.path.isfile(fname)):
                listed = {}
                num_lines = 0
                num_words = 0
                num_chars = 0
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
                print("{} , is not a file".format(fname))
                print("0  0  0")

        if(len(parameter) > 1 and el == False):
            for item in lsitall:
                key = item['fname']
                if(len(flag) == 1):
                    aflag = True
                    if(flag[0] == '-l'):
                        lflag = True
                        print("{} {}".format(item['num_lines'], key))

                    elif(flag[0] == '-m'):
                        mflag = True
                        print("{} {}".format(item['num_chars'], key))

                    elif(flag[0] == '-w'):
                        wflag = True
                        print("{} {}".format(item['num_words'], key))
                    else:
                        print("invalid arg")
                if(aflag == False):
                    print("{} {} {} {}".format(
                        item['num_lines'], item['num_words'], item['num_chars'], item['fname']))
            if(aflag == False):
                print("{} {} {} Total ".format(
                    total_lines, total_words, total_char))
            if(lflag == True):
                print(" {} Total ".format(total_lines))
            elif(mflag == True):
                print("{} Total ".format(total_char))
            elif(wflag == True):
                print("{} Total ".format(total_words))
        elif(len(parameter) == 1 and el == False):
            fname = parameter[0]
            dic1 = lsitall[0]
            if(len(flag) == 1):
                if(flag[0] == '-l'):
                    print("{} {}".format(dic1['num_lines'], fname))
                elif(flag[0] == '-m'):
                    print("{} {}".format(dic1['num_chars'], fname))
                elif(flag[0] == '-w'):
                    print("{} {}".format(dic1['num_words'], fname))
                else:
                    print("invalid arg")
            else:
                lis = list(dic1.values())

                print("{} {} {}".format(lis[1], lis[2], lis[3], lis[0]))
