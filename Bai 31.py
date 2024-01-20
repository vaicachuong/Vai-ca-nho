a = int(input())
b = int(input())

if a > b : 
    for i in range(1,a+1) : 
        if a % i == 0 and b % i == 0 : 
            print(i)
if a < b : 
    for i in range(1,b+1) : 
        if a % i == 0 and b % i == 0 : 
            print(i)
else : 
    for i in range(1,a+1) : 
        if a % i == 0 and b % i == 0 : 
            print(i)
