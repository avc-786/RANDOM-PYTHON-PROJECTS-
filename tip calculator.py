# Display a welcome message to the user
print("Welcome to the tip calculator")
# Ask the user for the total bill amount and convert it to an integer
bill = int(input(("What was the total bill? ")))
# Ask the user for the tip percentage and convert it to an integer
tip = int(input("How much tip would you like to give? "))
# Ask the user for the number of people splitting the bill and convert it to an integer
people = int(input("How many people to split the bill? "))
# Convert the tip percentage to a decimal
tip_as_percent = tip / 100
# Calculate the total tip amount by multiplying the bill by the tip percentage
total_tip_amount = bill * tip_as_percent
# Calculate the total bill amount including the tip
total_bill = bill + total_tip_amount
# Calculate the amount each person needs to pay by dividing the total bill by the number of people
bill_per_person = total_bill / people
# Round the amount each person needs to pay to 2 decimal places
final_amount = round(bill_per_person, 2)
# Display the final amount each person needs to pay
print(f"Each person should pay {final_amount}")