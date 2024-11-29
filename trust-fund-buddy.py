print(
"""

                                        Trust Fund Buddy


Totals your monthly spending so that your trust fund doesn't run out
(and you're to get a real job).

Please enter the requested, monthly costs. Since you are rich, ignore pennies
and use only dollar amounts.

"""
)

car=int(input("Lamborghini Tune-Ups: "))
#car=int(car)

rent=int(input("Manhattan Apartment: "))
jet=int(input("Private Jet Rental: "))
gifts=int(input("Gifts: "))
food=int(input("Dining Out: "))
staff=int(input("staff(butlers,chef,driver,assistant): "))
guru=int(input("Personal Guru and Coach: "))
games=int(input("Computer Games: "))

total=car+rent+jet+gifts+food+staff+guru+games
print("\nGrand total:",total)

input("\n\nPress the enter key to exit. ")
