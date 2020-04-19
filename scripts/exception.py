# Key takeaways
# * you can use an "else" statement after "except" ones to run code if no errors happen


def divide(dividend, divisor):
    return dividend / divisor


students = [
    {'name': 'Bob', 'grades': [75, 90]},
    {'name': 'Rolf', 'grades': []},
    {'name': 'Jen', 'grades': [100, 90]},
]

try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average}.')
except ZeroDivisionError as e:
    print(f'ERROR: {name} has no grades!')
else: # executed if no errors occur during try block
    print('All student averages were calculated.')
finally:
    print('End of student average calculation.')

