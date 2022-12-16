balance = 1000
logs = dict()

# if user enters 1234, then he is allowed to withdraw money
# else he is not allowed to withdraw money then the application stops working
def read_pin_code():
    attempt = 0
    # 1. herhaling -> attempt = 0
    while True:
        # 1. 4444 -> 2. 1234 -> 3. 1234
        user_pin = input("Enter your PIN: ")
        input_only_digits = user_pin.isdigit()
        input_has_4_digits = len(user_pin) == 4
        print("Is input only digits: " + str(input_only_digits))
        print("Has the input only 4 digits: " + str(input_has_4_digits))
        
        if input_only_digits and input_has_4_digits:
            return int(user_pin)
        else :
            print("Invalid input, try again..")
            attempt += 1
            if attempt == 3:
                print("You have exceeded the maximum number of attempts, please try again later..")
                break
        
def check_pin_code(pin_code):
    print("Checking your PIN.. {}".format(pin_code))
    if pin_code == 1234:
        print("Pin code is correct, you are allowed to withdraw money..")
        return True
    else:
        print("Pin code is incorrect, you are not allowed to withdraw money..")
        return False
    
def read_amount():
    while True:
        req_amount = input("Enter the amount you want to withdraw: ")
        if type(req_amount) == int and req_amount.isdigit() \
            and int(req_amount) > 0 and int(req_amount) <= 1000000:
            return int(req_amount)
        else:
            print("Invalid amount, try again..")
            

def check_amount(req_amount):
    if req_amount > balance:
        print("Insufficient balance, try again later, or ask your best friend for a loan..")
        return False
    
    elif req_amount < 0:
        print("Invalid amount, try again..")
        return False
    
    elif req_amount > 0 and req_amount < 5:
        print("Minimum amount is 5, try again..")
        return False
    
    else:
        return True

def update_balance(req_amount):
    balance = balance - req_amount
    print("Your new balance is: " + str(balance))

def withdraw(req_amount):
    if(check_amount(req_amount)):
        update_balance(req_amount)
        
# test de code
def atm():
    
    print("Welcome to our ATM..")
    
    print("Reading your PIN..")
    pin_code = read_pin_code() # werkt goed..
    print("Checking your PIN..")
    if(check_pin_code(pin_code)):
        print("Reading the amount you want to withdraw..")
        req_amount = read_amount()
        print("Checking the amount you want to withdraw..")
        withdraw(req_amount)
        print("Updating your balance..")
    else:
        print("Come back soon.. When you get your salary..")
        
    print("Thank you for using our ATM, have a nice day..")
    


atm()