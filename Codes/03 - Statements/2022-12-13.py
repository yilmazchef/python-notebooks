# numbers = [1,2,3,4,5]

# numbers.append(6)

# numbers.remove(3)


# # [1, 2, 4, 5, 6]

# numbers.pop(2)

# print(numbers)

# messages = ["Hello", "World", "Python", "Programming", "Language"]

# messages.append("Java")

# print("Java is added to the list" + str(messages))

# messages.remove("World")

# print("World is removed from the list" + str(messages))

# messages.remove("CSharp")

# print("CSharp is removed from the list" + str(messages))



# names = ["John", "Jack", "Jill", "James"]


# if("Yilmaz" in names):
#     names.remove("Yilmaz")
#     print("Yilmaz is removed from the list" + str(names))
# else:
#     print("Yilmaz is NOT in the list, sorry cannot remove it :(")
    
# # update the list with new values

# names[0] = "Yilmaz"
# names[4] = "Donald"

# print(names)

# lotto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# lotto[-1] = 99
# lotto[-3] = 88
# lotto[-0] = 77

# print(lotto)

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
#          'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
#          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# append een element aan de lijst
# chars.append('A')

# verwijder een element uit de lijst
# chars.remove('a')

# verwijder een element uit de lijst op basis van index
# chars.pop(0)
# chars[0] = None

# update een element in de lijst

# x = None
# y = 5

# print(x)
# print(y)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# guessed = [None, None, None, None, None, None, None, None, None, None]

# for guessed_number in guessed:
#     print(guessed_number)
    
# message = "" # mijn vriend heeft een bericht gestuurd met een lege string
# message2 = None # mijn vriend wilt een berict sturen maar heeft nog geen bericht

# print(None)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers[0] = None

# print(numbers)

# print(len(numbers))

# numbers.pop(2)

# print(len(numbers))

# print(numbers)

# lotto = [None, None, None, None, None, None]

# import random as r

# for lotto_number in lotto:
#     # 1 -> 44
#     # 2 -> 33
#     # 3 -> 44
#     if (lotto_number not in lotto):
#         lotto_number = r.randint(1, 45)


# unknown_lotto = [None, None, None, None, None, None]
# unknown_lotto_2 = [None, None, None, None, None, None]

# unknown_lotto[0] = 5
# unknown_lotto[1] = 17
# unknown_lotto[2] = 23
# unknown_lotto[3] = 25
# unknown_lotto[4] = 33
# unknown_lotto[5] = 44

# unknown_lotto_2[0] = 5
# unknown_lotto_2[1] = 5
# unknown_lotto_2[2] = 5
# unknown_lotto_2[3] = 16
# unknown_lotto_2[4] = 17
# unknown_lotto_2[5] = 18

# print(unknown_lotto)
# print(unknown_lotto_2)

# unknown_lotto = set(unknown_lotto)
# unknown_lotto_2 = set(unknown_lotto_2)

# print(unknown_lotto)
# print(unknown_lotto_2)

import random as r

lotto = set()

while True:
    # geneer een random getal tussen 1 en 45
    
    random_number = r.randint(1, 45)
    print("The random number is: " + str(random_number))
    print("The length of the set is: " + str(len(lotto)))
    if random_number not in lotto:
        lotto.add(random_number)
    if(len(lotto) == 6):
        break

print(sorted(lotto))

t = (2,3,4,1)

print(sorted(t))

