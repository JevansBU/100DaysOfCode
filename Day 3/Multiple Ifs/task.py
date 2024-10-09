print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7 ")
    else:
        bill = 12
        print("Adult tickets are £12")

        wants_photo = input("Do you want a photo taken? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        #Adds 3 to there bill
        bill += 3
        #bill += 3 must be indented before printing bill
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

#If/Elif/Else and Mult If statements asks user about there height and
#if they want to pay for photos and then calculates there total bill