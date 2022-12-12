# a guess app (guess a number between 1 and 100)

# correct_number = 50

# for repeat in range(1, 4): # een afstand tussen 1 t.e.m. 3
#     guessed_number = input("Guess a number between 1 and 100: ")
#     guessed_number = int(guessed_number)
#     if(guessed_number == correct_number):
#         print("You guessed it right!")
#     elif(guessed_number < correct_number): # 34 < 50
#         print("Your guess is too low!")
#     elif(guessed_number > correct_number):
#         print("Your guess is too high!")
#     elif(guessed_number < 0):
#         print("You cannot guess a negative number!")


# while True: # voer de volgende code uit zolang de voorwaarde (conditie) True is
#     guessed_number = input("Guess a number between 1 and 100: ")
#     guessed_number = int(guessed_number)
    
#     if(guessed_number == correct_number):
#         print("You guessed it right!")
#         break # stop de while loop
#     elif(guessed_number < correct_number):
#         print("Your guess is too low!")
#     elif(guessed_number > correct_number):
#         print("Your guess is too high!")
#     elif(guessed_number < 0):
#         print("You cannot guess a negative number!")
        


# lees de user input tot de gebruiker het juiste getal heeft geraden maar maximaal 3 keer

# counter = 0

# while True:
#     guessed_number = input("Guess a number between 1 and 100: ")
#     guessed_number = int(guessed_number)
    
#     counter = counter + 1
    
#     if(counter >= 3):
#         print("You have used all your guesses!")
#         break
#     else:
#         if(guessed_number == correct_number):
#             print("You guessed it right!")
#             break # stop de while loop
#         elif(guessed_number < correct_number):
#             print("Your guess is too low!")
#         elif(guessed_number > correct_number):
#             print("Your guess is too high!")
#         elif(guessed_number < 0):
#             print("You cannot guess a negative number!")
            

# students = ["John", "Jane", "Jack", "Jill", "Joe"]

# for student in students:
#     print(student)
    
# while len(students) > 0:
#     student = students.pop()
#     print(student)


# x = 10

## herhalingen

### druk alle numbers van 1 t.e.m. 10 af

# for number in range(1, 11):
#     print(number)
    
# counter = 0
# while counter < 11:
#     print(counter)
#     counter = counter + 1
    

### lees de user input tot de gebruiker het juiste getal heeft geraden

# while True: # infinite loop
#     guessed_number = int(input("Guess a number between 1 and 100: "))
    
#     if(guessed_number == 50):
#         print("You guessed it right!")
#         break # stop de while loop
#     else:
#         print("Your guess is wrong!")
        

### conditional statements

#### if

# if(True):
#     print("this code will be executed")
    
# if(False):
#     print("this code will not be executed")
    
# ### if else

# if(True):
#     print("this code from if statement will be executed")
# else:
#     print("this code from else statement will not be executed")
    
    
### if elif else (multiple conditions) conditions die meer dan 2 zijn worden meestal met if elif else geschreven

# condition1 = True
# condition2 = False
# condition3 = True
# condition4 = False

# if condition1:
#     print("condition1 is True")
# elif condition2:
#     print("condition2 is True")
# elif condition3:
#     print("condition3 is True")
# elif condition4:
#     print("condition4 is True")
# else:
#     print("no condition is True")
    

# color chooser app

# selected_color = input("Select a color (red, green, blue, yellow, cyan, magenta): ")

# if selected_color == "red":
#     print("#ff0000")
# elif selected_color == "green":
#     print("#00ff00")
# elif selected_color == "blue":
#     print("#0000ff")
# elif selected_color == "yellow":
#     print("#ffff00")
# elif selected_color == "cyan":
#     print("#00ffff")
# elif selected_color == "magenta":
#     print("#ff00ff")
# else:
#     print("Invalid color!")
    
# NA ELKE DOUBLE PUNT MOET JE EEN TAB INDENTATIE DOEN


# user_input = input("Enter a number: ")

# user_input = int(user_input)
# print(type(user_input))

# user_input_as_str = str(user_input)
# print(type(user_input_as_str))

# user_input_as_float = float(user_input)
# print(type(user_input_as_float))

student_list = ["John", "Jane", "Jack", "Jill", "Joe", "John", "Joe", "Joe"]
print(student_list) # [] is gebruikt om een list te maken

student_list_as_set = set(student_list)
print(student_list_as_set) # {} is gebruikt om een set te maken

student_list_as_tuple = tuple(student_list)
print(student_list_as_tuple) # () is gebruikt om een tuple te maken

# pseudocode voor een currency converter

# lees de user input
user_currency = input("Enter a currency (USD, EUR, GBP, JPY, AUD, CAD): ")
user_amount = input("Enter an amount: ")
user_amount = float(user_amount)

converted_amount = 0.00
converted_currency = "EUR"

# bereken de omrekening
if user_currency == "USD":
    converted_amount = user_amount * 0.85
    converted_currency = "EUR"
elif user_currency == "EUR":
    converted_amount = user_amount * 1.18
    converted_currency = "USD"
elif user_currency == "GBP":
    converted_amount = user_amount * 1.29
    converted_currency = "EUR"
else :
    print("Invalid currency!")
    

## bekende datatypen van Python
s = "Hello World" # string
i = 10 # integer
f = 10.5 # float
b = True # boolean
l = [1, 2, 3] # list
t = (1, 2, 3) # tuple
d = {"name": "John", "age": 30} # dictionary


