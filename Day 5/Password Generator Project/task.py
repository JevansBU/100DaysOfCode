

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy Level First
import random
password = []

print("Welcome to the PyPassword Generator Bean!")

nr_letters = int(input("How many letters would you like in your password?\n"))

for LetterGen in range(1, nr_letters + 1):         #This for loop generates the letters for the password 'x' amount of times 'x' being the users input
    usersL = random.choice(letters)
    password += usersL

nr_symbols = int(input(f"How many symbols would you like?\n"))

for SymbolGen in range(1, nr_symbols + 1):
    usersS = random.choice(symbols)               #Same as letters generator ^^^^
    password += usersS

nr_numbers = int(input(f"How many numbers would you like?\n"))

for NumbersGen in range(1, nr_numbers + 1):
    usersN = random.choice(numbers)              #Same as letter generator ^^^^
    password += usersN

finalEpass = ""           #This converts the list into a string so it can be printed all together VVV

for easyPass in password:
     finalEpass += easyPass

print(f"Your simple password is = {finalEpass}")

#Hard Level

finalCpass = ""
x = password                #This shuffles the list and then converts into a string
random.shuffle(x)
for complexPass in x:
    finalCpass += complexPass

print(f"Your Complex Password is = {finalCpass}")




