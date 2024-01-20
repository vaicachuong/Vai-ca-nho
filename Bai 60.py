n = int(input())
l_list = []
tong = 0
for i in range(1,n+1) : 
    l = int(input())
    l_list.append(l)

if l_list == sorted(l_list) : 
    print("True")

else : 
    print("False")