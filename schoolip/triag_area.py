# Program to calculate area of a triangle using both Heron's formula and Base/Height formula

# Take input
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

# Calculate and output area
area = (base * height) / 2
print(f"\nArea of this triangle is: {str(area)} square-unit")
