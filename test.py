# !/usr/bin/python
#  -*- coding: utf-8 -*-

#  FizzBuzz
#  try:
#      num = int(input('Enter any number: '))

#      if num % 3 == 0 and num % 5 == 0:
#          print("FizzBuzz")
#      elif num % 3 == 0:
#          print("Fizz")
#      elif num % 5 == 0:
#          print("Buzz")
#      else:
#          print(num)
#  except ValueError:
#      print("Please enter a valid integer.")


#  CORRECT TEST:
#  def format_string(string, length):
#      if len(string) >= length:
#          return string
#      spaces = (length - len(string)) // 2
#      return " " * spaces + string


#  result = format_string(string="abaa", length=15)
#  print(f"|{result}|")

#  CORRECT VERSION 1:
"""def format_string(string: str, length: float) -> int:
    length_of_string = len(string)

    if length_of_string >= length:
        return string

    padding_t = length - length_of_string
    padding_l = padding_t // 2
    padding_r = padding_t - padding_l

    formatted_string = " " * padding_l + string + " " * padding_r
    return formatted_string


result = format_string(string="abaa", length=15)
print(f"|{result}|")
"""

"""point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")
"""


#  def get_fullname(first_name, last_name, middle_name=""):
#      if middle_name:
#          full_name = f"{first_name} {middle_name} {last_name}"

#      else:
#          full_name = f"{first_name} {last_name}"
#      return full_name


#  print(get_fullname("Erich", "Remark", "Maria"))
#  print(get_fullname("Tom", "Walker"))


"""def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"
    return full_name


print(get_fullname("Erich", "Remark", "Maria"))
print(get_fullname("Tom", "Walker"))"""


# Задаємо конкретне число
#  num = int(input())

#   Перевіряємо кратність
#  if num % 3 == 0 and num % 5 == 0:
#      print("FizzBuzz")
#  elif num % 3 == 0:
#      print("Fizz")
#  elif num % 5 == 0:
#      print("Buzz")
#  else:
#      print(num)

#  work_experience = int(input("Enter your full work experience in years: "))

#  if work_experience > 5:
#      developer_type = "Senior"
#  elif work_experience > 1:
#      developer_type = "Middle"
#  else:
#      developer_type = "Junior"

#  print(
#      f"Your work experience is {work_experience} full year(s), and your developer type is {developer_type} now."
#  )

#  money = 0
#  if money:
#      print(f"You have {money} on your bank account")
#  else:
#      print("You have no money and no debts")

#  s1 = 'Hello'
#  s2 = 'world!'
#  joined_string = f"{s1} {s2}"   Hello world!

# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(2)
# print(count_2)   Виведе 4, оскільки число 2 зустрічається 4 рази

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))

# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort()
# print(nums)   Виведе [1, 1, 2, 3, 4, 5, 9]

# nums.sort(reverse=True)
# print(nums)   Виведе [9, 5, 4, 3, 2, 1, 1]

# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)   Виведе ['apple', 'banana', 'cherry']

# nums = [3, 1, 4, 1, 5, 9, 2]
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)   Виведе [1, 1, 2, 3, 4, 5, 9]

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# my_dict.pop("age")
# city = my_dict.get("city")
# print(city)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))   {3}
# print(a & b)   {3}

# a = {1, 2, 3}
# b = {3, 4, 5}
#  print(a.symmetric_difference(b))   {1, 2, 4, 5}
# print(a ^ b)
# print(a | b)
# print(a - b)
# print(a & b)

# s = "hello"
# print(s.upper())   Виведе 'HELLO'
# print(s.capitalize())

#  Просте форматування рядка
# name = "John"
# print("Hello, {}!".format(name))

#  Форматування з декількома аргументами
# age = 25
# print("Hello, {}. You are {} years old.".format(name, age))

#  Використання іменованих аргументів
# print("Hello, {name}. You are {age} years old.".format(name="Jane", age=30))

#  Використання індексів для вказівки порядку аргументів
# print("Hello, {1}. You are {0} years old.".format(age, name))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# three_numbers = my_list[2::3]

# print(my_list[::-1])   Output: [5, 4, 3, 2, 1, 0]
# print(my_list[::-2])
# print(three_numbers)

#  length = float(input('Enter the room length (in meters): '))
#  width = float(input('Enter the room width (in meters): '))
#  area = length * width
#  print(f"The room area is: {area} sq. meters.")

# my_list = []
# my_list.insert(0, 2024)
# my_list.insert(1, "Python")
# my_list.insert(2, 3.12)
#  my_list = [2024, 'Python', 3.12]

# my_list = [2024, 3.12]
# some_data = ["Python"]
# my_list.extend(some_data)
# my_list.insert(1, "Python")
# my_list.reverse()
# print(my_list)

# data = {"year": 2024, "lang": "Python", "version": 3.12}
# print(data)

# cat = {}
# cat["nick"] = "Simon"
# cat["age"] = 7
# cat["characteristics"] = ["gentle", "bytes"]

# age = cat.get("age")

# info = {"status": "vaccinated", "breed": True}
# cat.update(info)

# print(cat)
# print(f"The cat's age is: {age}")

# x = int(input("Введіть число: "))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# a = input("Введіть число: ")
# a = int(a)
# if a > 0:
#     print("Число додатне")
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print("Це число - нуль")

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False

# if is_next:
#     print("Test passed")
# else:
#     print("Test failed")

# rate = 4.32
# night_rate = rate / 2
# value_day = 164
# value_night = 60
# payment = (rate * value_day) + (night_rate * value_night)
# print(f"Total electricity cost: {payment} EUR")

# first_name = "Tom"
# last_name = "Walker"
# print(f"Name: {first_name}, Surname: {last_name}")

# first_name = "Tom"
# last_name = "Walker"
# full_name = first_name + " " + last_name
# print(full_name)

# length = 2.75
# width = 1.75
# area = length * width
# show = (
#     f"With width {width} and length {length} of the room, its area is equal to {area}"
# )
# print(show)

# length = float(input("Enter the room length (in meters): "))
# width = float(input("Enter the room width (in meters): "))
# area = length * width
# print(f"The room area is: {area} sq. meters.")

# length = "2.75"
# width = "1.75"
# area = float(length) * float(width)
# show = (
#     f"With width {width} and length {length} of the room, its area is equal to {area}"
# )
# print(show)

# is_active = True
# is_delete = False

# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = bool(input("Would you like to receive notifications? (Y/N): "))

# name = "Tom Walker"
# age = 20
# is_active = True
# subscription = None
# show = f"User {name} age {age} has an active account, subscription: {subscription}"
# print(show)

#  print('My first Python test')
#  print('Great it comes down so easy to console')
#  name = "Python"
#  print("Hello  "+name)
#  age = 20
#  age += 2
#  print(age)
#  print("your age is "+str(age))

#  human = False
#  print(human)

#  a = input("Рядок запрошення: ")
#  На екрані ви побачите: Рядок запрошення:

#  age = input("How old are you? ")
#  age = int(age)

#  pi_str = str(3.14)
#  age_str = str(29)

#  Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

#  Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

#  Обчислення загальної вартості
# total_cost = (
#     num_croissants * price_per_croissant
#     + num_glasses * price_per_glass
#     + num_coffee_packs * price_per_coffee_pack
# )

#  Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

#  Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")


"""
Напишіть функцію format_string, яка центрує рядок у рамках заданої довжини length.

Задачі:

Створіть функцію format_string, яка приймає два аргументи: string рядок, який потрібно форматувати та length довжина, у межах якої потрібно центрувати рядок.
Якщо довжина string більша або дорівнює length, поверніть рядок без змін.
Якщо довжина string менша за length, додайте перед рядком пробіли, для того, щоб рядок був центрований у рамках length. Кількість пробілів визначте за формулою (length - len(string)) // 2.
Поверніть з функції відформатований рядок, що центрується у межах length.
Очікуваний результат:

Функція format_string повертає відформатований рядок відповідно до заданих правил.

Підказки:

Використовуйте len() для визначення довжини рядка.
Для створення рядка з пробілів використовуйте " " * кількість_пробілів.
"""


# def format_string(string: str, length: int) -> str:
#      Get the length of the input string
#     length_of_string = len(string)

#      If the string is longer than or equal to the specified length, return it unchanged
#     if length <= length_of_string:
#         return string

#      Calculate the number of spaces needed for padding
#     padding = length - length_of_string
#     padding_left = padding // 2
#     padding_right = padding - padding_left

#      Create the formatted string with the calculated padding
#     formatted_string = " " * padding_left + string + " " * padding_right
#     return formatted_string


#  Example usage
# result1 = format_string("Hello world!", 40)
# result2 = format_string("abaa", 15)

# print(f"|{result1}|")   Centered within 40 characters
# print(f"|{result2}|")   Centered within 15 characters

"""* Функція first: 
    * size є обов'язковим аргументом.
    * *args дозволяє функції приймати будь-яку кількість додаткових позиційних аргументів. len(args) дає кількість цих аргументів.
* Функція second:
    * size є обов'язковим аргументом.
    * **kwargs дозволяє функції приймати будь-яку кількість додаткових ключових аргументів. len(kwargs) дає кількість цих аргументів.

Таким чином, обидві функції повертають суму size плюс кількість додаткових аргументів, які були передані.

def first(size, *args):
    return size + len(args)


print(first(5, "first", "second", "third"))   Результат: 8
print(first(1, "Alex", "Boris"))   Результат: 3


def second(size, **kwargs):
    return size + len(kwargs)


print(
    second(3, comment_one="first", comment_two="second", comment_third="third")
)   Результат: 6
print(second(10, comment_one="Alex", comment_two="Boris"))   Результат: 12
"""

#  def factorial(n):
#      print("Виклик функції factorial з n = ", n)
#      if n == 1:
#          print("Базовий випадок, n = 1, повернення 1")
#          return 1
#      else:
#          result = n * factorial(n - 1)
#          print("Повернення результату для n = ", n, ": ", result)
#          return result


#  print(factorial(5))

"""Рекурсія: Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Задачі:

Створіть функцію number_of_groups, яка приймає два аргументи: n - загальна кількість людей та k - кількість переможців.
У функції number_of_groups, використовуйте функцію factorial для обчислення факторіалів відповідно до формули сполучень: Cnk = n! / ((n - k)! · k!).
Обчислення здійснюється шляхом виклику функції factorial для отримання факторіалів n, n - k та k.
Поверніть результат цього обчислення.
Очікуваний результат:

Функція number_of_groups повертає кількість можливих різних списків переможців.

Зверніть увагу на те, які великі значення ми отримуємо для факторіала. Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.

Пояснення:
Функція factorial:
Це рекурсивна функція, яка обчислює факторіал числа n.
Базові випадки: факторіал 0 і 1 дорівнює 1.
Функція number_of_groups:
Використовує формулу сполучень без повторень для обчислення кількості можливих комбінацій.
numerator - це факторіал загальної кількості людей (n!).
denominator - це добуток факторіалів від кількості людей без переможців ((n - k)!) і кількості переможців (k!).
Використовуємо ціле ділення (//) для обчислення, оскільки ми працюємо з великими числами, де точне розділення може давати неточні результати через обмеження точності float в Python.

Зверніть увагу, що для дуже великих чисел, як у випадку з 50!, навіть 64-бітові цілі числа можуть бути недостатніми, тому результати можуть бути не точними через обмеження в обчислювальних ресурсах. Для більш точних обчислень з великими числами можна використовувати бібліотеки як decimal або sympy в Python, що дозволяють працювати з числами дуже великої точності.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
     Формула: C(n,k) = n! / ((n - k)! * k!)
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    return numerator // denominator


print(number_of_groups(50, 7))
"""

"""HW-03 TASK-01
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
Вимоги до завдання:
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.
Рекомендації для виконання:
Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.
Критерії оцінювання:
Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.
Приклад:
Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути −157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року
"""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            greeting_date = birthday_this_year

            if greeting_date.weekday() == 5:  # Sat
                greeting_date += timedelta(days=2)
            elif greeting_date.weekday() == 6:  # Sun
                greeting_date += timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "greeting_date": greeting_date.strftime("%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Sarah Thomas", "birthday": "1983.07.25"},
    {"name": "Jane Smith", "birthday": "1990.03.01"},
    {"name": "Katie Taylor", "birthday": "1987.09.09"},
    {"name": "Daniel Martinez", "birthday": "1994.02.20"},
    {"name": "Alice Johnson", "birthday": "1988.03.02"},
    {"name": "Michael Brown", "birthday": "1985.01.28"},
    {"name": "Emily Davis", "birthday": "1980.02.22"},
    {"name": "Chris Wilson", "birthday": "1995.04.12"},
    {"name": "David Anderson", "birthday": "1991.02.26"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Current week greetings list:", upcoming_birthdays)
