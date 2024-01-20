import random
n = int(input())
l_list = []

for i in range(1,n+1) : 
    l = int(input())
    l_list.append(l)

phan_tu_1 = random.randint(0,len(l_list))
phan_tu_2 = random.randint(0,len(l_list))
print(phan_tu_2)
print(phan_tu_1)
tong = l_list[phan_tu_1] + l_list[phan_tu_2] 
print(tong)
if tong % 2 != 0 : 
    print("list chan le")