'''
5.	迴圈的練習-prime
輸入一正整數，找出所有小於或等於的質數。
'''


result= []
tmp = []
try:
    while True:
        indata = input("請輸入一正整數:  ")
        indata = int(indata)
        for idx in range(1,indata):
            count = 0
            for idx2 in range(1,idx+1):
                if (idx%idx2 ==0) and idx !=1:
                    count +=1
            if count == 2:
                result.append(idx)
        print(result)
        result = []
except ValueError or TypeError as err:
    print(err)
