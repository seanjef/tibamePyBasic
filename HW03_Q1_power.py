'''
1.	函數的練習-power
寫一函數power(x, n)用來計算x的n次方。
說明：power (5,3)即計算5^3。

'''

def power(x,n):
    if n>=1:
        return x*power(x,n-1)
    else:
        return 1

print(power(5,3))