# Taking input From the shopkeeper

item = input("What item would you like to buy?: ")
price = float(input("What is the price.?:$ "))
quantity = int(input("How much quantity of item entered does the customer need.?: "))

# Calculation

bill = price * quantity

# printing

print(f"You have bought {quantity} {item}. So the total bill is: ${bill}")