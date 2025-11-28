i=1
a=1
b=1
print (a,b, end=",")
while i<21 :
    c=a+b
    (a,b)=(b,c)    
    i+=1
    print ( c , end= ",")
