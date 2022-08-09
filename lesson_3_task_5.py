"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 

Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 

Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def processing_new_string():
    """
    There are three correct types of input data:

    1) # - end of work of program
    2) 1 2 3 4... - only numbers
    3) 1 2 3 4 # ... - last string for program

    """
    cancel_of_work = '#'
    global current_sum
    local_sum = 0
    new_string = input('Enter new string: ').split()
    print(new_string)

    # case with '#'
    if new_string == cancel_of_work:
        print('\nEnd of program!')
        return False

    # case with only numbers
    if new_string[len(new_string) - 1] != cancel_of_work:
        try:
            for i in range(len(new_string)):
                local_sum += int(new_string[i])
        except:
            print('\nYou have typed invalid format of data string!')
            print(f'\nCarrent sum: {current_sum}\n')
            return True

        current_sum = current_sum + local_sum
        print(f'\nCarrent sum: {current_sum}\n')
        return True

    # case: numbers with special symbol
    else:
        try:
            for i in range(len(new_string) - 1):
                local_sum += int(new_string[i])
        except:
            print('\nYou have typed invalid format of data string!')
            print(f'\nCarrent sum: {current_sum}\n')
            return True

        current_sum = current_sum + local_sum
        print(f'\nCarrent sum: {current_sum}')
        print('\nEnd of program!')
        return False


start_work = True
current_sum = 0

while start_work == True:
    start_work = processing_new_string()



