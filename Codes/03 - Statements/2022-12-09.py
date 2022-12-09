# OP01: druk alle numbers van 1 t.e.m 1000 af (gebruik een for loop)

for number in range(1, 1001):
    print(number)
    

# OP02: druk alle even numbers van 1 t.e.m 1000 af (gebruik een for loop)
# is_even = (x % 2 == 0)

for number in range(1, 1001):
    # stap01 -> number = 1
    # stap02 -> number = 2
    # stap03 -> number = 3 ...
    if(number % 2 == 0):
        print(number)
        

# OP03: druk alle oneven numbers van 1 t.e.m 1000 af (gebruik een for loop)
for number in range(1, 1001):
    # stap01 -> number = 1
    # stap02 -> number = 2
    # stap03 -> number = 3 ...
    if(number % 2 != 0):
        print(number)
        
# OP04: druk alle karakters op een nieuwe lijn van een string af (gebruik een for loop)
# s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

quote = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

for ch in quote:
    print(ch)
    

## OP05: druk alle karakters in hoofdletter op een nieuwe lijn van een string af (gebruik hier een for loop)
## s = "Hello world!"

s = "Hello world!"
print(s.upper())

## OP05: druk alle karakters in kleineletter op een nieuwe lijn van een string af (gebruik hier een for loop)
## s = "HELLo VEnUs!"

s = "HELLo VEnUs!"
print(s.lower())

## 06: lees de user-invoer (input) dan print als ne voornaam en familienamen matchen met "John", "Doe"
## input -> "Yilmaz", "Doe"
## actual -> "John", "Doe" 

first_name = input("First name: ")
last_name = input("Last name: ")

print( "You name is {0} {1}".format(first_name, last_name) )

# case insensitive value check
is_user_john_doe = (first_name.lower() == "John".lower() and last_name.lower() == "Doe".lower())

# John            |
# Doe      |
# John Doe != John       Doe      

print(len(first_name))
print(len(last_name))

first_name = first_name.replace(" ", "")
last_name = last_name.replace(" ", "")

print(len(first_name))
print(len(last_name))

# deze evaluatie is case insensitive en trimmed (spaties zijn verwijdert)
is_user_john_doe = (first_name.lower().replace(" ", "") == "John".lower() 
                    and last_name.lower().replace(" ", "") == "Doe".lower())

print("Are you John Doe? -> {0}".format(is_user_john_doe))

# OP06: Valideer een email (geen spatie, geen case sensitiviteit)

email = input("Please enter your email: ")

email = email.lower().replace(" ", "")

print("Your email is: {0}".format(email))


