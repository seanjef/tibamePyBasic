def sum(n):
    if (n % 2)==0 and n >0:
        return n+sum(n-1)
    elif (n % 2) !=0 and n >0:
        return 0+sum(n-1)
    elif n ==0:
        return 0


print(sum(100))