


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_count = {}
for item in students:
    name = item['first_name']
    name_count[name] = name_count.get(name, 0)+1

for name in name_count:
    count = name_count[name]
    print(f"{name}: {count}")
print()




def name_analysis (students):  #Функция для подсчета самого частого имени в словаре
    name_count = {}

    for item in students:
        name = item['first_name']
        name_count[name] = name_count.get(name, 0) + 1

    max_freq = 0

    for name in name_count:
        count = name_count[name]
        if count > max_freq:  # Как здесь обновляются переменные? Где хранится максимальное значение?
            most_com_name = name
            max_freq = count
    return (most_com_name)



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
most_com_name = name_analysis(students)
print(f'Самое частое имя среди учеников: {most_com_name}')
print()



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
class1, class2, class3 = school_students

most_com_name1 = name_analysis(class1)
most_com_name2 = name_analysis(class2)
most_com_name3 = name_analysis(class3)
print(f'Самое частое имя в классе 1: {most_com_name1}')
print(f'Самое частое имя в классе 2: {most_com_name2}')
print(f'Самое частое имя в классе 3: {most_com_name3}')
print()




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def count_gender (school, is_male): #Функция для подсчёта по половому признаку
    results = []
    for info_about_class in school:
        class_name = info_about_class['class']
        students_list = info_about_class['students']
        boys_count = 0
        girls_count = 0

        for item in students_list:
            name = item['first_name']
            if name in is_male and is_male[name]:
                boys_count +=1
            else:
                girls_count +=1
        results.append({
            'class_name': class_name,
            'boys_count': boys_count,
            'girls_count': girls_count
        })
    return results

gender_stats = count_gender(school, is_male)
for data in gender_stats:
    print(f"Класс {data['class_name']}: девочки {data['girls_count']}, мальчики {data['boys_count']}")
print()




# Задание 5
# По информации об учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

def most_gender_finder(gender_stats_ex5):
    class_with_max_boys = None
    max_boys_count = 0

    class_with_max_girls = None
    max_girls_count = 0

    for data in gender_stats_ex5:
        if data['boys_count'] > max_boys_count:
            max_boys_count = data['boys_count']
            class_with_max_boys = data['class_name']

        elif data ['girls_count'] > max_girls_count:
            max_girls_count = data['girls_count']
            class_with_max_girls = data['class_name']

    return class_with_max_girls, class_with_max_boys



school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

gender_stats_ex5 = count_gender(school, is_male)

class_with_max_girls = most_gender_finder(gender_stats_ex5)
class_with_max_boys = most_gender_finder(gender_stats_ex5)

print(f"Больше всего мальчиков в классе {class_with_max_boys}")
print(f"Больше всего девочек в классе {class_with_max_girls}")
