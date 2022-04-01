#notMoved=True
#-----------------------------------------------------------------------------------------------------------------------------------------------
def possiblemoves(node,piece,x_pos,y_pos):
    Moves=[]
    opponent=[]
    if piece==1:
        opponent=[7,8,9,10,11,12]
        if x_pos==6: #black pawns are at line 7
            if node[x_pos-1][y_pos]==0:
                Moves.append((x_pos-1,y_pos,x_pos,y_pos))
                if node[x_pos-2][y_pos]==0:
                    Moves.append((x_pos-2,y_pos,x_pos,y_pos))
        elif x_pos>0 and x_pos<6:#black pawns in other lines
            if node[x_pos-1][y_pos]==0:
                Moves.append((x_pos-1,y_pos,x_pos,y_pos))
        if x_pos>=1 and x_pos<9 and y_pos>=1 and y_pos<9 and node[x_pos-1][y_pos-1] in opponent:
            Moves.append((x_pos-1,y_pos-1,x_pos,y_pos))
        if x_pos>=1 and x_pos<9 and y_pos>=-1 and y_pos<7 and node[x_pos-1][y_pos+1] in opponent:
            Moves.append((x_pos-1,y_pos+1,x_pos,y_pos))

    elif piece==2 or piece==11:
        #Rook movement
        if piece==2:
            opponent=[7,8,9,10,11,12]
            member=[1,2,3,4,5,6]
        else:
            opponent=[1,2,3,4,5,6]
            member=[7,8,9,10,11,12]
        Moves=rook(node,x_pos,y_pos,Moves,opponent,member)

    elif piece==3 or piece==10:
        if piece==3:
            opponent=[7,8,9,10,11,12]
            member=[1,2,3,4,5,6]
        else:
            opponent=[1,2,3,4,5,6]
            member=[7,8,9,10,11,12]

        if x_pos-2>=0 and x_pos-2<8 and y_pos+1>=0 and y_pos+1<8:
            if node[x_pos-2][y_pos+1]==0 or node[x_pos-2][y_pos+1] in opponent:
                Moves.append((x_pos-2,y_pos+1,x_pos,y_pos))
        if x_pos-2>=0 and x_pos-2<8 and y_pos-1>=0 and y_pos-1<8:
            if node[x_pos-2][y_pos-1]==0 or node[x_pos-2][y_pos-1] in opponent:
                Moves.append((x_pos-2,y_pos-1,x_pos,y_pos))
        if x_pos-1>=0 and x_pos-1<8 and y_pos+2>=0 and y_pos+2<8:
            if node[x_pos-1][y_pos+2]==0 or node[x_pos-1][y_pos+2] in opponent:
                Moves.append((x_pos-1,y_pos+2,x_pos,y_pos))
        if x_pos-1>=0 and x_pos-1<8 and y_pos-2>=0 and y_pos-2<8:
            if node[x_pos-1][y_pos-2]==0 or node[x_pos-1][y_pos-2] in opponent:
                Moves.append((x_pos-1,y_pos-2,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos+2>=0 and y_pos+2<8:
            if node[x_pos+1][y_pos+2]==0 or node[x_pos+1][y_pos+2] in opponent:
                Moves.append((x_pos+1,y_pos+2,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos-2>=0 and y_pos-2<8:
            if node[x_pos+1][y_pos-2]==0 or node[x_pos+1][y_pos-2] in opponent:
                Moves.append((x_pos+1,y_pos-2,x_pos,y_pos))
        if x_pos+2>=0 and x_pos+2<8 and y_pos+1>=0 and y_pos+1<8:
            if node[x_pos+2][y_pos+1]==0 or node[x_pos+2][y_pos+1] in opponent:
                Moves.append((x_pos+2,y_pos+1,x_pos,y_pos))
        if x_pos+2>=0 and x_pos+2<8 and y_pos-1>=0 and y_pos-1<8:
            if node[x_pos+2][y_pos-1]==0 or node[x_pos+2][y_pos-1] in opponent:
                Moves.append((x_pos+2,y_pos-1,x_pos,y_pos))

    elif piece==4 or piece==9:
        if piece==4:
            opponent=[7,8,9,10,11,12]
            member=[1,2,3,4,5,6]
        else:
            opponent=[1,2,3,4,5,6]
            member=[7,8,9,10,11,12]
        #Bishop movement
        Moves=bishop(node,x_pos,y_pos,Moves,opponent,member)
    elif piece==5 or piece==8:
        if piece==5:
            opponent=[7,8,9,10,11,12]
            member=[1,2,3,4,5,6]
        else:
            opponent=[1,2,3,4,5,6]
            member=[7,8,9,10,11,12]
        if x_pos-1>=0 and x_pos-1<8 and y_pos+1>=0 and y_pos+1<8:
            if node[x_pos-1][y_pos+1]==0 or node[x_pos-1][y_pos+1] in opponent:
                Moves.append((x_pos-1,y_pos+1,x_pos,y_pos))
        if x_pos-1>=0 and x_pos-1<8 and y_pos-1>=0 and y_pos-1<8:
            if node[x_pos-1][y_pos-1]==0 or node[x_pos-1][y_pos-1] in opponent:
                Moves.append((x_pos-1,y_pos-1,x_pos,y_pos))
        if x_pos-1>=0 and x_pos-1<8 and y_pos>=0 and y_pos<8:
            if node[x_pos-1][y_pos]==0 or node[x_pos-1][y_pos] in opponent:
                Moves.append((x_pos-1,y_pos,x_pos,y_pos))
        if x_pos>=0 and x_pos<8 and y_pos-1>=0 and y_pos-1<8:
            if node[x_pos][y_pos-1]==0 or node[x_pos][y_pos-1] in opponent:
                Moves.append((x_pos,y_pos-1,x_pos,y_pos))
        if x_pos>=0 and x_pos<8 and y_pos+1>=0 and y_pos+1<8:
            if node[x_pos][y_pos+1]==0 or node[x_pos][y_pos+1] in opponent:
                Moves.append((x_pos,y_pos+1,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos+1>=0 and y_pos+1<8:
            if node[x_pos+1][y_pos+1]==0 or node[x_pos+1][y_pos+1] in opponent:
                Moves.append((x_pos+1,y_pos+1,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos-1>=0 and y_pos-1<8:
            if node[x_pos+1][y_pos-1]==0 or node[x_pos+1][y_pos-1] in opponent:
                Moves.append((x_pos+1,y_pos-1,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos>=0 and y_pos<8:
            if node[x_pos+1][y_pos]==0 or node[x_pos+1][y_pos] in opponent:
                Moves.append((x_pos+1,y_pos,x_pos,y_pos))
        #if piece==5 and notMoved==True and node[x_pos][y_pos+2]==0:
        #    Moves.append((x_pos,y_pos+2,x_pos,y_pos))

    elif piece==6 or piece==7:
        Move1=[]
        Move2=[]
        if piece==6:
            opponent=[7,8,9,10,11,12]
            member=[1,2,3,4,5,6]
        else:
            opponent=[1,2,3,4,5,6]
            member=[7,8,9,10,11,12]
        Move1=bishop(node,x_pos,y_pos,Move1,opponent,member)
        Move2=rook(node,x_pos,y_pos,Move2,opponent,member)
        Moves=Move1+Move2
    elif piece==12:
        opponent=[1,2,3,4,5,6]
        member=[7,8,9,10,11,12]
        if x_pos==1: #black pawns are at line 7
            if node[x_pos+1][y_pos]==0:
                Moves.append((x_pos+1,y_pos,x_pos,y_pos))
                if node[x_pos+2][y_pos]==0:
                    Moves.append((x_pos+2,y_pos,x_pos,y_pos))
        elif x_pos>1 and x_pos<7:#black pawns in other lines
            if node[x_pos+1][y_pos]==0:
                Moves.append((x_pos+1,y_pos,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos-1>=0 and y_pos-1<8 and node[x_pos+1][y_pos-1] in opponent:
            Moves.append((x_pos+1,y_pos-1,x_pos,y_pos))
        if x_pos+1>=0 and x_pos+1<8 and y_pos+1>=0 and y_pos+1<8 and node[x_pos+1][y_pos+1] in opponent:
            Moves.append((x_pos+1,y_pos+1,x_pos,y_pos))
    return Moves
#------------------------------------------------------------------------------------------------------------------------------------------------
def rook(node,x_pos,y_pos,Moves,opponent,member):
    done=False
    #Rook left movement
    x=x_pos
    y=y_pos
    while y>0 and done==False:
        y=y-1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #Rook right movement
    x=x_pos
    y=y_pos
    done=False
    while y<7 and done==False:
        y=y+1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #Rook up movement
    x=x_pos
    y=y_pos
    done=False
    while x>0 and done==False:
        x=x-1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #Rook down movement
    x=x_pos
    y=y_pos
    done=False
    while x<7 and done==False:
        x=x+1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    return Moves
#--------------------------------------------------------------------------------------------------------------
def bishop(node,x_pos,y_pos,Moves,opponent,member):
    x=x_pos
    y=y_pos
    done=False
    while x-1>=0 and x-1<8 and y+1>=0 and y+1<8 and done==False:
        x=x-1
        y=y+1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #Front left diagonal
    x=x_pos
    y=y_pos
    done=False
    while x-1>=0 and y-1>=0 and x-1<8 and y-1<8 and done==False:
        x=x-1
        y=y-1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #back left diagonal
    x=x_pos
    y=y_pos
    done=False
    while x+1<8 and x+1>=0 and y-1>=0 and y-1<8 and done==False:
        x=x+1
        y=y-1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    #Back right diagonal
    x=x_pos
    y=y_pos
    done=False
    while x+1<8 and y+1>=0 and x+1>=0 and y+1<8 and done==False:
        x=x+1
        y=y+1
        if node[x][y]==0:
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in opponent:
            done=True
            Moves.append((x,y,x_pos,y_pos))
        if node[x][y] in member:
            done=True
    return Moves
#--------------------------------------------------------------------------------------------------------------
