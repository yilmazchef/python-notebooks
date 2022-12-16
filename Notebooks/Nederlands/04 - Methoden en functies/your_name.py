def print_your_name(first_name, last_name):
    print("----------------------------------")
    print(first_name + " " + last_name)
    print("----------------------------------")
    
print(type(print_your_name))

x = 10

print_your_name("Elon", "Musk")

print_your_name("Nikola", "Tesla")

def calc_sum(a, b):
    return a + b

first = calc_sum(10, 5)

second = calc_sum(20,10)

print ( first == second  )


def design_a_car(color, company, model, price):
    # ...
    # ...
        # ...
            # ...
                # ...
                    # ...
                # ...
        # ...
    # ...
    return "Color " + color + "," + " company " + company + "," \
                "model " + model + "," + "price " + price + "."
                
                
car1 = design_a_car("Gray", "Tesla", "X", 50000)
# gdyjvgsdhv8dfgr -> memory address demo

car2 = design_a_car("Red", "Renault", "Megane", 18000)
# bg7df6vıf78ob87g -> memory address demo

