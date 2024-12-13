# This is an infinite loop that will continue to run until the user decides to exit
while True:
    # Ask the user for their height and convert it to a float to ensure decimal values are accepted
    height = int(float(input("Enter your height in m (meters): ")))
    # Ask the user for their weight and convert it to a float to ensure decimal values are accepted
    weight = int(float(input("Enter your weight in kg (kilograms): ")))

    # Calculate the BMI using the formula: BMI = weight / height^2 and round the result to the nearest integer
    bmi = round(weight / height ** 2 )
    # Check the BMI and print the corresponding weight status
    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight. ")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight. ")
    elif bmi < 30:
        print(f"Your bmi is {bmi}, you are overweight. ")
    elif bmi < 35:
        print(f"Your bmi is {bmi}, you are obese. ")
    else:
        print(f"Your bmi is {bmi}, you are clinically fat. ")

    # Ask the user if they want to calculate their BMI again
    again = input("Do you want to calculate your BMI again? (yes/no): ")
    # Check if the user does not want to calculate again and exit the loop if true
    if again.lower() != "yes" or again.upper() != "YES": 
        break

# Print a farewell message after the user decides to exit
print("Thank you for using the BMI calculator. Have a great day!")
