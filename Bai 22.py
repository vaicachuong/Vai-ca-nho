toan = float(input())
van = float(input())
anh = float(input())

trung_binh = (toan + van + anh) / 3 

if trung_binh >= 8 and toan >= 8 or van >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5 : 
    print("Hoc sinh gioi")
if trung_binh >= 6.5 and toan >= 6.5 or van >= 6.5 and toan >= 5 and van >= 5 and anh >= 5 :
    print("Hoc sinh kha")
if trung_binh >= 5 and toan >= 5 or van >= 5 and toan >= 3.5 and van >= 3.5 and anh >= 3.5 :
    print("Hoc sinh trung binh")
if trung_binh >= 3.5 and toan >= 3.5 or van >= 3.5 and toan >= 2 and van >= 2 and anh >= 2 :
    print("Hoc sinh yeu")
else : 
    print("Hoc sinh kem")
