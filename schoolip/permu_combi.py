# Program to find permutations and combinations

n = int(input("Enter total number of objects (n): "))
r = int(input("Enter number of selected objects (r): "))

# Calculate factorials

if (0 <= r) and (r <= n):
    n_factorial = 1
    for i in range(1, n+1):
        n_factorial *= i

    r_factorial = 1
    for i in range(1, r+1):
        r_factorial *= i

    nr_factorial = 1
    for i in range(1, (n-r)+1):
        nr_factorial *= i

    # Calculate permutations and combinations

    permu = n_factorial / nr_factorial
    combi = n_factorial / (r_factorial * nr_factorial)

    # Show output
    print(f"Permutations: {permu}\nCombinations: {combi}")

else:
    print("Invalid inputs. Correct formula is: 0 <= r <= n")