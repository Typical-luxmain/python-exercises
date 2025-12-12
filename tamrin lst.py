#tamrin 1

lst= [1,5,8,12,7]
sum=0
for i in range (len(lst)):
    sum+=lst[i]
print (f"sum is {sum}")

#tamrin 2

lst=[12,6,36,45,8]
max=lst[0]
for i in range (len (lst)):
    if lst[i]>max:
        max=lst[i]
print (f"max is {max}")

#tamrin 3

lst=[1,56,213,56,324,12,56]
cnt=0
target=56
for i in range (len(lst)) :
    if lst[i]==target :
        cnt+=1
print(f"the count of your target is {cnt}")

#tamrin 4

lst=[12,56,1234,77,13,65]
even_lst=[]
for num in lst :
    if num % 2 == 0 :
        even_lst.append(num)
print(even_lst)

#tamrin 5

lst=[12,19,25,45,67,98]

#1st way:

lst_rev=[]
for i in range (1 , len(lst)+1):
    lst_rev.append(lst[-i])
print(lst_rev)

#2nd way:

lst.reverse()
print(lst)

#3rd way:

print(lst[::-1])

#tamrin 6

lst=[12,34,12,76,94,12,2]
new_lst=[]
for num in lst:
    if num  not in (new_lst) :
        new_lst.append(num)
print(new_lst)

#tamrin 7 

lst=["apple" , "grape" , "berry" , "orange" , "kiwi"]
for i in range (len(lst)):
    if lst[i]=="apple":
        lst[i]="orange"
print(lst)

#tamrin 8 

lst=[1,2,3,4]
new_lst=[]
for num in lst:
    new_lst.append(num*num)
print(new_lst)

#tamrin 9

lst=[1,4,8,12,10,28,56]
av=0
for i in range(len(lst)):
    av+=lst[i]
av=av/(len(lst))
cnt=0
for j in range (len(lst)):
    if lst[j]>av:
        cnt+=1
print(cnt)

#tamrin 10

lst=[
    [2,4,6],
    [12,14,16,18],
    [22,24,28]
]

for row in lst:
    sum=0
    for i in range (len(row)):
        sum+= int(row[i])
    print(sum)

#tamrin 11

lst=[
    [12,74,2],
    [23,75,34,56],
    [12,65,9]
]
max=lst[0][0]
for row in lst :
    for i in range(len(row)):
        if row[i]>max:
            max=row[i]
print(max)

#tamrin 12

matrix=[]
for i in range (1,11):
    row=[]
    for j in range (1,11):
        row.append(i*j)
    matrix.append(row)
for row in matrix:
    print (row)

#tamrin 13

import random
matrix=[]
for i in range (10) :
    row=[]
    for j in range (10):
        row.append(random.randint(0,5))
    matrix.append(row)

cnt=0
for row in matrix :
    for num in row:
        if num==0 :
            cnt+=1
print(cnt)









