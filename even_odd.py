def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    result = check_even_odd(num)
    print(f"{num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
