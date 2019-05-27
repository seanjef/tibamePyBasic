'''
10.	迴圈敘述的練習-nine_nine
   印出下列九九乘法表：
   		|	1	2	3	4	5	6	7	8	9
    -----------------------------------------------------------------
     9	|	9	18	27	36	45	54	63	72	81
     8	|	8	16	24	32	40	48	56	64
     7	|	7	14	21	28	35	42	49
     6	|	6	12	18	24	30	36
     5	|	5	10	15	20	25
     4	|	4	8	12	16
     3	|	3	6	9
     2	|	2	4
     1	| 	1

'''
for i in range(0,10):  #col
    col = ''
    for j in range(10,i,-1): #row
        if i==0 and j==10:
            col = "\t|"
            k=1
            while i ==0 and j ==10 and k<=9:
                col += ('\t' + str(k))
                k = int(k)
                k += 1
                if k<=9:
                    continue
                elif k>9:
                    col +=('\n' + '---'*14)
                    print(col)
        if i ==0 and j <=9:
            col = '  '
            col +=(str(j)+' |')
            print(col)
            #continue
        elif i>=1 and j<=9:
            col +='\t' + str(j*i)
            #print(col)
        col =''



