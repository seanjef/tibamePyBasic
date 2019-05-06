'''
3.	選擇性敘述的練習-electricity
輸入何種用電和度數，計算出需繳之電費。
電力公司使用累計方式來計算電費，分工業用電及家庭用電。
                   	   家庭用電        工業用電
   240度(含)以下			0.15元			0.45元
   240~540(含)度   		0.25元			0.45元
   540度以上        	    0.45元			0.45元
'''
import pandas as pd
RefHome = {'ElecRate':[0,240,540],
           'HomeUse': [0.15,0.25,0.45],
           'InduUse': [0.45,0.45,0.45]}

df = pd.DataFrame(RefHome)
try:
    while True:
        elecType, elecNum = input("輸入用電型態(家用:H, 企業:I)與使用度數(空格區分) : ").split(" ")
        elecNum = int(elecNum)
        key = 0
        fee = 0
        typeInfo = ''
        #確認電費級別
        for idx in range(len(RefHome['ElecRate'])):
            if elecNum > RefHome['ElecRate'] [-idx]  :
                key = idx
        if elecType == 'H' and type(elecType) == str:
            typeInfo = 'HomeUse'
        else:
            typeInfo = 'InduUse'
        print('Range: {0} , ElecType: {1}, Number: {2}'.format(key, typeInfo, elecNum))
        tmpNum = elecNum
        for idx in range(-1, -key-idx, -1):
            while tmpNum > RefHome['ElecRate'][idx]:
                fee = fee + RefHome[typeInfo][idx] * (tmpNum - RefHome['ElecRate'][idx])
                tmpNum = RefHome['ElecRate'][idx]
                print("###### idx{0}, key{1}, HomeUse{2}, fee{3}".format(idx,key,RefHome['ElecRate'][idx],fee))
        print('總計:\t\t\t\t\t{0}元'.format(fee))
except ValueError or TypeError:
    print("請輸入正確格式!")