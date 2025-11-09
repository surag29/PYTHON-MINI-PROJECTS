import random
n = random.randint(1,100)
a = -1
guess = 1

while(n!=a):
    a = int(input("enter your guess here : "))
    if(a>n):
        print("enter lower number ")
        guess += 1
    elif(a<n):
        print("enter higher number ")
        guess += 1
print(f"the correct guessed number is {n} in these many attempts {guess}")