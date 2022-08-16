"""
Сформировать  (не  программно)  текстовый  файл.  В  нём  каждая  строка  должна  описывать 
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. 
Сюда  должно  входить  и  количество  занятий.  Необязательно, чтобы для каждого предмета 
были все типы занятий. 

Сформировать  словарь,  содержащий  название  предмета  и  общее  количество  занятий  по 
нему. Вывести его на экран. 

"""

from pathlib import Path

the_path = Path(Path.cwd(), 'test_data', 'data6.txt')

f_obj = open(the_path, encoding='utf-8')

subjects_dict = {}
subject_name = ''
subject_lectures = 0
subject_practical_lessons = 0
subject_laboratory_lessons = 0

"""
При чтении названия учебной дисциплины будет учитываться тот факт, 
что название может состоять из нескольких слов. 

Например: "История России"

' '.join(line.split()[::-1][3:][::-1])[0:-1] ЧТО ЗДЕСЬ ПРОИСХОДИТ:

1) Сначала инверсия списка
2) Затем убираем первые три элемента списка, т.к. это количество предметов(лекции, практика и лабы)
3) Оставшееся название предмета обратно "разворачиваем"
4) В итоговой строке с помощью "среза" избавляемся от ":"

Аналогичными приемами извлекаем количество лекций, практический занятий и лабораторных работ из каждой строки
"""
for line in f_obj:

    # Extracting subject name
    subject_name = ' '.join(line.split()[::-1][3:][::-1])[0:-1]
    
    # Extracting subject laboratory lessons count
    try:
        subject_laboratory_lessons = int(line.split()[::-1][0][::-1][5:][::-1])
    except:
        subject_laboratory_lessons = 0
    
    # Extracting subject practical lessons count
    try:
        subject_practical_lessons = int(line.split()[::-1][1][::-1][4:][::-1])
    except:
        subject_practical_lessons = 0
    
    # Extracting subject lectures count
    try:
        subject_lectures = int(line.split()[::-1][2][::-1][3:][::-1])
    except:
        subject_lectures = 0
    
    subjects_dict.update({subject_name: subject_lectures + subject_practical_lessons + subject_laboratory_lessons})

print(subjects_dict)
f_obj.close()
