a=[[1, 0, 0, 1, 1, 0, 1, 0],
 [1, 0, 1, 1, 1, 1, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 1],
 [0, 0, 0, 1, 0, 1, 1, 1],
 [0, 0, 1, 0, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 0, 1]]

class Point:
    def __init__(self,x=-1,y=-1):
        self.x=x
        self.y=y
        self.startX = 0 if y-(4-1)<0 else y-(4-1)
        self.endX = len(a)-1 if (y+(4-1))>(8-1) else (y+(4-1))
        self.startY= 0 if x-(4-1)<0 else x-(4-1)
        self.endY= len(a)-1 if  (x+(4-1))>(8-1) else (x+(4-1))
    
    def show(self):
        return (self.x,self.y)

def check4Hor(a,p,color):
    start=p.startX
    end= p.endX
    startW=-1
    endW=-1
    k=0
    p1,p2=0,0
    for i in range(start,end-(4-1)+1):
        k=0
        for j in range(4):
            if(a[p.x][i+j]!=color):
                break
            k=k+1
        if(k==4):
            p1=Point(p.x,i)
            p2=Point(p.x,i+3)
            break
    return (k==4,p1,p2)

def check4Ver(a,p,color):
    start=p.startY
    end= p.endY
    k=0
    p1,p2=0,0
    for i in range(start,end-(4-1)+1):
        k=0
        for j in range(4):
            if(a[i+j][p.y]!=color):
                break
            k=k+1
        if(k==4):
            p1=Point(i,p.y)
            p2=Point(i+3,p.y)
            break
    return (k==4,p1,p2)

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
    p1,p2=0,0
    if(end_x-start_x<3):
        return (False,Point(),Point())
    for i in range(start_x,end_x-(4-1)+1):
        k=0
        for j in range(4):
            if(a[s-i-j][i+j]!=color):
                break
            k=k+1
        if(k==4):
            p1=Point(s-i,i)
            p2=Point(s-i-3,i+3)
            break
    return (k==4,p1,p2)

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
        return (False,Point(),Point())
    val=abs(p.y-start_x)
    x_a=p.x-val
    p1,p2=0,0
    for i in range(start_x,end_x-(4-1)+1):
        k=0
        for j in range(4):
            if(a[x_a+j][i+j]!=color):
                break
            k=k+1
        x_a=x_a+1
        if(k==4):
            p1=Point(x_a-4,i)
            p2=Point(x_a-1,i+3)
            break
    return (k==4,p1,p2)

def check4Win(a,p,color):
    results= [check4Hor(a,p,color),check4Ver(a,p,color),check4forwD(a,p,color),check4bacwD(a,p,color)]

    for result in results:
        if result[0]==True:
            return result
    return (False,Point(),Point())
    
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
        result=insertcolor(a,pos-1,player)
        if(result[0]==True):
            playerWon=player
            break
    print(f"Player {player} won the Game from {result[1].show()} to {result[2].show()}")









# print(check4Win(a,Point(3,0),1)[0]) #True
# print(check4Win(a,Point(7,2),1)[0]) #False
# print(check4Win(a,Point(7,6),1)[0]) #False
# print(check4Win(a,Point(5,6),1)[0]) #True
# print(check4Win(a,Point(0,6),1)[0]) #False
# print()
# print(check4Win(a,Point(7,5),1)[0]) #False
# print(check4Win(a,Point(1,2),1)[0]) #True 
# print(check4Win(a,Point(4,4),1)[0]) #True
# print(check4Win(a,Point(5,6),1)[0]) #True
# print(check4Win(a,Point(5,5),1)[0]) #True
