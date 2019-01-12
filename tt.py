STACKONE = []
STACKTWO = []
STACKTHREE = []
LOG = []
CHLOG = []
A = 0
B = 0
C = 0
DEPTH = 0
CODE = 0
LINE = 0
CHAR = 0
TMPCMD = 0
CMD = 0
DASH = 0
def Push(stack,number):
    stack.append(number)
def SPop(stack):
    if len(stack) == 0:
            stack.append(0)
    return stack.pop()
import linecache
import os,sys
linecache.clearcache()
#A = os.getcwd()
#print('Choose a Triple Threat program file in: ' + A)
#CODE = input("File name: ")
#CODE = A+"/"+CODE
#print(CODE)
CODE = sys.argv[1]
LINE=1
while 1 == 1:
    TMPCMD = linecache.getline(CODE, LINE)
    CMD = TMPCMD[CHAR:CHAR+2]
    if DEPTH == 0:
        if CMD == '11':
            Push(STACKONE,0)
        if CMD == '22':
            Push(STACKTWO,1)
        if CMD == '33':
            A = SPop(STACKTHREE)
        if CMD == '12':
            A = SPop(STACKONE)
            Push(STACKTWO,A)
        if CMD == '23':
            if len(STACKTWO) == 0:
                C = input('> ')
                A = int(C)
                STACKTWO.append(A)
            A = SPop(STACKTWO)
            Push(STACKTHREE,A)
        if CMD == '31':
            A = SPop(STACKTHREE)
            Push(STACKONE,A)
            Push(STACKONE,A)
        if CMD == '13':
            A = SPop(STACKONE)
            B = SPop(STACKTHREE)
            C = A+B
            Push(STACKTHREE,C)
        if CMD == '21':
            A = SPop(STACKONE)
            B = SPop(STACKTWO)
            C = A-B
            Push(STACKONE,C)
        if CMD == '32':
            A = SPop(STACKTHREE)
            B = SPop(STACKTWO)
            Push(STACKTWO,A)
            print(B)
        if CMD == '10':
            A = SPop(STACKONE)
            if A == 0:
                DEPTH=DEPTH+1
            else:
                Push(LOG,LINE)
                Push(CHLOG,CHAR)
        if CMD == '30':
            A = SPop(STACKTHREE)
            if A != 0:
                B = SPop(LOG)
                Push(LOG,B)
                LINE = B
                C = SPop(CHLOG)
                Push(CHLOG,C)
                CHAR = C
            else:
                B = SPop(LOG)
                C = SPop(CHLOG)
        if CMD == '00':
            break
        if CMD == '':
            break
    else:
        if CMD == '10':
            DEPTH=DEPTH+1
        if CMD == '30':
            DEPTH=DEPTH-1
        if CMD == '00':
            DEPTH=0
            break
        if CMD == '':
            DEPTH=0
            break
    DASH = TMPCMD[CHAR+2:CHAR+3]
    if DASH == "-":
        CHAR=CHAR+3
    else:
        CHAR=0
        LINE = LINE + 1
#print('End of program.')
