# Print a welcome message to the user
print("Welcome to python pizza deliveries")
# Ask the user for their preferred pizza size and store their response
size = input("What size pizza do you want? Small, Medium, or Large? ")
# Ask the user if they want pepperoni on their pizza and store their response
add_pepperoni = input("Do you want pepperoni? Yes or No: ")
# Ask the user if they want extra cheese on their pizza and store their response
extra_cheese = input("Do you want extra cheese? Yes or No: ")

# Initialize the bill to zero to keep track of the total cost
bill = 0 

# Determine the base cost of the pizza based on its size
if size == "Small": 
    bill = bill + 25  # Add $25 to the bill for a Small pizza
elif size == "Medium":
    bill = bill + 20  # Add $20 to the bill for a Medium pizza
else:
    bill = bill + 25  # Add $25 to the bill for a Large pizza

# Check if pepperoni is added and adjust the bill accordingly
if add_pepperoni == "Yes":
    if size == "Small": 
        bill = bill + 2  # Add $2 to the bill for pepperoni on a Small pizza
    else:
        bill = bill + 3  # Add $3 to the bill for pepperoni on a Medium or Large pizza
# Check if extra cheese is added and adjust the bill
if extra_cheese == "Yes":
    bill = bill + 1  # Add $1 to the bill for extra cheese

# Print the final total bill to the user
print(f"Your final bill is {bill}")