'''
2.	迴圏的練習-factor
輸入一正整數，求其所有的因數。
說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。


'''


for idx in range(1,37):
    if (36%idx ==0):
        print(idx)