# Program to calculate compound interest and simple interest

# Take input
p = float(input("Enter the principle amount: "))
r = float(input("Enter rate (% per annum): "))
t = float(input("Enter time (years): "))

# Calculate simple interest
si = (p * r * t) / 100

# Calculate compound interest
ci = (p * (1 + r / 100) ** t) - p

print(f'Simple Interest: {si}\nCompound Interest: {ci}')
