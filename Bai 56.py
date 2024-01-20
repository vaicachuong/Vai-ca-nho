n = int(input())
l_list = []
check = 0 
for i in range(1,n+1) :
    l = int(input()) 
    l_list.append(l)
for z in range(len(l_list)) : 
    if l_list[z] > 0 : 
        print(l_list[z], " la phan tu dau tien co dau duong")
        check = 1 
        break
if check == 0 : 
    print("-1")