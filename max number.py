a= int(input("enter the 1st number"))
b= int(input("enter the 2nd number"))
c= int(input("enter the 3rd number"))
if a>b and a>c :
    print (f"{a} is max")
elif b>a and b>c :
    print (f"{b} is max")
else:
    print (f"{c} is max")