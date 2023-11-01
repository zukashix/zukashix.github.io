# Program to caculate percentage in exams

# Take input and create variables
subjects = int(input('How many subjects do you have?: '))
scored_marks = 0
total_marks = 0

# Enquire marks using loop
for i in range(subjects):
    marks = str(input(f'Enter marks in subject {i + 1} in format => Scored/Max [Example: 66/70]: ')).replace(' ', '').split('/')
    scored_marks += float(marks[0])
    total_marks += float(marks[1])

# Calculate percentage and show output
percentage = (scored_marks / total_marks) * 100
print(f'Your percentage is: {round(percentage, 2)}%')
