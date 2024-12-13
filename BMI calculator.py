#my bmi calculator 
# Greet the user with the program's purpose
print("This is your handy dandy bmi calculator ")
# Ask for user's height and store it
height = input("What is your height in m? ")
# Ask for user's weight and store it
weight = input("What is your weight in kg? ")

# Calculate BMI using the formula: BMI = weight / height^2
BMI = int(weight) / float(height) ** 2 
# Convert the calculated BMI to an integer for simplicity
bmi_as_int = int(BMI)
# Display the calculated BMI to the user
print(f"{bmi_as_int} is your bmi. ")