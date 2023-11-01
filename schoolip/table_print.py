# Program to print tables of any input number

# Take input
num = float(input("Which number's table do you want to know?: "))
times = int(input("How many table multiplications do you want to print?: "))

for i in range(times):
    print(f'{num} x {i + 1} = {num * (i + 1)}')
