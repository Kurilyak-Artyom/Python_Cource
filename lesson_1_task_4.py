print('Enter integer number: ',end='')
n = int(input())
max_digit = 0

while n > 0:
    if n % 10 > max_digit:
        max_digit = n % 10
    n = n // 10

print(max_digit)
