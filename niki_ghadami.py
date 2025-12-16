##tamrin 1

# def fact(x):
#     if x==1:
#         return 1
#     return x*fact(x-1)
    
# x=int(input("enter a number (enter 0 to end): "))
# while x != 0: 
#     print(fact(x))
#     x=int(input("enter a number (enter 0 to end): "))
# else:
#     print("the end")

##tamrin 2

# lst=[]
# no_dupli=[]

# x=input("enter a number (enter stop to end): ")
# while x!= "stop":
#     x=int(x)
#     lst.append(x)
#     x=input("enter a number (enter 0 to end): ")
    

# def remove_duplicate():
#     for i in range (len(lst)) :
#         if lst[i] not in no_dupli :
#             no_dupli.append(lst[i])

# remove_duplicate()
# print(no_dupli)

##tamrin 3



##tamrin 4

# lst=[]
# sort=False
# x=input("enter a number (enter stop to end: )")
# while x != "stop" :
#     x=int(x)
#     lst.append(x)
#     x=input("enter a number (enter stop to end: )")

# def is_sorted():
#     for i in range (len(lst)-1):
#         if lst[i] > lst[i+1] :
#             sort=True
        
# is_sorted()
# if sort==True:
#     print("list is sorted")
# else:
#     print("list is not sorted")

##tamrin 5

# x=int(input("enter a number"))
# def digit_sum(x):
#     if x <= 0:
#         return 0
#     return x % 10 + digit_sum(x // 10)

# print(digit_sum(x))

##tamrin 6

# x=int(input("enter a number: "))

# def sum_rec(x):
#     if x== 1 :
#         return 1
#     return x+sum_rec(x-1)

# print(sum_rec(x))

##tamrin 7

# x=int(input("enter a number: "))

# def mult_rec(x):
#     if x==1 :
#         return 1
#     return x*mult_rec(x-1)

# print(mult_rec(x))

##tamrin 8

# x=int(input("enter a number: "))

# def count_down(x):
#     if x==1:
#         print(1 , end=" ")
#         return 
#     print(x , end=" ")
#     count_down(x-1)
#     print(x , end=" ")
    
    

# count_down(x)

##tamrin 9

# x=int(input("enter a number: "))

# def digits(x):
#     global y
#     y=0
#     if x<10:
#         return 1
#     return 1 + digits(x//10)

# print(digits(x))

##tamrin 10

x=input("enter a string: ")

def print_reverse(x):
    if len(x)==0 :
        return ""
    return print_reverse(x[1:]) + x[0]

print(print_reverse(x))




