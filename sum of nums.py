a = int(input())
b = 0
if 1<= a <= 1000 :    
    for i in range (a+1) :
        b += i
    for j in range (1,a) :
        print (f"{j} +" , end= " ")
    print (a , end= " ")
    print (f"= {b}")