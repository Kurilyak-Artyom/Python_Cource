"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.
"""

def user_data(**kwargs):
    return f"\nUser first name: {kwargs['arg1']}\n\nUser second name: {kwargs['arg2']}\n\nUser birthday: {kwargs['arg3']}\n\nUser city: {kwargs['arg4']}\n\nUser email: {kwargs['arg5']}\n\nUser telephon number: {kwargs['arg6']}"


user_first_name = input('Enter first name of User: ')
user_second_name = input('Enter second name of User: ')
user_birth_date = input('Enter birthday of User in DD:MM:YYYY format: ')
user_city = input('Enter city of User: ')
user_email = input('Enter email of User: ')
user_telephon = input('Enter telephon number of User: ')

print(user_data(arg1=user_first_name, arg2=user_second_name, arg3=user_birth_date, arg4=user_city, arg5=user_email,
                arg6=user_telephon))

