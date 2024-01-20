l = list(map(int,input().split()))

L1 = []
L2 = []
L3 = []

for i in range(len(l)) : 
    if L1 == 0 : 
        L1.append(l[i])
    elif l[i] % 2 == 0 : 
        L2.append(l[i])
    else : 
        L3.append(l[i])

print(L2 + L1 + L3)