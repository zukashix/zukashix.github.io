# Program to calculate triangle area using heron's formula

# Take input 
side1 = float(input("Enter length of 1st side: "))
side2 = float(input("Enter length of 2nd side: "))
side3 = float(input("Enter length of 3rd side: "))

# Calculate area
half_p = (side1 + side2 + side3) / 2
area = ((half_p) * (half_p - side1) * (half_p - side2) * (half_p - side3)) ** 0.5

# Show output
if area == 0:
    print('\nInvalid triangle measurements.') # Tell user if measurements are invalid
else:
    print(f"\nArea of this triangle is: {str(area)} square-unit")