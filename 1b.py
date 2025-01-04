qty=int(input("Enter the quantity of item sold"))
price=int(input("Enter the price of one item"))
discount_percent=int(input("Enter the discount"))
tax=int(input("Enter the tax"))
total_price=price*qty
discount=(discount_percent/100)*total_price
discounted_price=total_price-discount
tax_price=(tax/100)*discounted_price
net_amount=discounted_price+tax_price
print("The Quantity is=",qty)
print("The Price=",price)
print("The Discount Percent=",discount)
print("The Tax Percent=",tax)
print("The Total price=",total_price)
print("The Discounted Price=",discounted_price)
print("The Tax=",tax_price)
print("Net amount",net_amount)


