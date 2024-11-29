#shopping cart
item=input("what item do you want to purchase?: ")
price=float(input("What is the price of the item?: "))
quantity=int(input("How many items do you want to purchase?: "))
total=price*quantity

print(f"You have purchased {quantity}x amount of {item}")
print(f"Your total cost is: £{round(total)}.")

