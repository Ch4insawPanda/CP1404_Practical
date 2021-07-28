'''
Pseudocode:
Get TotalItems, ItemPrices
Calculate TotalPrice
Check Discount
Display TotalItems, TotalPrice
'''
TotalPrice = 0
TotalItems: int = int(input("Number of items: "))
while TotalItems <= 0:  #To make sure the number of items is greater than 0
    print("Error:Invalid Number of Items")
    TotalItems = int(input("Number of items: "))
for i in range(TotalItems):   #This range is to get the individual price for each of the items
    ItemPrice = float(input("Price of item: $"))
    TotalPrice += ItemPrice
if TotalPrice > 100:    #This if-else is to check if the user is eligible for discount
    Discount = .1
else:
    Discount = 0
NewTotalPrice = TotalPrice*(1-Discount)
print(f'Total price of {TotalItems} is ${NewTotalPrice:.2f}')