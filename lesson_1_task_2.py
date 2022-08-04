print('Enter number of seconds (0 < seconds < 86 400): ',end='')
number = int(input())

if int(number // 3600) <= 9:
    hours = str('0' + str(int(number // 3600)))
else:
    hours = str(int(number // 3600))

if int((number - 3600 * (number // 3600)) // 60) <= 9:
    minutes = str('0' + str(int((number - 3600 * (number // 3600)) // 60)))
else:
    minutes = str(int((number - 3600 * (number // 3600)) // 60))

if int(number % 60) <= 9:
    seconds = str('0' + str(int(number % 60)))
else:
    seconds = str(int(number % 60))

print(f"\n{hours}:{minutes}:{seconds}")
