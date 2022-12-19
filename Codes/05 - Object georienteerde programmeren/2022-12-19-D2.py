class Student():
    def __init__(self, id, name, course, grade):
        # de id value van de key id is gelezen door de 2de argument van de methode.
        self.id = id
        self.name = name
        self.course = course
        self.grade = grade
        
class Course():
    def __init__(self, title, department):
        self.title = title
        self.department = department

# instance_name.attribute
# instance_name.method()
# . (point) is the accessor operator

message = "Hello World"
words = message.split()

course_python = Course("Python fundamentals", "IT and Computer Science")
course_java = Course("Java fundamentals", "IT and Computer Science")

student1 = Student(1, "Nikola", course_python, 80)
student2 = Student(2, "Einstein", course_java, 88)

# student2 is de naam van de instantie
# . (punt) is de operator om de attribuut 'name' te accessen.
print(student1.name)
print(student2.name)

print(type(student1.name))
print(type(student1))
print(type(student1.grade))

# we kunnen op een klas meerdere datatypen samenvoegen.

class Car():
    def __init__(self, brand, model, engine, year, max_speed):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year
        self.max_speed = max_speed
        
    def sit_and_buckle_up(self):
        pass
    
    def insert_ignition_key(self):
        pass
    
    def change_gear(self):
        pass
    
    def twist_ignition_key(self):
        pass
    
    def shift_the_gear(self):
        pass

class Engine():
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        
engine_tesla = Engine("Tesla", "NGin", "Electrical motor")

car_tesla = Car("Tesla", "X", engine_tesla, 2022, 240)

car_tesla.sit_and_buckle_up()
car_tesla.insert_ignition_key()
car_tesla.twist_ignition_key()
car_tesla.change_gear()
car_tesla.shift_the_gear()



# class NameOfTheClass():
#    def __init__(self, attributen ..... gesplit met comma ):
#        self.attr1 = attr1
#        self.attr2 = attr2

#    def method1(self):
#       pass