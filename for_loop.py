operator=input("enter an operator: (+/*%) ")
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))

for i in range(5):

    if operator=="+":
        print(num1+num2)
    elif operator=="*":
        print(num1*num2)
        #operator = eval(input("enter a operator: "))
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    print(i, num1 + num2)



input("\press enter to exit")
#    if operator=="+":
#        print(num1+num2)
#    elif operator=="*":
#        print(num1*num2)
#    elif operator=="/":
#        print(num1/num2)
#else:
#    print("invalid operator")