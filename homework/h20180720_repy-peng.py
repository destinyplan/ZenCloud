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
                if y+1 < length and key==fivemap[x][y+1]:
                    #再判断右侧三个棋格是否为key
                    # fivemap[x][y+2] fivemap[x][y+3] fivemap[x][y+4]
                    isSucess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if y+1+max < length and key==fivemap[x][y+1+max] :
                            isSucess=True
                        else:
                            isSucess=False
                            break
                        max+=1
                    if isSucess:
                        return True
                #right-down
            if key==elem:
                if x+1 < length and y+1 < length and key==fivemap[x+1][y+1]:
                    #再判断右下侧三个棋格是否为key
                    # fivemap[x+2][y+2] fivemap[x+3][y+3] fivemap[x+4][y+4]
                    isSucess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if x+1+max < length and y+1+max < length and key==fivemap[x+1+max][y+1+max] :
                            isSucess=True
                        else:
                            isSucess=False
                            break
                        max+=1
                    if isSucess:
                        return True
                # #down
            if key==elem:
                if x+1 < length and key==fivemap[x+1][y]:
                    #再判断下侧三个棋格是否为key
                    # fivemap[x+2][y] fivemap[x+3][y] fivemap[x+4][y]
                    isSucess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if  x+1+max < length and key==fivemap[x+1+max][y] :
                            isSucess=True
                        else:
                            isSucess=False
                            break
                        max+=1
                    if isSucess:
                        return True
                # right-up
            if key==elem:
                if y+1 < length and x-1 > 0 and key==fivemap[x-1][y+1]:
                    #再判断右上侧三个棋格是否为key
                    # fivemap[x-2][y+2] fivemap[x-3][y+3] fivemap[x-4][y+4]
                    isSucess=False#有没有成功扫描到3个元素
                    max=1
                    while max<4:
                        if  y+1+max < length and x-1-max > 0 and key==fivemap[x-1-max][y+1+max] :
                            isSucess=True
                        else:
                            isSucess=False
                            break
                        max+=1
                    if isSucess:
                        return True
            y+=1
        x+=1
    return False

fivemap = []
i = '-'
tag = i
c = [tag]
player1 = 1
player2 = 2
sp = True
leng=int(input('plz input num:'))
wth = leng*c
#print(wth)
for tag in wth:
    fivemap.append(wth.copy())
#print(fivemap)
#下棋
info = '{} win the game'
win=' '
while True:
    
    result=False
    if sp:
        print("当前该玩家player1落子")
        x=int(input("请输入x:"))
        y=int (input("请输入y:"))
         
           
    else :
        print("当前该玩家player2落子")
        a=int(input("请输入a:"))
        b=int(input("请输入b:")) 
         
      
    if sp:
        if fivemap[x][y] == tag:
            
            fivemap[x][y]=player1
            sp=False
            result = AI(fivemap,player1)
            win='player1'
        else:
            print("落子有误")
            continue      
    else:
        if fivemap[a][b] == tag:
            
            fivemap[a][b]=player2
            sp=True
            result = AI(fivemap,player2)
            win='player2'
        else:
            print("落子有误")
            continue
    
    
            
#打印棋局 
    num = 0
    print('    ***************')
         
    for m in fivemap:
        
        print(num,end=' ')
        for n in m:   
            print(n,end=' ')
        print(num)     
        print('')
       
        num+=1
    print('    ***************')     
    if result:
        break
print(info.format(win))
                 