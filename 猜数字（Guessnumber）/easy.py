def easy():

    import random as r
    print('-----欢迎来到猜数字小游戏------')
    print('-----简单模式-----')
    Key = int(r.randint(1,100))
    while True:
        num = int(input('请猜一个数'))
        if (num == Key):
            print('恭喜你！猜对了！')
            break
        if (num > Key):
            print('大了，再猜一次吧！')
        if (num < Key):
            print('小了哟~')