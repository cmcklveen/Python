# Tip Calculator

print("Welcome to Tip Calculator")

# What was the total bill?

total_bill = input("What was the total bill? $")
#print(type(total_bill))
total_bill = float(total_bill)
#print (type(total_bill))

# Calculate tip percentage

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage =  int(tip) / 100
# print(percentage)
total_bill_plus_tip = total_bill + total_bill * percentage
# print(total_bill_plus_tip)

# How many people are splitting the bill?

people = input("How many people to split the bill? ")
people = int(people)

cost_per_person = total_bill_plus_tip / people
cost_per_person = round(cost_per_person, 2)

print(f"Each person should pay: ${cost_per_person}")