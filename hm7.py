# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# b) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# c) Посчитать среднее количество лет всех людей из списка.

# people = [{"name": "John", "age": 15},
#           {"name": "John2", "age": 15},
#           {"name": "Alisa", "age": 26},
#           {"name": "Mike", "age": 37},
#           {"name": "Jack", "age": 45}]

# a)
# minAge = min(people, key=lambda x:x['age'])
# for i in range(len(people)):
#     if people[i]["age"] == minAge["age"]:
#         print(people[i]["name"])

# b)
# maxLen = max(people, key=lambda x:len(x['name']))
# for i in range(len(people)):
#     if len(people[i]["name"]) == len(maxLen["name"]):
#         print(people[i]["name"])

# c)
# ageList = []
# for i in people:
#     ageList.append(i['age'])
# print(sum(ageList)/len(ageList))

# 2. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

# def myFunc(str1, str2):
#     myList = []
#     for i in str1:
#         if str2.find(i) != -1:
#             myList.append(i)
#     return list(set(myList))
#
# print(myFunc('abcdee', 'abezzzabce'))

# 3. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

# def myFunc(str1, str2):
#     myList = []
#     for i in str1:
#         if str2.count(i) == 1 and str1.count(i) == 1:
#             myList.append(i)
#     return myList
#
# print(myFunc('abzzzbce','abcdee'))

# 4. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

# import random
# import string
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
#
# def create_email(domains, names):
#     myRandStr = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 7)))
#     e_mail = f"{random.choice(names)}.{random.randint(100, 999)}@{myRandStr}.{random.choice(domains)}"
#     return e_mail
#
# e_mail = create_email(domains, names)
# print(e_mail)
