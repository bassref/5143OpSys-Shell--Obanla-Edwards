import os
import shutil
import getch as gt
getch = gt.Getch()
# function to print a file one page at a time


def less(**kwargs):
    answer = ''
    termSize = shutil.get_terminal_size()
    numLines = termSize[1]
    fName = kwargs['params']
    lines =[]
    answer =''
    # store all the lines in lines
    if(len(fName) > 0):
        for p in fName:
            with open(fName[0], "r") as f:
                lines = f.read().splitlines()
    else:
        answer = 'invalid command'
    pageNum = 1
    lineNum = 1
    nextPage = input()
    begin = lineNum
    end = begin + numLines

    # print as many lines that can fit on the screen
    for i in range(begin, begin+end):
        answer = answer + lines[i]
        answer = answer + '\n'
        lineNum += 1
    currpos = lineNum
    prevpos = lineNum
    while True:
        char = getch()  # read a character (but don't print)
        if char == '\x03' or char == 'q':
            raise SystemExit("\r")

        elif char in '\x1b':                # arrow key pressed
            null = getch()                  # waste a character
            direction = getch()             # grab the direction

            if direction in 'A':            # up arrow pressed
                # get the PREVIOUS set of lines to display on the screen
                # prints out '↑' then erases it (just to show something)
                if(prevpos > begin):  # if the previous position is past the beginning
                    currpos = prevpos
                    prevpos = begin
                    for i in range(prevpos, currpos):
                        answer = answer + lines[i]
                        answer = answer + '\n'
                        lineNum += 1

            if direction in 'B':            # down arrow pressed
                # get the NEXT set of lines to display on the screen
                os.system('cls' if os.name == 'nt' else 'clear')
                prevpos = currpos + 1
                currpos = currpos + numLines
                for i in range(prevpos, currpos):
                    answer = answer + lines[i]
                    answer = answer + '\n'
                    lineNum += 1

            if direction in 'C':            # left arrow pressed
                # move the cursor to the LEFT on your command prompt line
                # prints out '←' then erases it (just to show something)
                direction = '\033[<1>C'

            if direction in 'D':            # right arrow pressed
                # moves the cursor to the RIGHT on your command prompt line
                # prints out '→' then erases it (just to show something)
                direction = '\033[<1>D'

        elif(nextPage == 'h' or nextPage == 'H'):
            os.system('cls' if os.name == 'nt' else 'clear')
            printHelp()
    return answer
# function to display command options


def printHelp():
    info = []
    info = info.append("********************************************")
    info = info.append('\n')
    info = info.append("Command Options:")
    info = info.append('\n')
    info = info.append("Down arrow key : Next Page")
    info = info.append('\n')
    info = info.append("Up arrow key : Previous Page")
    info = info.append('\n')
    info = info.append("F or f : Move forward to the next line")
    info = info.append('\n')
    info = info.append("B or b : Move back to the previous line")
    info = info.append('\n')
    info = info.append("S or s : Go to the beginning of the file")
    info = info.append('\n')
    info = info.append("E or e : Go to the end of the file")
    info = info.append('\n')
    info = info.append("********************************************")

    return info
