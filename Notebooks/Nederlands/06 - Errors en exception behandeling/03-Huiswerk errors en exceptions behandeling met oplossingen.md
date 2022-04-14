<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Huiswerk: Errors en Exception behandeling

### Probleem 1
Behandel de uitzondering/exception die wordt veroorzaakt door de onderstaande code met behulp van de blokken <code>try</code> en <code>except</code>.


```python
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-c35f41ad7311> in <module>()
          1 for i in ['a','b','c']:
    ----> 2     print(i**2)
    

    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


### Probleem 2

Behandel de uitzondering die wordt veroorzaakt door de onderstaande code met behulp van de blokken <code>try</code> en <code>except</code>. Gebruik vervolgens een <code>finally</code>-blok om 'All Done' af te drukken.


```python
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-2-6f985c4c80dd> in <module>()
          2 y = 0
          3 
    ----> 4 z = x/y
    

    ZeroDivisionError: division by zero


### Probleem 3
Schrijf een functie die om een geheel getal vraagt en druk het kwadraat ervan af. Gebruik een <code>while</code>-lus met een <code>try</code>, <code>except</code>, <code>else</code>-blok om rekening te houden met onjuiste invoer.


```python
def ask():

    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break


    print('Thank you, your number squared is: ',n**2)
```

#Goed gedaan!
