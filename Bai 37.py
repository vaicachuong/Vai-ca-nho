list_a = []
while True : 
    a = int(input())
    list_a.append(a)
    if a == -1 : 
        list_a.remove(-1)
        break 
print(max(list_a))
print(min(list_a))