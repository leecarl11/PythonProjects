operator=input("Enter operator: (+ - * /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

#print(num1*num2)
if operator=="+":
    result=num1+num2
    print(round(result,3))
elif operator=="-":
        result=num1-num2
        print(round(result,3))
elif operator=="*":
            result=num1*num2
            print(round(result,3))
elif operator=="/":
                result=num1/num2
                print(round(result,3))
else:
    print(f"{operator} is not a valid operator")