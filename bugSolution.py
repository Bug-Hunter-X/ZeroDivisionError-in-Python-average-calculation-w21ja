def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers) 
print(f"Average: {average}") # Output: Average: 0

my_numbers = [10,20,30]
average = calculate_average(my_numbers)
print(f"Average: {average}") # Output: Average: 20.0