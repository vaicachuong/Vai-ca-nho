l = input().split()
Max = ""
for i in l : 
    if len(i) > len(Max)  : 
        Max = i 
print(l.index(Max))