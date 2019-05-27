try:
    data = input("enter the month?  ")
    data = int(data)
    while type(data) == int and data <=12 :
        result = int(data/3)
        if result == 0 or result ==4:
            print("Winter")
            break
        elif result == 1:
            print("Spring")
            break
        elif result == 2:
            print("Summer")
            break
        elif result == 3:
            print("Fall")
            break
    exit(0)
except ValueError or TypeError:
    print("pls enter the number from 1 to 12..")