#Simple pyramid pattern
no_of_rows=int(input("Enter no of rows:\n"))
for i in range(0,no_of_rows):
    for j in range(0,i+1):
        print("* ",end=" ")
    print("\n")

#180 degree rotation
no_of_rows1=int(input("Enter No Of Rows:\n"))
k=2*no_of_rows1-2
for i in range(0,no_of_rows1):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")

#Printing Triangle

no_of_rows2=int(input("Enter No Of Rows:\n"))
k=no_of_rows2-1
for i in range(0,no_of_rows2):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")

