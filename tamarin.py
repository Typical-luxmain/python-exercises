# #tamrin 1

# week1=["ali" , "sara" , "reza" , "maryam" , "hossein"] 
# week2=["reza" , "maryam" , "nima" , "ali"]
# week3=["ali" , "maryam" , "nima" , "zahra"]

# #الف
# set1=set(week1)
# set2=set(week2)
# set3=set(week3)

# presence=set1&set2&set3
# print(presence)

# #ب
# f1=set1|set2|set3
# f2=f1 - presence
# print(f2)

# #ج
# f3= set1-set2-set3 | set2-set1-set3| set3-set1-set2
# print(f3)

# #tamrin 2
passwords=["aabbcc" , "abc123" , "111222" , "abcd"]

for password in passwords :
    if len(set(password)) < 5 :
        print (f"{password} is a weak password!")
# #tamrin 3
# a={1,2,3,5,7,9}
# b={1,2,3,5,7,9}
# c={1,3,4,6,8}

# #الف
# if a&b == a:
#     print ("a and b are cheaters!")

# if a&c == a:
#     print ("a and c are cheaters!")

# if c&b == b:
#     print ("b and c are cheaters!")

# #ب
# q=a&b | a&c | b&c
# print(q)

# #tamrin 4
# user1={"python" , "ai" , "data" , "math"}
# user2={"python" , "web" , "js" , "html"}
# user3={"ai" , "data" , "python"}

# #الف
# f1=user1&user2&user3
# print(f1)

# #ب
# f2=user1 - user2 - user3
# print(f2)

# #ج
# set1=user1&user2
# set2=user1&user3
# set3=user2&user3

# if set1>set2 and set1>set3:
#     print("user1 had the most in common")

# elif set2>set1 and set2>set3:
#     print("user3 had the most in common")

# else:
#     print("user2 had the most in common")

# #tamrin 5
# logs=[
#     {"ali" , "sara" , "reza"},
#     {"reza" , "maryam"},
#     {"ali" , "reza" , "nima"},
#     {"sara" , "reza"}
# ]

# #الف
# f1=logs[0]&logs[1]&logs[2]&logs[3]
# print(f1)

# #ب
# f2=logs[0]^logs[1]^logs[2]^logs[3]
# print(f2)