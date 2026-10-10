# take input from user
price = float(input("Type the price : "))
dis = float(input("Type the discount : "))

# calculate the cost
cost = (price - (price*(dis/100)))

# print the result
print(round(cost,2))
