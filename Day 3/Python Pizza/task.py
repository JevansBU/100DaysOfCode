print("Welcome to Python Pizza Deliveries!")


bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input >:(")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3



extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill}.")

#This code asks the user what size pizza they want, if they want extra
#pepperoni and/or cheese and then calculates there bill for them


