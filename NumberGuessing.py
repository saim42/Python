num=42
no_of_guesses=10
no_of_attempts=0
while(True):
    print("Enter your guess")
    guess=int(input())
    no_of_attempts=no_of_attempts+1
    if guess==42:
        print("congrates you have guessed in" , no_of_attempts)
        break
    elif guess<42:
        no_of_guesses=no_of_guesses-1
        print("Enter greater number\n","No of Gusses left=",no_of_guesses)
        continue
    elif guess>42:
        no_of_guesses = no_of_guesses - 1
        print("Enter Smaller number\n", "No of Gusses left=", no_of_guesses)
        continue
    if no_of_guesses==0:
        print("Soory u have no more guess left")
    else:
        continue
