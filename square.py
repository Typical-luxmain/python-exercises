n = int(input())
if 3 <= n <= 10:   
    for i in range(n):  
        if i == 0 or i == n-1 :
            print ("*" * n)
        else :
             print ("*" + " " * (n-2) + "*")
else : 
    print ("enter a number between 3 and 10")