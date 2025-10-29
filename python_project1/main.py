import random
computer = random.choice([-1, 0, 1])
youstr = input("enter the guess: ")
youdict = {"s": 1,"w": -1,"g": 0}
revdict = {1: "snake", -1: "water", 0: "gun"}
you = youdict[youstr]
print(f"the computers choice is {revdict[computer]} \n your choice is {revdict[you]}")
if computer == you:
    print("its a tie")
elif (computer ==1 and you ==0):
     print("you win")
elif(computer ==1 and you == -1):
     print("you lose")
elif(computer ==0 and you ==1):
        print("you lose")
elif(computer ==0 and you == -1):
        print("you win")
elif(computer ==-1 and you ==1):
        print("you win")
elif(computer ==-1 and you ==0):
        print("you lose")
else:
       print("somtheing went wrong")
    

