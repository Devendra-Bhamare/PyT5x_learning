# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favorite hobby: ")

# Processing the input
years_to_100 = 100 - age
message = f"\nHello, {name}! You are {age} years old."
message += f"\nYour favorite hobby is {hobby}."

# Adding a conditional message
if age < 100:
    message += f"\nYou will turn 100 in {years_to_100} years."
else:
    message += "\nYou have already turned 100 or are above 100 years old!"

# Printing the final output
print(message)
