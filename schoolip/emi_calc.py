# Program to calculate EMI with amount, duration and interest

# Take inputs

amt = float(input('Enter product\'s full amount: '))
time = int(input("Enter duration of the EMI (in months): "))
intrst = (float(input("Enter interest in %: ").strip().replace('%', '')) / 12) / 100

# Calculate EMI amount

emi = amt * intrst * (1 + intrst) ** time / ((1 + intrst) ** time - 1)

# Show output 
print(f'Your EMI should cost you Rs. {round(emi, 2)} per month')