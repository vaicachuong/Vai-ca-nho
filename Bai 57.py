n = int(input())
l_list = []
l_list_am = []
check = 0 
for i in range(1,n+1) :
    l = int(input()) 
    l_list.append(l)

for z in range(len(l_list)) : 
    if l_list[z] < 0 :
        l_list_am.append(l_list)

print(max(l_list_am))