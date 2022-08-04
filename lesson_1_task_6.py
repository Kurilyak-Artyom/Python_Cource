a = int(input('Enter value of A: '))
b = int(input('Enter value of B: '))

the_day = 1

while a < b:
    a = a * 1.1
    the_day = the_day + 1

print(f'\nDay number {the_day}')
