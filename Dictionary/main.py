programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.","Function": "A piece of code that you can easily call over and over again."}



programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary["Loop"])

empty_dictionary = {}

programming_dictionary = {}
print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Print score of element

print(student_scores["Ron"])

# Adding new items to dictionary

student_scores["Nga"] = "99"

print(student_scores["Nga"])

# Create a empty dictionary
empty_directory = {}

# existing dictionary
# student_scores = {}

print(student_scores["Nga"])

student_scores["Nga"] = "100"

print(student_scores["Nga"])

# Loop through a dictionary
for key in student_scores:
    print(key)
    print(student_scores[key])