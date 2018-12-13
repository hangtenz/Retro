ids=[]
hashids={}
op1=[]
op2=[]
cons=[]
def run(linecommand,numline):
    res = []
    res.append((10,linecommand[0]))
    if(linecommand[1] in ids):
        res.append((11,linecommand[1]))
        res.append((17,4))
        if(linecommand[3] in ids):
            res.append((11,linecommand[3]))
        elif(linecommand[3] in cons):
            res.append((12,linecommand[3]))
        if(len(linecommand)<=4): return res,numline
        if(linecommand[4] == '+'):
            res.append((17,1))
        elif(linecommand[4] == '-'):
            res.append((17,2))
        if(linecommand[5] in ids):
            res.append((11,linecommand[5]))
        elif(linecommand[5] in cons):
            res.append((12,linecommand[5]))
    elif(linecommand[1] == 'IF'):
        res.append((13,0))
        if(linecommand[2] in ids):
            res.append((11,linecommand[2]))
        elif(linecommand[2] in cons):
            res.append((12,linecommand[2]))
        if(linecommand[3] == '<'):
            res.append((17,3))
        elif(linecommand[3] == '='):
            res.append((17,4))
        if(linecommand[4] in ids):
            res.append((11,linecommand[4]))
        elif(linecommand[4] in cons):
            res.append((12,linecommand[4]))
    elif(linecommand[1] == 'PRINT'):
        res.append((15,0))
    elif(linecommand[1] == 'GOTO'):
        numline=linecommand[1]
        res.append((14,linecommand[2]))
    elif(linecommand[1] == 'STOP'):
        res.append((16,0))
        numline=-1
    return res,numline
###############################################################################
#############################pre run###########################################
###############################################################################
allline={}
linenumber=0
strs = 'abcdefghijklmnopqrstuvwxyz'.upper()
count=0
for s in strs:
    ids.append(s)
    count+=1
    hashids[s]=count
op1.append('+')
op1.append('-')
op2.append('<')
op2.append('=')
for i in range(0,1001,1):
    cons.append(str(i))
###############################################################################
############################end pre run########################################
###############################################################################
out=[]
while(linenumber!=-1):
    if(linenumber in allline):
        o,n=out.append(run(allline[linenumber],linenumber))
        out.append(o)
        linenumber=n
        continue
    line=input().split()
    allline[line[0]]=line
    o,n=run(line,linenumber)
    out.append(o)
    linenumber=n
for o in out:
    s=""
    for o2 in o:
        for o3 in o2:
            if(o3 in ids):
                s+=str(hashids[o3])+" "
            else:
                s+=str(o3)+" "
    print(s)
print(0)
