# Program to calculate the sum of squares of first X natural numbers

# Take input
x = int(input("Enter a positive integer: "))

# Calculate
if x < 1:
    print("Invalid input. Please enter a positive integer.")
else:
    total = 0
    for i in range(1, x + 1):
        total += i ** 2

    # Show output
    print(f"The sum of the squares of the first {x} natural numbers is: {total}")

