print('Enter value of A: ',  end='')
a = int(input())

print('Enter value of B: ', end='')
b = int(input())

the_day = 1

while a < b:
    a = a * 1.1
    the_day = the_day + 1

print(f'\nDay number {the_day}')
