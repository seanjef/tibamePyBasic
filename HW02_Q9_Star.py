for idx in range(1,6):
    print('*'*idx)

print("--------------")

for idx in range(6,1,-1):
    print('*'*idx)

print("--------------")

print("5層")
level =5
out = ''
for i in range(1,level+1):
    out += ' ' * (level - i)
    for j in range(1,i+1):
        out += '* '
    out += ' ' * (level - 1)
    print(out)
    out = ''