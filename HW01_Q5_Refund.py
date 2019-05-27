'''
5.	選擇性敘述的練習-refund
輸入在某商店購物應付金額與實付金額。
實付金額小於應付金額，則印出”金額不足”。
實付金額等於應付金額，則印出”不必找錢”。
實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。

'''
import math
try:
    while True:
        shpay, acpay = input("請輸入應付金額與實付金額: ").split(sep=" ")
        shpay, acpay = int(shpay), int(acpay)
        if acpay > shpay:
            col = (acpay - shpay)
            output = "應找回 "
            for idx in [1000,500,100,50,10,5,1]:
                tmp = math.floor(col / idx)
                if col / idx and idx>=100:
                    output += f'{tmp}張{idx}元 ' if tmp >1 else f'{tmp}張{idx}元 '
                    col =(col - idx*tmp) if col>idx else col%idx
                else:
                    output += f'{tmp}個{idx}硬幣 ' if tmp > 1 else f'{tmp}個{idx}硬幣 '
                    col = (col - idx * tmp) if col > idx else col % idx
            print(output)
        elif acpay == shpay:
            print("不必找錢")
        else:
            print("金額不足")
except ValueError or TypeError as err:
    print(err)



'''
>>> stock = 'tsmc'
>>> close = 217.5
>>> f'{stock} price: {close}'
'tsmc price: 217.5'
output += f'{math.floor(col/idx)}張{idx}元' if math.floor(col/idx) >1 else f'{math.floor(col/idx)}張{idx}元'

print(math.floor(col/idx))
'''
