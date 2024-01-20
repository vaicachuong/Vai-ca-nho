a = int(input())
s = 1
mau = 2 

while s < a :
    s += 1 / mau 
    mau += 1 
    if s > a :
        print(s) 
        break 
