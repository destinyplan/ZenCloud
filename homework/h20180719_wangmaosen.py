#定义一个函数
#这个函数的功能是判断是否胜利
def Win(fivemap,key):
    #初始化x和y，从第一行第一列开始判断
    x = 0
    y = 0

    #遍历棋盘元素
    for line in fivemap:   #遍历每一行
        y = 0
        for elem in line:   #遍历每一行的元素
            if key == elem:
                #右边5个相同,则是x不变,y+1

                #如果y >= legth-5,那么就没有必要再进行验证,永远不可能凑齐 
                if y < length - 5:
                    if key == fivemap[x][y+1]:
                        #现在已经2个相同,再判断右边3个是否也相同,都为key值
                        #key == fivemap[x][y+2],key == fivemap[x][y+3],key == fivemap[x][y+4]
                        isSuncess = False    #判断接下来的3个是否是key指

                        max = 1
                        while max < 4:
                            if key == fivemap[x][y+1+max]:
                                isSuncess = True
                            else:
                                isSuncess = False
                                break
                            max += 1
                        
                        if isSuncess:
                            return True

                #判断下面5个是否相同,则是y不变,x+1

                #如果x >= legth-5,那么就没有必要再进行验证,永远不可能凑齐
                if x < length-5:
                    if key == fivemap[x+1][y]:
                        #判断接下来的3个是否是key指
                        #key == fivemap[x+2][y],key == fivemap[x+3][y],key == fivemap[x+4][y]
                        isSuncess = False    #判断接下来的3个是否是key指

                        max = 1
                        while max < 4:
                            if key == fivemap[x+1+max][y]:
                                isSuncess = True
                            else:
                                isSuncess = False
                                break
                            max += 1
                        
                        if isSuncess:
                            return True
                
                #判断右下方的5个是否相同,则是x+1,y+1

                #如果x >= legth-5 并且y >= length-5,那么就没有必要再进行验证,永远不可能凑齐
                if x < length-5 and y < length-5:
                    if key == fivemap[x+1][y+1]:
                        #判断接下来的3个是否是key指
                        #key == fivemap[x+2][y+2],key == fivemap[x+3][y+3],key == fivemap[x+4][y+4]
                        isSuncess = False    #判断接下来的3个是否是key指

                        max = 1
                        while max < 4:
                            if key == fivemap[x+1+max][y+1+max]:
                                isSuncess = True
                            else:
                                isSuncess = False
                                break
                            max += 1
                        
                        if isSuncess:
                            return True

                #判断左下方的5个是否相同,则是x+1,y-1

                #如果x >= length-5 并且y <= 4,那么就没有必要再进行验证,永远不可能凑齐
                if x < length-5 and y > 4:
                    if key == fivemap[x+1][y-1]:
                        #判断接下来的3个是否是key指
                        #key == fivemap[x+2][y-2],key == fivemap[x+3][y-3],key == fivemap[x+4][y-4]
                        isSuncess = False    #判断接下来的3个是否是key指

                        max = 1
                        while max < 4:
                            if key == fivemap[x+1+max][y-1-max]:
                                isSuncess = True
                            else:
                                isSuncess = False
                                break
                            max += 1
                        
                        if isSuncess:
                            return True

            y += 1
        x += 1
    return False
                

#定义棋盘
fivemap = []
ll = ['-']
length = int(input('请输入棋盘的长度：'))
# 定义列表长度
width = length * ll
# print(width)

#生成棋盘
i = 0
while i<length:
    fivemap.append(width.copy())
    i += 1
# print(fivemap)

#下棋

#定义玩家
play01 = 1
play02 = 2
isplay01 = True
def Check():
    str = '*'
    print(21*str)
    print('  0 1 2 3 4 5 6 7 8 9')
    num = 0
    for ii in fivemap:
        print(num,end=' ')
        for jj in ii:
            print(jj,end=' ')
        print()
        num += 1
    print(21*str)
    print()

while True:
#判断轮到谁
    if isplay01:
        while True:
          
            Check()
            while True:
                x = int(input('请输入play01x: '))
                if x >= length:
                    print('您输入的值越界,应小于length长度')
                    continue
                elif x < 0:
                    print('请输入length范围之内的数字')
                else:
                    break
            while True:
                y = int(input('请输入play01y: '))
                if y >= length:
                    print('您输入的值越界,应小于length长度')
                    continue
                elif y < 0:
                    print('请输入length范围之内的数字')
                else:
                    break
            #判断该位置上是否有值
            if fivemap[x][y] == '-':
                fivemap[x][y] = play01
                break
            else:
                print('该位置上已经有棋子,请重新找个位置放置棋子')
                continue
        isplay01 = False
        #判断play01是否胜利
        result = Win(fivemap,play01)
        if result:
            print('play01 胜利')
            break
    else:
        while True:
            Check()
            while True:
                x = int(input('请输入play02x: '))
                if x >= length:
                    print('您输入的值越界,应小于length长度')
                    continue
                elif x < 0:
                    print('请输入length范围之内的数字')
                else:
                    break
            while True:
                y = int(input('请输入play02y: '))
                if y >= length:
                    print('您输入的值越界,应小于length长度')
                    continue
                elif y < 0:
                    print('请输入length范围之内的数字')
                else:
                    break
            #判断该位置上是否有值
            if fivemap[x][y] == '-':
                fivemap[x][y] = play02 
                break
            else:
                print('该位置上已经有棋子,请重新找个位置放置棋子')
                continue 
        isplay01 = True
        #判断play02是否胜利
        result = Win(fivemap,play02)
        if result:
            print('play02 胜利')
            break

    #打印棋盘
    Check()

print('game over')
