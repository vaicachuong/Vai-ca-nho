n = int(input())
dem = 0 
du = 0 
nguyen = 0 
n = 0 
while True : 
    print(dem)
    du = n // 10 
    nguyen = du % 10 
    n = du 
    dem += 1
    if nguyen == 0 : 
        break
print(dem) 
    