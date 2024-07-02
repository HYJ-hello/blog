def diffcult():
    
    import random as r
    print('-----欢迎来到猜数字小游戏------')
    print('-----困难模式（只有5次机会）-----')
    Key = int(r.randint(1,100))
    for i in range(5):
        num = int(input('请猜一个数'))
        if (num == Key):
            print('恭喜你！猜对了！')
            break
        if (num > Key):
            print('大了，再猜一次吧！')
        if (num < Key):
            print('小了哟~')
    print("-----游戏结束-----")