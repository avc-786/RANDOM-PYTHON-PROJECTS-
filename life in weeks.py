# this block of code will tell your life in weeks 
# Ask the user for their age and convert it to an integer
age = int(input("What is your age? "))
# Calculate the number of years left until the user is 80
years_left = 80 - age
# Calculate the number of days left until the user is 80
daysleft = years_left * 365 
# Calculate the number of weeks left until the user is 80
weeksleft = years_left * 52 
# Calculate the number of months left until the user is 80
monthsleft = years_left * 12 

# Format the outcome string with the calculated values
outcome = (f"You have {daysleft} days, {weeksleft} weeks, {monthsleft} months left.")
# Print the outcome to the user
print(outcome)