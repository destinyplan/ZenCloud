def AI(fivemap,key):
    x=0
    y=0
    for line in fivemap:
        y=0
        for elem in line:
            # print(x,y,fivemap[x][y])
            if key==elem:
                #right
                if key==fivemap[x][y+1]:
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
                #right-down
                if key==fivemap[x-1][y+1]:
                    isSuncess=False
                    max=1
                    while max<4:
                        if key==fivemap[x-1-max][y+1+max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                #down
                if key==fivemap[x-1][y]:
                    isSuncess=False
                    max=1
                    while max<4:
                        if key==fivemap[x-1-max][y] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                #left-down
                if key==fivemap[x-1][y-1]:
                    isSuncess=False
                    max=1
                    while max<4:
                        if key==fivemap[x-1-max][y-1-max] :
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
#         [[1,0,0,0,0,0,0,0,0,0],
#          [0,1,0,0,0,0,0,0,0,0],
#          [0,0,1,0,0,0,0,0,0,0],
#          [0,0,0,1,0,0,0,0,0,0],
#          [0,0,0,0,1,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0]]

ll=[0]
player1=4
player2=8
isP1=True
length=10

length=int(input("输入个10吧="))
width = length*ll #[0,0,0.......0]

#创建指定宽度的棋盘
i=0
while i<length:
    fivemap.append(width.copy())
    i+=1

#下棋
while True:
    result=False
    #下一步棋
    if isP1:
        print("凹凸曼落子")
    else:
        print("怪兽落子")
    x=int(input("激光x"))
    y=int(input("音波y"))
    if isP1:
        fivemap[x][y]=player1
        isP1=False
        #AI判断当前棋局是否结束
        result = AI(fivemap,player1)
    else:
        fivemap[x][y]=player2
        isP1=True
        #AI判断当前棋局是否结束
        result = AI(fivemap,player2)

    #刷新当前棋盘
    print('*********************')
    print('  0 1 2 3 4 5 6 7 8 9')
    num = 0 
    for ii in fivemap:
        print (num,end=" ")
        for jj in ii:
            print(jj,end=" ")
        print("")
        num += 1
    print('*********************')

    #game over
    if result:
        break

print("反正最后是我赢了")
