n = int(input())
l_list = []
tong = 0
for i in range(1,n+1) : 
    l = int(input())
    l_list.append(l)

for z in range(len(l_list)) : 
    tong += l_list[z]

print(tong/len(l_list))