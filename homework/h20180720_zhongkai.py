fivemap = []
ll =[0]
length = int(input("please input map size:"))
width = length * ll
# print(width)
i = 0
player1 = 1
player2 = 2
while i < length:
    fivemap.append(width.copy())
    i += 1
# print(fivemap)
Isp1 = True


# 判断输赢
def AI(fivemap,key):
    x = 0
    y = 0
    length = len(fivemap)
    for line in fivemap:
        y = 0
        for value in line:
            if key == value:
                # right右边
                if y+1<length and key == fivemap[x][y+1]:
                    isSuccess = False
                    max = 1
                    while max < 4:
                        if key == fivemap[x][y+1+max] and y+1+max<length:
                            isSuccess = True
                        else:
                            isSuccess = False
                            break
                        max += 1
                    if isSuccess:
                        return True
                # right-down 右下
                if y + 1 < length and x + 1 < length and key == fivemap[x + 1][y + 1]:
                    isSuccess = False
                    max = 1
                    while max < 4:
                        if y + 1 + max < length and x + 1 + max < length and key == fivemap[x + 1 + max][y + 1 + max]:
                            isSuccess = True
                        else:
                            isSuccess = False
                            break
                        max += 1
                    if isSuccess:
                        return True
                # down 下
                if x+1<length and key == fivemap[x+1][y] :
                    isSuccess = False
                    dax = 1
                    while dax < 4:
                        if x + 1 + dax < length and key == fivemap[x+1 + dax][y] :
                            isSuccess = True
                        else:
                            isSuccess = False
                            break
                        dax += 1
                    if isSuccess:
                        return True
                # left-down 左下
                if  x+1<length and y-1>=0 and key == fivemap[x + 1][y-1]:
                    isSuccess = False
                    lax = 1

                    while lax < 4:
                        if  x + 1 + lax < length and y - 1 - lax >= 0 and key == fivemap[x + 1 + lax][y - 1 - lax] :
                            isSuccess = True
                        else:
                            isSuccess = False
                            break
                        lax += 1
                    if isSuccess:
                        return True


            y += 1
        x += 1
    return  False


#下棋
while True:
    result = False
    if Isp1:
        P1X = int(input("玩家1落子X="))
        P1Y = int(input("玩家1落子Y="))
        if fivemap[P1X][P1Y] == 0:
            fivemap[P1X][P1Y] = player1
            Isp1 = False
            result = AI(fivemap, player1)
        else:
            print("此处有棋子，换地方吧！")
            continue



    else:
        P2X = int(input("玩家2落子X="))
        P2Y = int(input("玩家2落子Y="))
        if fivemap[P2X][P2Y] == 0:
            fivemap[P2X][P2Y] = player2
            Isp1 = True

            result = AI(fivemap, player2)
        else:
            print("此处有棋子，换地方吧！")
            continue



    #再次打印
    print("*  "*length)


    print("===============五子棋===============")
    num = 0
    for n in fivemap:
        print(num,end="   ")
        for j in n:
            print(j,end="  ")

        print("")
        num += 1
    print("============Made By ZK============")



    if result:
        break

print("someone win the game")
