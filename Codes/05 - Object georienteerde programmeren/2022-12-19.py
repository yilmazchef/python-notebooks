# students = [ "Nikola", "Einstein", "Newton", "Marie", "Charlie", "Darwin" ]
# ids = [ 1, 2, 3, 4, 5, 6 ]
# courses = [ "Python", "Java", "C++", "C#", "PHP", "JavaScript" ]
# grades = [ 80, 70, 60, 50, 88, 59 ]

# school_zip = list(zip(ids, students, courses, grades))

# school_list = [ids, students, courses, grades]
# school_list list(dataype moet een set, tuple, list of dictionary zijn)

# 2de manier om een list te maken
# school_list = list()
# school_list.append(ids)
# school_list.append(students)
# school_list.append(courses)
# school_list.append(grades)

# print( school_zip )

# print("-" * 50)

# print( school_list )

# print(school_zip[0])

# school_dict = dict()
# school_dict["students"] = list(zip(ids, students, courses, grades))

# print(school_dict)

# OOP (Object georienteerde programmeren)

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 9)
dog2 = Dog("Spike", 8)
dog3 = Dog("Bella", 6)

# print("Dog 1: ", dog1.name, ", ", dog1.age)
# print("Dog 2: ", dog2.name, ", ", dog2.age)
# print("Dog 3: ", dog3.name, ", ", dog3.age)

print("-" * 50)

dogs = [dog1, dog2, dog3]

for dog in dogs:
    print(dog.name, ", ", dog.age)


# maak een class voor een student

# names = [ "Nikola", "Einstein", "Newton", "Marie", "Charlie", "Darwin" ]
# ids = [ 1, 2, 3, 4, 5, 6 ]
# courses = [ "Python", "Java", "C++", "C#", "PHP", "JavaScript" ]
# grades = [ 80, 70, 60, 50, 88, 59 ]

class Student():
    pass

