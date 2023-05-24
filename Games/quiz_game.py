print("Welcome to My Computer Quiz")

playing = input("Do you want to play my game? ")

if playing != "yes": 
    quit()

print("OK, Let's play :)")

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")