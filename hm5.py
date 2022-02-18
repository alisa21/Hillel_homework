# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# number = 10900000
# count_zeros = 0
#
# for zero in str(number):
#     if zero == '0':
#         count_zeros += 1
# print(count_zeros)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# number = 10020000000
# number = str(number)[::-1]
# count_trailing_zeros = 0
#
# for trailing_zero in number:
#     if trailing_zero == '0':
#         count_trailing_zeros += 1
#     else:
#         break
# print(count_trailing_zeros)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = [1, 'a', 3, 'l', 5, 'i']
# my_list_2 = ['s', 8, 'a', 10]
# my_result = []
# i = 0
# y = 0
#
# while i < len(my_list_1):
#     if i % 2 != 0:
#         my_result.append(my_list_1[i])
#     i += 1
# while y < len(my_list_2):
#     if y % 2 == 0:
#         my_result.append(my_list_2[y])
#     y += 1
# print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = []

for item in my_list[1::]:
    new_list.append(item)
new_list.append(my_list[0])
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4]
# my_list.append(my_list.pop(0))
# print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#
# my_str = "43 больше чем 34 но меньше чем 56"
# sum_of_numbers = 0
# print(my_str.split())
# for number in my_str.split():
#     if number.isdigit():
#         sum_of_numbers += int(number)
# print(sum_of_numbers)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
#

# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
#
# print(my_str[my_str.index('o')+1:my_str.rindex('g')])

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
#

# my_str = 'abcdefg'
# my_list = []
#
# for i in range(0, len(my_str), 2):
#     if len(my_str[i:i+2]) < 2:
#         my_list.append(my_str[i:i+2]+'_')
#     else:
#         my_list.append(my_str[i:i + 2])
# print(my_list)


# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [2,4,1,5,3,9,0,7]
# counter = 0
# for i in range(1, len(my_list)-1):
#     if my_list[i] > my_list[i-1] + my_list[i+1]:
#         counter += 1
# print(counter)
