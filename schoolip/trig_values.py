# Program to calculate several values of a triangle 

p = float(input("Enter the perpendicular length of triangle: "))
b = float(input("Enter the base length of triangle: "))
h = float(input("Enter the hypotenuse of triangle: "))

if (p <= 0) or (h <= 0) or (b <= 0):
    output = "Invalid Input."
else:
    # Calculate values
    peri = p + b + h
    half_p = (p + b + h) / 2 # Half perimeter for area
    area = ((half_p) * (half_p - p) * (half_p - b) * (half_p - h)) ** 0.5 # Area

    if area == 0.0:
        output = "Invalid triangle measurements."
    else:
        output = f"""
Mathematical values of this triangle are:

Area = {round(area, 2)} square-unit
Perimeter = {peri} unit

Trigonometric Values of this triangle are:

Sin = {p}/{h} = {p/h}
Cos = {b}/{h} = {b/h}
Tan = {p}/{b} = {p/b}
Cosec = {h}/{p} = {h/p}
Sec = {h}/{b} = {h/b}
Cot = {b}/{p} = {b/p}
"""
        
print(output)