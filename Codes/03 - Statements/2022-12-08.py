# number = int(input("Enter a number: "))
# print("The number you entered is: " + str(number))

# number = int(input("Enter a number: "))
# print("The number you entered is: " + str(number))

# number = int(input("Enter a number: "))
# print("The number you entered is: " + str(number))

# number = int(input("Enter a number: "))
# print("The number you entered is: " + str(number))

# number = int(input("Enter a number: "))
# print("The number you entered is: " + str(number))

# print(
#     int(input("Enter a number: ")) * 5
# )

# print("hello" in "hello world")

# print(1 not in [1, 2, 3])

# searched_value in list

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for dynamic_value in list:
# for number in number_list:
#     # stap 01: print(1)
#     # stap 02: print(2)
#     # stap 03: print(3)
#     # stap 04: print(4)
#     # ...
#     # stap 10: print(10)
#     print(number)


# student_list = ["John", "Jane", "Jack", "Jill", "Mary", "Mark"]

# for student in student_list:
#     print(student)
    
# numbers = list(range(1, 50)) 

# for number in numbers:
#     if(number != 20):
#         print(number)
#     else:
#         print("************************")
        

# print( "a" in "apple")
# print("crazy" in "apple iphone")

# for ch in "apple":
#     print(ch)
    
# offensive_sentence = "I hate you, you are a stupid person!"
# word_list = offensive_sentence.split()

# print("I ****** you, you are a ******* person!")

# print("I", " am", " the", "legend", sep = "_")

# for word in word_list:
#     if( word == "hate" or word == "stupid" ):
#         print("******", end = " ")
#     else:
#         print(word, end = " ")


# print("Hello World", end = "!!!")

# OP01 :
# maak een lijst van getallen tussen 0 en t.e.m 1000
# druk alleen even getallen af.

# x mod 2 is gelijk aan 0 (zero) dan is de getal 'even



# mylist = list(range(0, 10))

# for n in mylist:
#     print(n)
    
# for letter in "Aliexpress, Amazon, Paypal...":
#     if letter == 'a':
#         print(letter)
        
    
for word in "Aliexpress, Amazon, Paypal..., Tesla".split():
    for ch in word:
        if(ch == ','):
            print(" ", end = '')
        elif(ch == '.'):
            continue
        else:
            print(ch, end='')
            
# replace text in python

s = "Aliexpress, Amazon, Paypal..., Tesla"
slist = s.split()

# replace the word 'Aliexpress' with 'Alien'
slist[0] = 'Alien'

# replace each ',' with ' ' using advanced for loop



