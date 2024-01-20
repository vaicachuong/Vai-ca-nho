l = input().split()

n = 10**9
m = ""

for i in l : 
    if i.isnumeric() and n > int(i) : 
        n = int(i)
    elif i.isalpha() and len(i) > len(m) : 
        m = i

print(n,m)