'''
五子棋V0.9 by all
'''
#判断当前棋局是否有人胜利
def AI(fivemap,key):
    x=0
    y=0
    length = len(fivemap)
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
                        if y+1+max<length and key==fivemap[x][y+1+max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                #right-down
                if y+1<length and x+1<length and key==fivemap[x+1][y+1]:
                    #再判断右侧三个棋格是否为key
                    # f9ivemap[x][y+2] fivemap[x][y+3] fivemap[x][y+4]
                    isSuncess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if y+1+max<length and x+1+max<length and key==fivemap[x+1+max][y+1+max] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                # #down
                if x+1<length and key==fivemap[x+1][y]:
                    #再判断下侧三个棋格是否为key
                    isSuncess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if x+1+max<length and key==fivemap[x+1+max][y] :
                            isSuncess=True
                        else:
                            isSuncess=False
                            break
                        max+=1
                    if isSuncess:
                        return True
                # #left-down
                if x+1<length and y-1>=0 and key==fivemap[x+1][y-1]:
                    #再判断左下侧三个棋格是否为key
                    isSuncess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if x+1+max<length and y-1-max >=0 and key==fivemap[x+1+max][y-1-max] :
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

#显示棋盘
def ShowMap(fivemap):
    #打印棋盘顶部彩边
    print("*****************************")
    print("*    ",end="")
    startChar=ord('A')
    newlength=length+startChar
    while startChar<newlength:
        print("{}".format(chr(startChar)),end=" ")
        startChar+=1
    print("   *")

    #打印棋盘
    lineNum=1
    startChar=ord('A')
    for ii in fivemap:
        #打印棋盘左边彩边
        print("**{} ".format(chr(startChar)),end=" ")

        for jj in ii:
            print(jj,end=" ")

        #打印棋盘右边彩边
        print(" {}**".format(chr(startChar)))
        startChar+=1

    #打印棋盘底部部彩边
    print("*    ",end="")
    startChar=ord('A')
    while startChar<newlength:
        print("{}".format(chr(startChar)),end=" ")
        startChar+=1
    print("   *")
    print("*****************************")

# 一些提示性语句
tips_size='请输入棋盘宽度:'
tips_play_1='请玩家1落子:'
tips_play_2='请玩家2落子:'
tips_exp='棋子坐标(例:AA:第一行第一列):'
tips_key_error='落子有错,请重新落子!'
tips_out_of_map='棋盘没那么大,请重新落子!'
tips_player_1='鸣人'
tips_player_2='佐助'

#变量定义
mapkey='-'
fivemap=[]
ll=[mapkey]
player1=1
player2=4
isP1=True
length=10

length=int(input(tips_size))
width = length*ll #[0,0,0.......0]

#创建指定宽度的棋盘
i=0
while i<length:
    fivemap.append(width.copy())
    i+=1

#第一次显示空棋盘
ShowMap(fivemap)

#下棋
info="{} 胜!!!"
while True:
    result=False
    #下一步棋
    if isP1:
        print(tips_play_1)
    else:
        print(tips_play_2)
    xy=input(tips_exp)
    if len(xy)!=2:
        print(tips_key_error)
        continue
    x=ord(xy[0])-65
    y=ord(xy[1])-65
    if x>=0 and x<length and y>=0 and y<length :
        if isP1:
            if mapkey == fivemap[x][y]:
                fivemap[x][y]=player1
                isP1=False
                #AI判断当前棋局是否结束
                result = AI(fivemap,player1)
                info = info.format(tips_player_1)
            else:
                print(tips_key_error)
                continue
        else:
            if mapkey == fivemap[x][y]:
                fivemap[x][y]=player2
                isP1=True
                #AI判断当前棋局是否结束
                result = AI(fivemap,player2)
                info = info.format(tips_player_2)
            else:
                print(tips_key_error)
                continue

        #刷新当前棋盘
        ShowMap(fivemap)
        
        #game over
        if result:
            break
    else:
        print(tips_out_of_map)

print(info)