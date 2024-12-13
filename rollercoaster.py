# Welcome message to the rollercoaster ride
print("WELCOME TO THE ROLLERCOASTER!!!! ")
# Ask for the number of riders and convert the input to an integer
num_riders = int(input("How many people want to ride the rollercoaster? "))
# Initialize the bill to zero to keep track of the total cost of tickets and any additional services
bill = 0  
# Loop through each rider
for i in range(num_riders):
    # Ask for the height of each rider and convert the input to an integer
    height = int(input(f"Enter the height of rider {i+1} in cm: "))
    # Check if the rider is tall enough to ride
    if height >= 120:
        # Ask for the age of the rider and convert the input to an integer
        age = int(input(f"What is the age of rider {i+1}? "))
        # Determine the ticket price based on age
        if age < 12:
            # Add the child ticket price to the bill and print the ticket type
            bill += 7
            print("Child ticket: $7")
        elif age <= 18:
            # Add the youth ticket price to the bill and print the ticket type
            bill += 12
            print("Youth ticket: $12")
        else:
            # Add the adult ticket price to the bill and print the ticket type
            bill += 20
            print("Adult ticket: $20")
    else: 
        print("Too short to ride.")
# Output the final bill
print(f"Total bill: ${bill}")
             
             
        