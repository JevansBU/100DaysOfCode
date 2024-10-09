mod = 10 % 3
print(float(mod))

# Gives 'How many is remaining' after the equation

divNumber = input("Pick a number that you'd like to divide")
divNumber2 = input(f"And what would you like to divide " + divNumber + " by?")
divTotal = (int(divNumber) / int(divNumber2))
divTotal2 = round(divTotal, 4)
print(f"This is your Divided Total = {divTotal2}")
newFigure = (int(divNumber) % int(divNumber2))
if newFigure == 0:
    print("There are NO remainders")
else:
    print("There are remainders!!!")

#Modulu = % which calculates how many remainders there are in a division
#This code asks you what numbers you want to divide and then calculates the division and the remainders amount
