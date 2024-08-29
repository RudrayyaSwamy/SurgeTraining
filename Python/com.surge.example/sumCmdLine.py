import sys

def sum_two_numbers(a, b):
    return a + b

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Usage: python sum_numbers.py <number1> <number2>")
        sys.exit(1)

    try:
        # Read numbers from command line arguments
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)

    # Calculate the sum
    result = sum_two_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
