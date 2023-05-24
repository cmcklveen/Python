# BMICalculator Calculator

score = 97

kilos = input("Enter your weight in kilograms. ")
meters = input("Enter your height in meters. ")

# f string

print(f"You entered a weight of {kilos}kg and a height of {meters}m\n")

bmi =  float(int(kilos) / float(meters) * float(meters))

print(f"Your BMI is {bmi}")