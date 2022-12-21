<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# while-lussen (loop)

De <code>while</code>-instructie in Python is een van de meest algemene manieren om iteratie uit te voeren. Een <code>while</code>-instructie zal herhaaldelijk een enkele instructie of een groep instructies uitvoeren als de voorwaarde waar is. 
De reden dat het een 'lus (loop)' wordt genoemd, is omdat de code-instructies **herhaaldelijk** worden doorlopen totdat niet langer aan de voorwaarde wordt voldaan.

Het algemene formaat van een while-lus is:

    while test:
        code statements
    else:
        final code statements

Laten we eens kijken naar een paar eenvoudige <code>while</code>-lussen in actie.


```python
x = 0

while x < 10: # voer de volgende code uit zolang de voorwaarde (conditie) True is
    print(x)
    x = x + 1

```


```python
y = 11

condition = (y > 10 and y < 20) # True
# y = 100, condition = 100 > 10 and 100 < 20 = True and False = False
# y = 0, condition = 0 > 10 and 0 < 20 = False and True = False
# y = 11, condition = 11 > 10 and 11 < 20 = True and True = True
# y = 20, condition = 20 > 10 and 20 < 20 = True and False = False

while (y > 10 and y < 20):
    print(y)
    y = y + 1
```

Merk op hoe vaak de print-statements voorkwamen (occurred) en hoe de <code>while</code>-lus doorging totdat aan de True-voorwaarde werd voldaan, wat eenmaal x==10 voorkwam. 
Het is belangrijk op te merken dat zodra dit gebeurde, de code stopte. Laten we eens kijken hoe we een <code>else</code>-statement kunnen toevoegen:


```python
# lees de user pincode tot de gebruiker de juiste pincode heeft ingevoerd maar maximaal 3 keer

correct_pincode = 1234

while True:
    user_pincode = int(input("Enter your pincode: "))
    are_they_equal = (user_pincode == correct_pincode) # True
    
    if are_they_equal:
        print("You have entered the correct pincode!")
        break
    else:
        print("Try again:")
```


```python
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')
```

# break, continue, pass

We kunnen de instructies <code>break</code>, <code>continue</code> en <code>pass</code> gebruiken in onze loops om extra functionaliteit toe te voegen voor verschillende gevallen. 
De drie statements worden gedefinieerd door:

    break: Breaks out of the current closest enclosing loop.
    continue: Goes to the top of the closest enclosing loop.
    pass: Does nothing at all.
    
    
Denkend aan <code>break</code> en <code>continue</code> statements, ziet het algemene formaat van de <code>while</code>-lus er als volgt uit:

    while test: 
        code statement
        if test: 
            break
        if test: 
            continue 
    else:

<code>break</code> en <code>continue</code> statements kunnen overal in de body van de lus verschijnen, maar we zullen ze meestal verder genest plaatsen in combinatie met een <code>if</code> statement om een actie op basis van een voorwaarde.

Laten we doorgaan en enkele voorbeelden bekijken!


```python
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue
```

Merk op hoe we een afgedrukte instructie hebben als x==3, en een wordt afgedrukt terwijl we verder gaan door de buitenste while-lus. Laten we een keer pauzeren x == 3 en kijken of het resultaat klopt:


```python
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue
```

Merk op dat het andere <code>else</code> statement niet werd bereikt en dat doorgaan nooit werd afgedrukt!

Na deze korte maar eenvoudige voorbeelden zou u zich op uw gemak moeten voelen bij het gebruik van <code>while</code>-statements in uw code.

** Een woord van waarschuwing (caution) echter! Het is mogelijk om een oneindig (infiniet) lopende lus te maken met <code>while</code> statements. Bijvoorbeeld:**


```python
# VOER DEZE CODE NIET UIT!!!! DO NOT RUN THIS CODE!!!! 
while True:
    print("I'm stuck in an infinite loop!")
```

Een korte opmerking: als je *deed* de bovenstaande cel hebt uitgevoerd, klik dan op het Kernel-menu hierboven om de kernel opnieuw te starten!


```python
while True:
    print("You have been hacked!")
```


```python
x = 11

condition = (x > 10) # 11 > 10 = True

while (x > 10): # True # alleen 1 keer gevalueerd
    print(x)
    x = x - 1
```

    11
    


```python
# lees alle characters van een string

while True:
    character = input("Would you like to continue installation? (y/n)")
    if character == "y" or character == "Y":
        # print a progress bar
        print( "Installing: [", end = "" )
        # print 100 equal signs
        for i in range(0, 100):
            print("=", end = "")
        print("]")
    elif character == "n" or character == "N":
        print("Installation stopped.")
        break
    else:
        print("Invalid input.")
        
        
# : is een slice operator
# indentatie is belangrijk
```

    Installing: [====================================================================================================]
    Installation stopped.
    
