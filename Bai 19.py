import math
a = int(input())
b = int(input())
c = int(input())

delta = pow(b,2) - 4*a*c

if delta > 0 : 
    print("phuong trinh co 2 nghiem phan biet")
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print(x1)
    print(x2)
if delta < 0 : 
    print("phuong trinh co 1 nghiem kep")
    x = -b/2*a
    print(x)
else : 
    print("phuong trinh vo nghiem")