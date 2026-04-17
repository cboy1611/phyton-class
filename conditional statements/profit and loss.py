cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
if selling_price > cost_price:
    print("Profit: ", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss: ", cost_price - selling_price)
else:
    print("No profit, no loss.")                