a=[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.startX = 0 if y-(4-1)<0 else y-(4-1)
        self.endX = len(a)-1 if (y+(4-1))>(8-1) else (y+(4-1))
        self.startY= 0 if x-(4-1)<0 else x-(4-1)
        self.endY= len(a)-1 if  (x+(4-1))>(8-1) else (x+(4-1))

def check4Hor(a,p,color):
    start=p.startX
    end= p.endX
    k=0
    for i in range(start,end-(4-1)+1):
        k=0
        for j in range(4):
            if(a[p.x][i+j]!=color):
                break
            k=k+1
        if(k==4):
            break
    return k==4

def check4Ver(a,p,color):
    start=p.startY
    end= p.endY
    k=0
    for i in range(start,end-(4-1)+1):
        k=0
        for j in range(4):
            if(a[i+j][p.y]!=color):
                break
            k=k+1
        if(k==4):
            break
    return k==4

def check4forwD(a,p,color):
 
    if(abs(p.startX-p.y)>=abs(p.endY-p.x)):
        start_x=(p.x+p.y)-p.endY
    else:
        start_x=p.startX

    if(abs(p.startY-p.x)>=abs(p.endY-p.y)):
        end_x=p.endY
    else:
        end_x=abs(p.startY-p.x)+p.y

    k=0
    s=p.x+p.y
    if(end_x-start_x<3):
        return False
    for i in range(start_x,end_x-(4-1)+1):
        k=0
        for j in range(4):
            if(a[s-i-j][i+j]!=color):
                break
            k=k+1
        if(k==4):
            break
    return k==4

def check4bacwD(a,p,color):
    if(abs(p.startX-p.y)>=abs(p.startY-p.x)):
        start_x=p.y-abs(p.startY-p.x)
    else:
        start_x=p.startX

    if(abs(p.endX-p.y)>=abs(p.endY-p.x)):
        end_x=p.y+abs(p.endY-p.x)
    else:
        end_x=p.endX

    if(end_x-start_x<3):
        return False
    val=abs(p.y-start_x)
    x_a=p.x-val
    for i in range(start_x,end_x-(4-1)+1):
        k=0
        for j in range(4):
            if(a[x_a+j][i+j]!=color):
                break
            k=k+1
        x_a=x_a+1
        if(k==4):
            break
    return k==4

def check4Win(a,p,color):
    return check4bacwD(a,p,color) or check4Ver(a,p,color) or check4Hor(a,p,color) or check4forwD(a,p,color)

def insertcolor(a,position,color):
    prev=-1
    for i in range(len(a)):
        if(a[i][position]==0):
            prev=i
    if(prev==-1):
        raise Exception('Position Overflow')
    a[prev][position]=color
    return(check4Win(a,Point(prev,position),color))

playerWon=0
while playerWon==0:
    players=[1,2]
    for player in players:
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j],end=' ')
            print()
        print(f'Player {player}, Enter the position from 1 to 8 where you want to insert')
        pos=int(input())
        if(insertcolor(a,pos-1,player)==True):
            playerWon=player
            break
    print(f"Player {player} won the Game")

