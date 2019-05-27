'''
4.	選擇性敘述的練習-leapYear
輸入一西元年，如2015。判斷此年份是否為閏年。
提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
'''


try:
    while True:
        data = input("請輸入年分: ")
        data = int(data)
        if ((data % 4 == 0) and (data % 100 != 0)) or((data % 400==0) and (data % 4000 != 0)):
            print("%d 是閏年".format(data))
        else:
            print("%d 非閏年".format(data))

except ValueError or TypeError as err:
    print(err)