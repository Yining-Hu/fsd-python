import random

def generate_random_numbers(n):
    return [random.randint(0, 10) for _ in range(n)]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorials(numbers):
    factorial_array = []
    for num in numbers:
        factorial_array.append(factorial(num))
    return factorial_array

def show_arrays(random_numbers, factorial_numbers):
    print("Array of random numbers:", random_numbers)
    print("Array of factorials:", factorial_numbers)

def main():
    # Generate 5 random numbers
    random_numbers = generate_random_numbers(5)

    # Calculate factorials of each random number
    factorial_numbers = factorials(random_numbers)

    # Show the arrays of random numbers and factorials
    show_arrays(random_numbers, factorial_numbers)

if __name__ == "__main__":
    main()