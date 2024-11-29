year=0
def fut_val():
    print("\nThis program calculates the future value. ")
    year=(eval(input("\nEnter year of investment. ")))
    
    principal=eval(input("Enter the initial principal: "))
    apr=eval(input("Enter the annual interest rate: "))
    
    for i in range(20):
        principal=principal*(1+apr)
    print("The value in", year," years is", principal)
fut_val()