#def change():
#    print("\nPrint change counter")
#    #print()
#    print("\nPlease enter the count of each coin type. ")
#    quarters=int(input("Quarters: "))
#    dimes=int(input("Dimes: "))
#    nickels=int(input("Nickels: "))
#    pennies=int(input("Pennies: "))
#    total=quarters *.25 + dimes * .10 + nickels * .05 + pennies * .01
#    print()
#    print("The total value of your change is ", total)
#change()

#import math

#def main():
#    print("This program finds the real solutions to a quadratic: ")
#    print()
    
#    a=float(input("enter coefficient a: "))
#    b=float(input("enter coefficient b: "))
#    c=float(input("enter coefficient c: "))
#    
#    discRoot=math.sqrt(b*b-4*a*c)
#    root1=(-b+discRoot)/(2*a)
#    root2=(-b-discRoot)/(2*a)
#    print()
#    print("the soutions are:", root1,root2) 
#main()

print()
def main():
    n=int(input("please enter a whole number: "))
    fact=1
    for factor in range(2,n+1):
        fact=fact*factor
    print("the factorial of ", n, "is",fact)

main()