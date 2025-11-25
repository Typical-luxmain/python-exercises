n=input("enter a string: ")
digit=0
ch=0
other=0
for i in range (len(n)):
    if n[i].isdigit():    
        digit +=1
    if n[i].isalpha():
        ch+=1
    else:
        other+=1
print (f"the number of digits={digit} , characters={ch} , others={other}")