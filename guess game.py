import random 

wins=0
losses=0
used_nums=[]
def create_number():
    global y
    y=random.randint(1,100)
    if y in used_nums:
        create_number()
    else:
        used_nums.append(y)
        return y
     

def check_guess():
    attempts=6
    global x , wins , losses
    for i in range(attempts):
        x=int(input("guess the secret number: "))
        if x>y :
            print(f"the secret number is lower than {x}")

        elif y>x :
            print(f"the secret number is higher than {x}")

        else:
            print(f"{x} is the secret number!")
    
            wins+=1
            ask_continue()
            return
    print(f"you lost! the secret number was {y}")
    losses+=1
    ask_continue()

def ask_continue():
    n=input("do you want to continue? (yes/no)")
    if n=="yes":
        create_number()
        check_guess()
        ask_continue()
    else:
        show_score()

def show_score():
    print(f"wins{wins} , losses{losses}")


create_number()
check_guess()
ask_continue()


    
