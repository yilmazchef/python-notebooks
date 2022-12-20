# Opdrachten OOP met oplossingen

Programma Uitleg:

1. Er wordt een klasse met de naam Calculator gemaakt en de methode __init__() wordt gebruikt om de waarden van die klasse te initialiseren.
2. Methoden voor het optellen, aftrekken, vermenigvuldigen, delen van twee getallen en het retourneren van hun respectievelijke resultaten zijn gedefinieerd.
3. Het menu wordt afgedrukt en de keuze wordt gemaakt door de gebruiker.
4. Er wordt een object voor de klasse gemaakt met de twee nummers van de gebruiker die als parameters worden doorgegeven.
5. Met behulp van het object wordt de respectieve methode aangeroepen volgens de keuze van de gebruiker.
6. Als de keuze 0 is, wordt de lus afgesloten.
7. Het eindresultaat wordt afgedrukt.


```python
class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Calculator(a, b)

choice = 1

while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice=int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(),2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
 
print()
```

    0. Exit
    1. Add
    2. Subtraction
    3. Multiplication
    4. Division
    Result:  6
    0. Exit
    1. Add
    2. Subtraction
    3. Multiplication
    4. Division
    Result:  8
    0. Exit
    1. Add
    2. Subtraction
    3. Multiplication
    4. Division
    Exiting!
    
    

Runtime scenarios om te testen

```
 
Case 1:
Enter first number: 2
Enter second number: 4
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 1
Result:  6
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 3
Result:  8
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 0
Exiting!
 
Case 2:
Enter first number: 150
Enter second number: 50
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 2
Result:  100
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 4
Result:  3.0
0. Exit
1. Add
2. Subtraction
3. Multiplication
4. Division
Enter choice: 0
Exiting!

```
