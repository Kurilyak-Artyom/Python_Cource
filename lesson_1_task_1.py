print('Enter first integer digit: ',end='')
a1 = int(input())

print('Enter second integer digit: ',end='')
a2 = int(input())

print('Type of a1 is ', type(a1))

a1 = 5
print('ID of 5: ',id(5))
print('ID of a1: ',id(a1))

print('Enter first string: ',end='')
string1 = input()

print('Enter second string: ',end='')
string2 = input()

if string1 > string2:
    print(string1,'>',string2)
elif string1 < string2:
    print(string1,'<',string2)
else:
    print(string1,'=',string2)

print('length of first string is',len(string1))
print('length of second string is',len(string2))

