'''
4.	迴圏的練習-amstrong
Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
找出所有的Amstrong數。
說明：153=13+53+33，故153為Amstrong數。

'''

for idx in range(100,1000):
    #print(idx)
    tmp = []
    for i in str(idx):
        tmp.append(i)
        #print(i)
    con = (int(tmp[0])**3 + int(tmp[1])**3 + int(tmp[2])**3)
    if int(idx) == con:
        print(idx)

