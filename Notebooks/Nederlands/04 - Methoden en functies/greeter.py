def say_hello():
    print("Hello World!")

say_hello()

print_hello = say_hello

del say_hello

print_hello()

def sum_numbers(a, b):
    return a + b

print(sum_numbers(1, 2))

alternative_sum = sum_numbers

print(alternative_sum(1, 2))

afdrukken = print

afdrukken("Hello World!")