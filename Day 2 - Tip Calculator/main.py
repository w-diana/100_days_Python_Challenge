#Objective:
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_people = int(input("How many people to split the bill? "))

amount_to_pay = (total_bill * float("1." + percentage_tip))/no_of_people
amount_to_pay = round(amount_to_pay,2)
print(f"Each person should pay: ${amount_to_pay}")


