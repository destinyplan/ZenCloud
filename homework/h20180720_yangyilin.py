def AI(fivemap,key):
    x=0
    y=0
    for line in fivemap:
        y=0
        for elem in line:
            # print(x,y,fivemap[x][y])
            if key==elem:
                #right
                if y+1<length and key==fivemap[x][y+1]:
                    #再判断右侧三个棋格是否为key
                    # fivemap[x][y+2] fivemap[x][y+3] fivemap[x][y+4]
                    isSuncess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if key==fivemap[x][y+1+max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                #down
                elif x+1<length and key==fivemap[x+1][y]:
                    isSuncess=False
                    max=1
                    while max<4:
                        if key==fivemap[x+1+max][y] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                #right-down
                elif x+1<length and y+1<length and key==fivemap[x+1][y+1]:
                    isSuncess=False
                    max=0
                    while max<4:
                        if key==fivemap[x+1+max][y+1+max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                # #left-down
                elif x+1<length and y-1<0 and key==fivemap[x+1][y-1]:
                    isSuncess=False
                    max=0
                    while max<4:
                        if key==fivemap[x+1+max][y-1-max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
            y+=1
        x+=1
    return False
fivemap=[]
ll=[0]

player1=1
player2=4

length=int(input('please set map size: '))
width=length*ll
i=0
while i<length:
    fivemap.append(width.copy())
    i+=1
print(fivemap)

isP1=True
info='{} win the game'
while(True):
    result=False
    print("===============================")
    if isP1:
        print("当前是P1")
    else:
        print("当前是P2")
    a=int(input('输入a: '))
    b=int(input('输入b: '))
    if isP1:
        fivemap[a][b]=player1
        isP1=False
        result=AI(fivemap,player1)
        info.format('玩家一')
    else :
        fivemap[a][b]=player2
        isP1=True
        result=AI(fivemap,player2)
        info.format('玩家二')
    
    print('0  1  2  3  4  5  6  7  8  9')
    print('*******************************')
    num=0
    for i in fivemap:
        print(num,end="  ")
        for a in i:
            print(a,end='  ')
        print('')
        num+=1
    if result:
        break
print("someone win the game")



