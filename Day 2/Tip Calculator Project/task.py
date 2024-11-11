print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
trueTip = float(tip / 10)
Total = float((bill / people) * trueTip)
float(Total)
Total_Amount = round(Total, 2)
print(f"Each person should pay = £{Total_Amount}")
#Day 2 Project Complete!!!!
#Created a tip calculator depending on how may people there are eating




