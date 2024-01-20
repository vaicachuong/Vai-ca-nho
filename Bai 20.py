month = int(input())
year = int(input())

if month == 2 : 
    if year % 4 == 0 or (year % 100 == 0 and year % 400 != 0) : 
        print("29")
        
if 0 < month < 13 :
    if month == 2 : 
        print("28")
    else : 
        print("31")
    