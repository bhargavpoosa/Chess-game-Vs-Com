#notMoved=True
#-----------------------------------------------------------------------
from helpfnVcom import possiblemoves,rook,bishop
def sort_tuple(tup):#Priority Queue
    l=len(tup)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if tup[j][3]>tup[j+1][3]:
                temp=tup[j]
                tup[j]=tup[j+1]
                tup[j+1]=temp
            if tup[j][3]==tup[j+1][3]:
                if tup[j][4]>tup[j+1][4]:
                    temp=tup[j]
                    tup[j]=tup[j+1]
                    tup[j+1]=temp
    return tup
#-------------------------------------------------------------------------------------------
def check_board(piece,node):#returns the count of particular piece on the board
    count=0
    for i in range(8):
        for j in range(8):
            if node[i][j]==piece:
                count=count+1
    return count
#------------------------------------------------------------------------------------------------
def isolation_check(node):
    black_isolated=0
    white_isolated=0
    for i in [2,3,4,5]:
        for j in [1,2,3,4,5,6]:
            if node[i][j]==1 and node[i+1][j-1]!=1 and node[i+1][j-1]!=1:
                white_isolated=white_isolated+1
            if node[i][j]==12 and node[i-1][j-1]!=12 and node[i-1][j+1]!=12:
                black_isolated=black_isolated+1
        if node[i][0]==1 and node[i+1][1]!=1:
            white_isolated=white_isolated+1
        if node[i][7]==1 and node[i+1][6]!=1:
            white_isolated=white_isolated+1
        if node[i][0]==12 and node[i-1][1]!=1:
            black_isolated=black_isolated+1
        if node[i][7]==12 and node[i-1][6]!=1:
            black_isolated=black_isolated+1
    return (white_isolated,black_isolated)
#-------------------------------------------------------------------------------------------
def check(node):
    black_blocked=0
    white_blocked=0
    white_doubled=0
    black_doubled=0
    for i in [1,2,3,4,5,6]:
        for j in range(8):
            if node[i][j]==1 and node[i-1][j]==12:
                white_blocked=white_blocked+1
            if node[i][j]==1 and node[i-1][j]==1:
                white_doubled=white_doubled+1
            if node[i][j]==12 and node[i+1][j]==1:
                black_blocked=black_blocked+1
            if node[i][j]==12 and node[i+1][j]==12:
                black_doubled=black_doubled+1
    return (white_blocked,black_blocked,white_doubled,black_doubled)
#--------------------------------------------------------------------------------------------------------------
def Mobility(node):
    white_mobility=0
    black_mobility=0
    Moves=[]
    for i in range(8):
        for j in range(8):
            if node[i][j] in [1,2,3,4,5,6]:
                Moves=possiblemoves(node,node[i][j],i,j)
                white_mobility=white_mobility+len(Moves)
            if node[i][j] in [7,8,9,10,11,12]:
                Moves=possiblemoves(node,node[i][j],i,j)
                black_mobility=black_mobility+len(Moves)
            Moves.clear()
    return (white_mobility,black_mobility)
#------------------------------------------------------------------------------------------------
def eval(node):#Heuristic function
    num=[]
    weights=[1,5,3,3,200,9]
    h=0
    (x,y)=isolation_check(node)
    h=h-0.5*(y-x)
    (p,q,r,s)=check(node)
    h=h-0.5*(q-p)-0.5*(s-r)
    (x,y)=Mobility(node)
    h=h+0.1*(y-x)
    for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
        count = check_board(i,node)
        num.append(count)
    for j in range(6):
        h=h+weights[j]*(num[11-j]-num[j])
    return h
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def movegen(node,player,level):#returns the list the children nodes for a particular parent node
    p=node
    dup=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    child=[]
    Moves=[]
    member=[]
    if player=='max':
        member=[7,8,9,10,11,12]
    else:
        member=[1,2,3,4,5,6]
    for i in member:
        for j in range(8):
            for k in range(8):
                if node[j][k]==i:
                    Moves=possiblemoves(node,i,j,k)
                    if len(Moves)!=0:
                        for (x,y,x_prev,y_prev) in Moves:
                            dup=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
                            for a in range(8):
                                for b in range(8):
                                    dup[a][b]=node[a][b]

                            temp=dup[x][y]
                            dup[x_prev][y_prev]=0
                            if i==12 and x==7:
                                dup[x][y]=7
                            else:
                                dup[x][y]=i
                            child.append(dup)
                            if len(parent)==0:
                                parent.append([dup,p,0,level+1])
                            elif [dup,p,0,level+1] not in parent and [dup,p,1,level+1] not in parent:
                                parent.append([dup,p,0,level+1])
                    Moves.clear()
        Moves.clear()
    return child
#-------------------------------------------------------------------------------------------------------------------------------
def min(a,b):
    if a<b:
        return a
    else:
        return b
#----------------------------------------------------------------------------------------------------------------------------------------
def SSS(root,depth):
    open=[]
    next_child=[]
    board=[]
    global parent
    parent=[]
    open.append((root,'max','live',2000,0))
    while(True):
        sort_tuple(open)
        (N,player,status,h,d)=open.pop()
        if N==root and status=='solved' and len(board)!=0:
            return board,h

        if status=='live':
            if d==depth:
                open.append((N,player,'solved',min(h,eval(N)),depth))
            elif player=='max':
                for child in movegen(N,player,d):
                    open.append((child,'min','live',h,d+1))
            elif player=='min':
                open.append((movegen(N,player,d)[0],'max','live',h,d+1))

        if status=='solved':
            next_child=[]
            for i in range(len(parent)):
                if parent[i][0]==N and parent[i][3]==d:
                    p=parent[i][1]
                    parent[i][2]=1

            for i in range(len(parent)):
                if parent[i][1]==p and parent[i][2]==0:
                    next_child=parent[i][0]
                    parent[i][2]=1
                    break

            if player=='max' and len(next_child)==0:
                open.append((p,'min','solved',h,d-1))
            elif player=='max':
                open.append((next_child,'max','live',h,d))
            elif player=='min':
                open.append((p,'max','solved',h,d-1))
                board=[]
                if p==root:
                    board.append(N)
                #Remove all successors of p in open
                children=movegen(p,'max',d-1)
                index=0
                size=len(open)
                for i in range(len(children)):
                    index=0
                    size=len(open)
                    while(index<size):
                        if open[index][0]==children[i]:
                            open.pop(index)
                            break
                        else:
                            index=index+1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
