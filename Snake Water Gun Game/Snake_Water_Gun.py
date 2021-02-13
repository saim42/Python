import  random

won_by_comp=0
won_by_u=0
# no_of_turns=10
no_of_attempts=0
while (no_of_attempts<10):
    print("Enter Your Choice")
    choice =random.choice(["Snake", "Water", "Gun"])
    User_Choice = input()
    if User_Choice==choice:
        print("Same Option Picked!!!")
        no_of_attempts=no_of_attempts+1
    elif User_Choice=="Snake" and choice=="Water":
        print("You won")
        won_by_u=won_by_u+1
        no_of_attempts=no_of_attempts+1
    elif User_Choice=="Snake" and choice=="Gun":
        print("Computer won")
        won_by_comp=won_by_comp+1
        no_of_attempts = no_of_attempts + 1
    elif User_Choice=="Gun" and choice=="Snake":
        print("You won")
        won_by_u=won_by_u+1
        no_of_attempts = no_of_attempts + 1
    elif User_Choice == "Gun" and choice == "Water":
        print("Computer won")
        won_by_comp = won_by_comp + 1
        no_of_attempts = no_of_attempts + 1
    elif User_Choice=="Water" and choice=="Gun":
        print("You won")
        won_by_u=won_by_u+1
        no_of_attempts = no_of_attempts + 1
    elif User_Choice == "Water" and choice == "Snake":
        print("Computer won")
        won_by_comp=won_by_comp+1
        no_of_attempts = no_of_attempts + 1
    else:
        print("You Have Select Wrong Opion")
if won_by_u > won_by_comp:
    print("You Have Won This Game total Points=",won_by_u)
elif won_by_u==won_by_comp:
    print("Tie")
elif won_by_comp> won_by_u:
    print("Computer won This Game total Points=", won_by_comp)




