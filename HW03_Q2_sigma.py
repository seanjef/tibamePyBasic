'''
2.	函數的練習-sigma
寫一函數my_fun (x, n)如下：

提示：利用上題的power(x,n)和課堂上的factorial(n)來完成。

'''
def fac(x):
    if x>0:
        return x*fac(x-1)
    elif x ==0:
        return 1


def power(x,n):
    if n>=1:
        return x*power(x,n-1)
    else:
        return 1







