# 1. Creëer een rekenmachine functie genaamd calculator() die 2 parameters heeft genaamd a en b.

def read_number():
    attempt = 0
    while True:
        user_pin = input("Enter a number: ")
        input_only_digits = user_pin.isdigit()
        print("Is input only digits: " + str(input_only_digits))
        
        if input_only_digits:
            return int(user_pin)
        else :
            print("Invalid input, try again..")
            attempt += 1
            if attempt == 10:
                print("You have exceeded the maximum number of attempts, please try again later..")
                break


def calculator(a, b):
    
    # 1.2. Sum van a en b
    print( calc_sum(a, b) )
    
    # 1.3. Subs van a en b
    print( calc_min(a, b) )
    
    # 1.4. Mul van a en b
    print( calc_mul(a, b) )
    
    # 1.5. Div van a en b
    print( calc_div(a, b) )
    
    # 1.6. FloDiv van a en b
    print( calc_flodiv(a, b) )
    
    # 1.7. Perc van a en b
    print( calc_perc(a, b) )

def calc_sum(a, b):
    return (a + b)

def calc_min(a, b):
    return (a - b)

def calc_mul(a, b):
    return (a * b)

def calc_div(a, b):
    return (a / b)

def calc_flodiv(a, b):
    return (a // b)

def calc_perc(a, b):
    return calc_mul( calc_div(a, b), 100) 
    
print( "Percentage is: ", calc_perc(10, 50))
print( "Percentage is: ", calc_perc(5, 8))

# 1.1. Lees de gebruikersinvoer (user-input)
a = read_number()
b = read_number()

calculator(a, b)