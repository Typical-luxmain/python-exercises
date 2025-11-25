a = input()
b = input()
rev_a = a[::-1]
rev_b = b[::-1]
if rev_a < rev_b :
    print (a, "<" ,b)
elif rev_b < rev_a :
    print (b, "<" ,a)
else :
    print (a, "=" ,b)
