print('Enter value of proceeds: ',end='')
the_proceeds = int(input())

print('Enter value of expense: ',end='')
the_expense = int(input())

if the_expense > the_proceeds:
    print('\nWe have more expenses!')
elif the_expense == the_proceeds:
    print('\nProceeds and expenses are equivalent!')
else:
    print('\nProceeds more than expenses!')
    print(f'\nIncome: {(the_proceeds - the_expense) / the_proceeds:.2f}',)
    print('\nEnter number of employees: ',end='')
    the_employees = int(input())
    print(f'\nProfit per employee: {(the_proceeds - the_expense) / the_employees:.2f}')
