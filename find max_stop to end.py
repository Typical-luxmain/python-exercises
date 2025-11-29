num=input("enter a number: (enter stop to end)")
max_num=int(num)
while num != "stop" :
    num=int(num)
    if num > max_num :
        max_num=num
    num=input("enter a number: (enter stop to end)")
if num=="stop":
    print (f"end of program. your max is {max_num}")