pos=0
neg=0
zero=0
for i in range (10):
    num=int(input(f"enter the {i+1} number: ") )
    if num > 0 :
        pos +=1 
    elif num <0 :
        neg +=1 
    else :
        zero +=1 
print (f"you have {pos} positive , {neg} negative and {zero} zero")