from contextlib import closing


def greet_cusstomer():
    print("Welcome to the Lemonade stand!")
    print("fresh lemonade, made just for you.")

    #part 2: call the greet_customer function
greet_cusstomer()

#part 3:ask for the price per cup and the number of cups sold
price_per_cup = float(input("Enter the price per cup per dollars: "))   
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price,cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)  

rounded_total = round(total_cost, 2)
print("total cost:",rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid, rounded_total)
print("Change due:", change_due, 2)
def thank_you_message(cups):
    if cups >= 5:
        return "wow,big order! thanks so much for your support!"
    else: 
        return "thanks for stopping by the stand!"
    
closing_message = thank_you_message(cups_sold)
print("")
print("===== LEMONADE STAND RECIEPT =====")
print("price per cup:", price_per_cup)
print("cups sold:", cups_sold)
print("total cost:", rounded_total)
print("amount paid:", amount_paid)
print("change due:", rounded_total)
print(closing_message)
print("===================================")