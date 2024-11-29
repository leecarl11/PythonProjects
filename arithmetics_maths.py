import math
#Arithmetic operators
#friends=10
#friends=friends + 1
#friends+=2
#friends-=2
#friends*=2
#friends/=2
#exponential to the power of any number
#friends**=2
#modulus, this gives the remainder of any division
#remainder=friends%7
#print(remainder)
#friends%=7
#print(friends)

#Maths builtin related functions
#x=3.14
#y=4
#z=5

#the round function
#result=(round(x*y+z)-1)
#result=abs(y)
#raising the base to a given power
#result=pow(4,3)
#maximum value
#result=max(x,y,z)
#result=min(x,y,z)
#print(result)
#print(math.pi)
#print(math.e)
#result=math.sqrt(25)
#print(round(result))
#x=9.9
#result=math.sqrt(x)
#result=math.ceil(x)
#rounds a number up
#result = math.floor(x)
#rounds a number down
#print(result)

#calculating the circumference of a circle

radius=float(input("enter the radius of a circle: "))
circumference=2*math.pi*radius
print(f"the circumference of a circle is {round(circumference,3)}cm")
input("\nPress the enter key to exit... ")