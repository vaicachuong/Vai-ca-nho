l = list(map(int,input().split()))

list_max = max(l)
list_min = min(l)

for i in range(len(l)) : 
    if l[i] == list_max : 
        vi_tri_max = i 
    elif l[i] == list_min : 
        vi_tri_min = i

vi_tri_max = vi_tri_min
vi_tri_min = vi_tri_max

print(l)