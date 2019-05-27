'''
6.	迴圏的練習-rope
若有一條繩子長3000公尺，每天剪去一半的長度，需多少天繩子的長度會短於5公尺。

'''

rope = 3000
count = 0
while rope/2 >5:
    count+=1
    rope /=2

print("需要{0}天長度會小於5公尺 ".format(count))