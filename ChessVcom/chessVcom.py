import pygame
from pygame import mixer
import time
from helpfnVcom import possiblemoves,rook,bishop
from sss import SSS,min,movegen,eval,check_board,sort_tuple
#Initialization
pygame.init()
#Screen creation
screen=pygame.display.set_mode((900,600))

background=pygame.image.load('photos/chessimg.png')
#------------------------------------------------------------------------------------------------------------------------------------------
horiz_padding=120
verti_padding=20
cell_size=70
half_cellsize=35
#global notMoved
#notMoved=True
#------------------------------------------------------------------------------------------------------------------------------------------
#Loading white colour chess piece images
pawnwhite=pygame.image.load('photos/pawnwhite.png')
kingwhite=pygame.image.load('photos/kingwhite.png')
rookwhite=pygame.image.load('photos/rookwhite.png')
knightwhite=pygame.image.load('photos/knightwhite.png')
bishopwhite=pygame.image.load('photos/bishopwhite.png')
queenwhite=pygame.image.load('photos/queenwhite.png')
#--------------------------------------------------------------------------------------------------------------------------------------------
#Loading black colour chess piece images
kingblack=pygame.image.load('photos/kingblack.png')
queenblack=pygame.image.load('photos/queenblack.png')
rookblack=pygame.image.load('photos/rookblack.png')
bishopblack=pygame.image.load('photos/bishopblack.png')
knightblack=pygame.image.load('photos/knightblack.png')
pawnblack=pygame.image.load('photos/pawnblack.png')
#-------------------------------------------------------------------------------------------------------------------------------------------
#Caption
pygame.display.set_caption('Chess Game')
#Background Colour
screen.fill((0,0,0))
#Font declaration
font=pygame.font.Font('freesansbold.ttf',32)

pics=dict()
pics['white']=[pawnwhite,rookwhite,knightwhite,bishopwhite,queenwhite,kingwhite]
pics['black']=[pawnblack,rookblack,knightblack,bishopblack,queenblack,kingblack]

chess=dict()
Board=[[11,10,9,7,8,9,10,11],[12,12,12,12,12,12,12,12],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[2,3,4,6,5,4,3,2]]
pawnlist_white=[]
pawnlist_black=[]
rooklist_white=[]
rooklist_black=[]
knightlist_white=[]
knightlist_black=[]
bishoplist_white=[]
bishoplist_black=[]
kinglist_white=[]
kinglist_black=[]
queenlist_white=[]
queenlist_black=[]
Moves=[]
turn='white'

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#pawnlist_white and pawnlist_black contains the squares,where pawns are placed
i=6
for j in range(8):
    rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
    pawnlist_white.append(rect)

i=1
for j in range(8):
    rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
    pawnlist_black.append(rect)
#---------------------------------------------------------------------------------------------------------
#Similarly rooklist_white(rooklist_black),knightlist_white(knightlist_black),bishoplist_white(bishoplist_black),kinglist_white(kinglist_black),queenlist_white(queenlist_black)
#contains the squares where the rooks,knights,bishops,kings and queens are placed respectively
i=7
j=0
while j<8:
    if j==0 or j==7:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        rooklist_white.append(rect)
    elif j==1 or j==6:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        knightlist_white.append(rect)
    elif j==2 or j==5:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        bishoplist_white.append(rect)
    elif j==3:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        queenlist_white.append(rect)
    elif j==4:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        kinglist_white.append(rect)
    j+=1

i=0
j=0
while j<8:
    if j==0 or j==7:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        rooklist_black.append(rect)
    elif j==1 or j==6:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        knightlist_black.append(rect)
    elif j==2 or j==5:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        bishoplist_black.append(rect)
    elif j==3:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        queenlist_black.append(rect)
    elif j==4:
        rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
        kinglist_black.append(rect)
    j+=1
#----------------------------------------------------------------------------------------------------------------------------------------
chess['white']=[pawnlist_white,rooklist_white,knightlist_white,bishoplist_white,queenlist_white,kinglist_white]
chess['black']=[pawnlist_black,rooklist_black,knightlist_black,bishoplist_black,queenlist_black,kinglist_black]
#------------------------------------------------------------------------------------------------------------------------------------
def place_piece():
    #if player_ft==True:
    for i in ['white','black']:
        for j in range(len(chess[i])):
            for k in range(len(chess[i][j])):
                Rect=pics[i][j].get_rect()
                Rect.center=chess[i][j][k].center
                screen.blit(pics[i][j],Rect)
#-----------------------------------------------------------------------------------------------------------------------------------------
def design_board():
    flag=0
    for i in range(8):
        for j in range(8):
            rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
            if flag==0:
                pygame.draw.rect(screen,(240,207,174),rect)#Desert Sand-(240,207,174)
                pygame.draw.rect(screen,(255,255,255),rect,2)
                if j<7:
                    flag+=1
            else:
                if j<7:
                    flag=0
                pygame.draw.rect(screen,(181,101,29),rect)#Light Brown-(181,101,29)
                pygame.draw.rect(screen,(255,255,255),rect,2)
#--------------------------------------------------------------------------------------------------------------
def game_over(turn,font,screen):
    if turn=='white':
        drawText=font.render('BLACK COLOR WINS',True,(0,0,0))
    else:
        drawText=font.render('WHITE COLOR WINS',True,(0,0,0))
    screen.blit(drawText,(250,250))
    pygame.display.update()
#------------------------------------------------------------------------------------------------------------------------
def show_board(board):
    index1=0
    index2=0
    index3=0
    index4=0
    index5=0
    index6=0
    index7=0
    index8=0
    index9=0
    index10=0
    index11=0
    index12=0
    for i in range(8):
        for j in range(8):
            if board[i][j]==1:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                pawnlist_white[index1].center=rect.center
                index1=index1+1
            elif board[i][j]==2:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                rooklist_white[index2].center=rect.center
                index2=index2+1
            elif board[i][j]==3:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                knightlist_white[index3].center=rect.center
                index3=index3+1
            elif board[i][j]==4:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                bishoplist_white[index4].center=rect.center
                index4=index4+1
            elif board[i][j]==5:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                kinglist_white[index5].center=rect.center
                index5=index5+1
            elif board[i][j]==6:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                queenlist_white[index6].center=rect.center
                index6=index6+1
            elif board[i][j]==7:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                queenlist_black[index7].center=rect.center
                index7=index7+1
            elif board[i][j]==8:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                kinglist_black[index8].center=rect.center
                index8=index8+1
            elif board[i][j]==9:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                bishoplist_black[index9].center=rect.center
                index9=index9+1
            elif board[i][j]==10:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                knightlist_black[index10].center=rect.center
                index10=index10+1
            elif board[i][j]==11:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                rooklist_black[index11].center=rect.center
                index11=index11+1
            elif board[i][j]==12:
                rect=pygame.Rect(horiz_padding+j*cell_size,verti_padding+i*cell_size,cell_size,cell_size)
                pawnlist_black[index12].center=rect.center
                index12=index12+1
    while(index1<len(pawnlist_white)):#Removing the dead pieces
        pawnlist_white.pop(index1)
        index1=index1+1
    while(index2<len(rooklist_white)):
        rooklist_white.pop(index2)
        index2=index2+1
    while(index3<len(knightlist_white)):
        knightlist_white.pop(index3)
        index3=index3+1
    while(index4<len(bishoplist_white)):
        bishoplist_white.pop(index4)
        index4=index4+1
    while(index5<len(kinglist_white)):
        kinglist_white.pop(index5)
        index5=index5+1
    while(index6<len(queenlist_white)):
        queenlist_white.pop(index6)
        index6=index6+1
    while(index7<len(queenlist_black)):
        queenlist_black.pop(index7)
        index7=index7+1
    while(index8<len(kinglist_black)):
        kinglist_black.pop(index8)
        index8=index8+1
    while(index9<len(bishoplist_black)):
        bishoplist_black.pop(index9)
        index9=index9+1
    while(index10<len(knightlist_black)):
        knightlist_black.pop(index10)
        index10=index10+1
    while(index11<len(rooklist_black)):
        rooklist_black.pop(index11)
        index11=index11+1
    while(index12<len(pawnlist_black)):
        pawnlist_black.pop(index12)
        index12=index12+1

    pygame.display.update()
#------------------------------------------------------------------------------------------------------------------------
#Changes Turn
def change_turn(turn):
    if turn=='white':
        turn='black'
    else:
        turn='white'
    return turn
#---------------------------------------------------------------------------------------------------------------------------------
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((0,0,0))
    design_board()
    place_piece()
    #Exit Button
    exitButton=pygame.Rect(700,500,70,40)
    exitText=font.render('Exit',True,(0,0,0))
    exitRect=exitText.get_rect()
    exitRect.center=exitButton.center
    pygame.draw.rect(screen,(255,255,255),exitButton)
    screen.blit(exitText,exitRect)
    #Shows the turn of the player
    turnButton=pygame.Rect(780,500,100,40)
    if turn=='white':
        turnText=font.render('White',True,(0,0,0))
    else:
        turnText=font.render('Black',True,(0,0,0))
    turnRect=turnText.get_rect()
    turnRect.center=turnButton.center
    pygame.draw.rect(screen,(255,255,255),turnButton)
    screen.blit(turnText,turnRect)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse=pygame.mouse.get_pos()
            if exitRect.collidepoint(mouse):
                game_over(turn,font,screen)
                done=True
            elif len(Moves)!=0 and x_prev!=mouse[0] and y_prev!=mouse[1]:
                y_final=int((mouse[0]-horiz_padding)/cell_size)
                x_final=int((mouse[1]-verti_padding)/cell_size)
                if piece==1 and x_final==0:
                    piece=6
                Board[x_final][y_final]=piece
                Board[y][x]=0
                notMoved=False
                Moves.clear()
                show_board(Board)
                design_board()
                place_piece()
                pygame.display.update()
                #Adds sound
                sound=mixer.Sound('photos/click.wav')
                sound.play()
                change_turn(turn)
                if check_board(8,Board)==0:
                    game_over(turn,font,screen)
                    time.sleep(2)
                    done=True
                    break
                time.sleep(1)
                B,_=SSS(Board,2)
                Board=B[0]
                show_board(Board)
                design_board()
                place_piece()
                #Adds sound
                sound=mixer.Sound('photos/click.wav')
                sound.play()
                change_turn(turn)
                if check_board(5,Board)==0:
                    game_over(turn,font,screen)
                    time.sleep(2)
                    done=True
                    break
                pygame.display.update()
            elif turn=='white':
                Moves.clear()
                x_prev=mouse[0]
                y_prev=mouse[1]
                x=int((mouse[0]-horiz_padding)/cell_size)
                y=int((mouse[1]-verti_padding)/cell_size)
                piece=Board[y][x]
                Moves=possiblemoves(Board,Board[y][x],y,x)
                for j in range(len(Moves)):
                    pygame.draw.rect(screen,(255,255,153),[cell_size*Moves[j][1]+horiz_padding,cell_size*Moves[j][0]+verti_padding,cell_size,cell_size])
                    pygame.draw.rect(screen,(0,0,0),[cell_size*Moves[j][1]+horiz_padding,cell_size*Moves[j][0]+verti_padding,cell_size,cell_size],2)
                place_piece()
                pygame.display.update()
                time.sleep(2)
    pygame.display.update()
