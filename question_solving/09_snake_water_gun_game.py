import random
def check(computer,user):
    if computer == user:
        print("Draw")
    elif computer == 0 and user == 2:
        print("Computer Wins")
    elif computer == 1 and user == 0:
        print("Computer Wins")
    elif computer == 2 and user == 1:
        print("Computer Wins")
    else:
        print("User Wins")

print("Let's Play stone paper scissor game!")
computer=random.randint(0,2)
user=int(input("0 for stone,1 for paper and 2 for scissor:"))

check(computer,user)
print(f"Computer Choosen {computer}")



