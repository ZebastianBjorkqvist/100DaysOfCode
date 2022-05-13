print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
numPpl = int(input("How many people to split the bill? "))

print(f"Each person should pay: {round((bill * (1+tip))/numPpl, 2)}")
