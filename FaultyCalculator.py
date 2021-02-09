print("Enter first number")
fNum=int(input())
print("Enter second number")
sNum=int(input())
print("Enter the operation you want to perform")
operation=int(input())
calculator={45*3:555,56+9:77,56/6:4}
if fNum==45 and sNum==3 and operation==2:
    print(calculator[45*3])
elif fNum==56 and sNum==9 and operation==1:
    print(calculator[56+9])
elif fNum==56 and sNum==6 and operation==3:
    print(calculator[56/6])
elif operation==1:
    print(fNum+sNum)
elif operation==2:
    print(fNum*sNum)
elif operation==3:
    print(fNum/sNum)