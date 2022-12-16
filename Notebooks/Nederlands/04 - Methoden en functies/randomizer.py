# random examples

import random

help(random.randint)

number = random.randint(10, 100)

print(number)

help(random.choice)

students = [ "John", "Mary", "William", "Nick", "Zoe" ]

random_student = random.choice(students)

print(random_student)

import statistics

help(statistics.median)


import calendar

help(calendar.isleap)


print(calendar.isleap(2022))

print(calendar.isleap(2024))

print(calendar.isleap(2020))


help(calendar.month)

print(calendar.month(2022, 3, 10, 2) )

print(calendar.day_name)