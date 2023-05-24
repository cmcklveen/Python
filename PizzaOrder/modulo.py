age = input("How old are you? ")

if int(age) < 12:
    print("Please pay $5 dollars")
elif int(age) < 18:
    print("Please pay $7 dollars")
else:
    print("Please pay $12 dollars")