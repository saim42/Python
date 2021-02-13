import datetime
def getdate():
    return datetime.datetime.now()
def lock(choice):
    if choice==1:
        print("Enter 1 for Exercise and 2 for Food\n")
        choi1=int(input())
        if choi1==1:
            text=input("Type please!!!\n")
            with open ("Saim_Exercise.txt","a") as sa:
                sa.write(str([str(getdate())])+":"+text+"\n")
            print("Enter Successfully")
        elif choi1==2:
            text = input("Type please!!!")
            with open("Saim_Food.txt","a") as sa:
                sa.write(str([str(getdate())])+":"+text+"\n")
            print("Enter Successfully\n")
    elif choice==2:
        print("Enter 1 for Exercise an 2 for food\n")
        ch=int(input())
        if ch==1:
            text=input("Type please!!!\n")
            with open ("Huraira_Ecercise.txt","a") as hu:
                hu.write(str([str(getdate())])+":"+text+"\n")
            print("Entered Successfully\n")
        elif ch==2:
            text = input("Type please!!!\n")
            with open("Huraira_Food.txt", "a") as hu:
                hu.write(str([str(getdate())]) + ":" + text + "\n")
            print("Entered Successfully\n")
    elif choice==3:
        print("Enter 1 for Exercise an 2 for food\n")
        cho=int(input())
        if cho==1:
            text=input("Type please!!!\n")
            with open ("Waleed_Ecercise.txt","a") as wa:
                wa.write(str([str(getdate())])+":"+text+"\n")
            print("Entered Successfully\n")
        elif cho==2:
            text = input("Type please!!!\n")
            with open("Waleed_Food.txt", "a") as wa:
                wa.write(str([str(getdate())]) + ":" + text + "\n")
            print("Entered Successfully\n")

def retrieve(choice):
    if choice==1:
        print("Enter 1 for exercise and 2 for food\n")
        ch=int(input())
        if ch==1:
            with open ("Saim_Exercise.txt") as sa:
                for i in sa:
                    print(i,end="")
        if ch==2:
            with open ("Saim_Food.txt") as sa:
                for i in sa:
                    print(i,end="")
    if choice==2:
        print("Enter 1 for Exercise and 2 for Food\n")
        chos=int(input())
        if chos==1:
            with open ("Huraira_Ecercise.txt") as hu:
                for i in hu:
                    print(i,end="")
        if chos==2:
            with open ("Huraira_Food.txt") as hu:
                for i in hu:
                    print(i,end="")

    if choice==3:
        print("Enter 1 for Ecercise and 2 for Food\n")
        chh=int(input())
        if chh==1:
            with open ("Waleed_Exercise.txt") as wa:
                for i in wa:
                    print(i,end="")
        if chh==2:
            with open ("Waleed_Food.txt") as wa:
                for i in wa:
                    print(i,end="")

print("Welcome To Health Management System")
print("Enter 1 for Locking And 2 for Retreiving\n")
choice=int(input())
if choice==1:
    print("Enter 1 for Saim, 2 for Huraira and 3 for Waleed\n")
    chose_Person=int(input())
    lock(chose_Person)
elif choice==2:
    print("Enter 1 for Saim, 2 for Huraira and 3 for Waleed\n")
    chose_Person=int(input())
    retrieve(chose_Person)