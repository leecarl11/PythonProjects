print(
    """
                           Restaurant Bill
    """
)
fifteen_percent=0.15
twenty_percent=0.20
soup=float(input("soup: "))
chicken=float(input("chicken: "))
ribs=float(input("ribs: "))
noodles=float(input("noodles: "))
wings=float(input("wings: "))

total_bill=soup+chicken+ribs+noodles+wings
print("\nGrand total bill with:",total_bill + fifteen_percent,"fifteen_percent tip added! ")
print("\nGrand total bill with:",total_bill + twenty_percent,"twenty_percent tip added! ")
input("\nPress Enter to Exit")