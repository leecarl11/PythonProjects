#if = Do some code only IF some condition is True
#    Else do something else

#age=int(input("Enter your age: "))

#if age >= 100:
#    print("You are too old. ")
#elif age >= 18:
#    print("try again. ")
#elif age >= 100:
#    print("you are too old! ")
#else:
#    print("You are now signed up. ")

#response=input("would you like food? (Y/N): ")

#if response=="Y":
#    print("Have some food. ")
#else:
#    print("No food for you. ")

name=input("Enter your name: ")

if name=="":
    print("Please enter your name. ")
else:
    print(f"Hello {name}, how are you doing?")

online=False
if online:
    print(f"The user {name},is online. ")
else:
    print(f"The user {name}, is offline. ")
    print("try again tomorrow. ")