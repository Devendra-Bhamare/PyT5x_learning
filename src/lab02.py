# Taking a list of numbers as input
numbers = input("Enter numbers separated by spaces: ")

# Converting the input string into a list of integers
num_list = list(map(int, numbers.split()))

# Calculating the sum and average
total = sum(num_list)
average = total / len(num_list) if num_list else 0

# Displaying results
print("\nYou entered:", num_list)
print("Sum of numbers:", total)
print("Average of numbers:", round(average, 2))
