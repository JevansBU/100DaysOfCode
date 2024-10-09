print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Tickets are £5")
    elif age <= 18:
        print("Tickets are £7")
    else:
        print("Tickets are £12")
else:
    print("Sorry you have to grow taller before you can ride.")

#Asks for your height and age and then specifies how much you have to pay
#for tickets depending how old you are
  
