'''
3.	迴圏的練習-perfect_number
一個數字若等於其所有因數的總和，則此數為perfect number。
找出100以內所有的完美數。
說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。

'''

import numpy as np
result= []
tmp = []
for idx in range(1,101):
    for idx2 in range(1,idx+1):
        if (idx%idx2 ==0) and idx !=1:
            #print(idx2) #列出每個數的所有因數
            tmp.append(idx2)
    print("#############")
    print("length:{0} and array:{1}".format(len(tmp),tmp))
    row = 0
    tmp2= 0
    for row in range(0, len(tmp)-1):
        tmp2 += tmp[row]
        print(tmp2)

    if tmp2 == idx:
        print("tmp2:{0}  tmp[len(tmp)-1]:{1}".format(tmp2, idx))
        result.append(tmp2)

    tmp = []
print("Final answer:{0}".format(result))
    #print(tmp)

