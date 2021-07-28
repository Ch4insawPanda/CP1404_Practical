"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter Sales: $"))
while sales > 0:
    if sales < 1000:
        BonusPercentage = .1   #10% bonus below $1000 in sales
    else:
        BonusPercentage = .15   #15% bonus for above $1000 in sales
    BonusAmount = sales*BonusPercentage    #To calculate how much the actual bonus is
    print(f'Your bonus for ${sales:.2f} is ${BonusAmount:.2f}')
    sales = float(input("Enter Sales: $"))
print("Goodbye")