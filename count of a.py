x=input("enter a string: ")
counter=0

for ch in x :
    if ch.lower()=="a":
        counter+=1
print (f"the count of a is {counter}")