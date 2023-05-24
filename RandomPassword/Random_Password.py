import random

print("Password Generator")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','*','(',')']

range_of_letters = input("Enter number of letters wanted in your password. ")
range_of_numbers = input("Enter the number of numbers wanted in your password. ")
range_of_symbols = input("Enter the number of symbols wanted in your password. ")
password_list = []
password = ""

for character in range(1,int(range_of_letters) + 1):
    random_character = random.choice(letters)
    password_list += str(random_character) 

for number in range(1,int(range_of_numbers) + 1):
    random_number = random.choice(numbers)
    password_list += str(random_number)

for symbol in range(1,int(range_of_symbols) + 1):
    random_symbol = random.choice(symbols)
    password_list += str(random_symbol)

random.shuffle(password_list)


for character in password_list:
    password += character
    

#print(password_list)

#print(password_list)
print(f"Your new password is {password}")

