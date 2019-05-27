'''
1.	迴圏的練習-expression
利用for迴圏計算12-22+32-42+…+492-502的值。

'''

result = 0
for idx in range(1,51):
    result += idx**2 if idx%2==1 else idx**2*(-1)

print(result)