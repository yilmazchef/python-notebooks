# a guess app (guess a number between 1 and 100)

correct_number = 50

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

counter = 0

while True:
    guessed_number = input("Guess a number between 1 and 100: ")
    guessed_number = int(guessed_number)
    
    counter = counter + 1
    
    if(counter >= 3):
        print("You have used all your guesses!")
        break
    else:
        if(guessed_number == correct_number):
            print("You guessed it right!")
            break # stop de while loop
        elif(guessed_number < correct_number):
            print("Your guess is too low!")
        elif(guessed_number > correct_number):
            print("Your guess is too high!")
        elif(guessed_number < 0):
            print("You cannot guess a negative number!")
            

students = ["John", "Jane", "Jack", "Jill", "Joe"]

for student in students:
    print(student)
    
while len(students) > 0:
    student = students.pop()
    print(student)


x = 10
