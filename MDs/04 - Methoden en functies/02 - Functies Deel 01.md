<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Functies

## Inleiding tot functies

Deze lezing zal bestaan ​​uit het uitleggen wat een functie is in Python en hoe je er een maakt. Functies zullen een van onze belangrijkste bouwstenen zijn wanneer we steeds grotere hoeveelheden code construeren om problemen op te lossen.

### Wat is een functie?

Formeel is een functie een handig apparaat dat een reeks instructies groepeert, zodat ze meer dan eens kunnen worden uitgevoerd. Ze kunnen ons ook parameters laten specificeren die kunnen dienen als invoer voor de functies.

Op een meer fundamenteel niveau stellen functies ons in staat om niet herhaaldelijk dezelfde code herhaaldelijk te schrijven. Als je je de lessen over strings en lijsten herinnert, onthoud dan dat we een functie len() hebben gebruikt om de lengte van een string te krijgen. Aangezien het controleren van de lengte van een reeks een veelvoorkomende taak is, zou u een functie willen schrijven die dit herhaaldelijk op commando kan doen.

Functies zullen een van de meest basale niveaus zijn van het hergebruik van code in Python, en het zal ons ook in staat stellen om te gaan nadenken over programmaontwerp (we zullen veel dieper ingaan op de ideeën van ontwerp wanneer we leren over objectgeoriënteerd programmeren).

### Waarom zelfs functies gebruiken?

Simpel gezegd, u moet functies gebruiken wanneer u van plan bent een codeblok meerdere keren te gebruiken. Met deze functie kunt u hetzelfde codeblok oproepen zonder het meerdere keren te hoeven schrijven. Dit stelt je op zijn beurt in staat om complexere Python-scripts te maken. Om dit echter echt te begrijpen, moeten we onze eigen functies schrijven!

## Topics van de functies
* def trefwoord (keyword)
* simpele voorbeeld van een functie
* het aanroepen van een functie met ()
* parameters accepteren
* print versus return
* het toevoegen van logica binnen een functie
* meerdere returns binnen een functie
* het toevoegen van lussen (for, while) binnen een functie
* tuple uitpakken
* interacties tussen de functies

### def trefwoord

Laten we eens kijken hoe we de syntaxis van een functie in Python kunnen bouwen. Het heeft de volgende vorm:


```python
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes.
    When you call help() on your function it will be printed out.
    '''
    # Voeg de statements hier toe.
    # Retourneer het gewenste resultaat
```


```python
def calculate_sum(num1, num2):
    """
    This method prints the sum of 2 given numbers.
    The data format can only be integer or float.
    """
    print( num1 + num2 )

def calculate_substraction(num1, num2):
    print(num1 - num2)
    
def calculate_multiplication(num1, num2):
    print(num1 * num2)
    
def calculate_division(num1, num2):
    print(num1 / num2)

```

    30
    20
    80
    0.05
    13.64
    


```python

# een methode aanroepen
calculate_sum(10, 20)
calculate_multiplication(4, 5)
calculate_substraction(100, 20)
calculate_division(1, 20)

calculate_sum(10.24, 3.4)

```

We beginnen met <code>def</code> en dan een **spatie** gevolgd door de naam van de functie. Probeer namen relevant te houden, bijvoorbeeld len() is een goede naam voor een lengte()-functie. Wees ook voorzichtig met namen, je zou een functie niet dezelfde naam willen aanroepen als een [ingebouwde functie in Python](https://docs.python.org/3/library/functions.html) (zoals len).

Vervolgens komen een paar haakjes met verschillende argumenten gescheiden door een **komma**. Deze argumenten zijn de invoer voor uw functie. U kunt deze invoer in uw functie gebruiken en ernaar verwijzen. Hierna zet je een dubbele punt.

Nu is hier de cruciale stap, u moet inspringen om de code in uw functie correct te beginnen. Python maakt gebruik van *whitespace* om code te ordenen. Veel andere programmeertalen doen dit niet, dus houd daar rekening mee.

Vervolgens zie je de docstring, hier schrijf je een basisbeschrijving van de functie. Met Jupyter en Jupyter Notebooks kunt u deze doc-strings lezen door op Shift+Tab te drukken na een functienaam. Doc-strings zijn niet nodig voor eenvoudige functies, maar het is een goede gewoonte om ze in te voeren, zodat u of andere mensen de code die u schrijft gemakkelijk kunnen begrijpen.

Hierna begint u met het schrijven van de code die u wilt uitvoeren.

De beste manier om functies te leren is door voorbeelden door te nemen. Laten we dus proberen voorbeelden door te nemen die betrekking hebben op de verschillende objecten en gegevensstructuren waarover we eerder hebben geleerd.

### Eenvoudig voorbeeld van een functie


```python
def say_hello():
    print('hello world')
```

### Het aanroepen van een functie met ()

Roep de functie aan:


```python
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()

```

    hello world
    hello world
    hello world
    hello world
    hello world
    hello world
    hello world
    

Als u het haakje () vergeet, wordt alleen het feit weergegeven dat say_hello een functie is. Later zullen we leren dat we functies kunnen doorgeven aan andere functies! Maar onthoud voor nu gewoon om functies aan te roepen met ().


```python
print(type(say_hello))

print(type(print))
```

    <class 'function'>
    <class 'builtin_function_or_method'>
    

### Parameters accepteren (argumenten)
Laten we een functie schrijven die mensen begroet met hun naam.


```python
def greeting(name):
    print(f'Hello {name}')
```


```python
greeting('Jose')
```

    Hello Jose
    

## Het gebruiken van return
Tot nu toe hebben we alleen print() gebruikt, maar als we de resulterende variabele willen opslaan, moeten we het sleutelwoord **return** gebruiken.

Laten we enkele voorbeelden bekijken die een <code>return</code>-instructie gebruiken. Met <code>return</code> kan een functie een resultaat *retourneren* dat vervolgens als variabele kan worden opgeslagen of op elke gewenste manier kan worden gebruikt.

### Voorbeeld: Toevoegingsfunctie


```python
def add_num(num1,num2):
    return num1+num2
```


```python
add_num(4,5)
```




    9




```python
# Kan ook opslaan als variabele vanwege return
result = add_num(4,5)
```


```python
print(result)
```

    9
    

Wat gebeurt er als we twee strings invoeren?


```python
add_num('one','two')
```




    'onetwo'



## Veel voorkomende vraag: "Wat is het verschil tussen *return* en *print*?"

**Met het trefwoord return kunt u het resultaat van de uitvoer van een functie daadwerkelijk (actually) als variabele opslaan. De functie print() geeft u eenvoudig de uitvoer weer, maar slaat deze niet op voor toekomstig gebruik. Laten we dit in meer detail onderzoeken**


```python
def print_result(a,b):
    print(a+b)
```


```python
def return_result(a,b):
    return a+b
```


```python
print_result(10,5)
```

    15
    


```python
# U zult geen uitvoer zien als u dit in een .py-script uitvoert
return_result(10,5)
```




    15



**Maar wat gebeurt er als we dit resultaat echt willen opslaan voor later gebruik?**


```python
my_result = print_result(20,20)
```

    40
    


```python
my_result
```


```python
type(my_result)
```




    NoneType



**Wees voorzichtig! Merk op hoe print_result() je het resultaat niet in een variabele laat opslaan! Het drukt het alleen af, met print() als resultaat Geen voor de opdracht!**


```python
my_result = return_result(20,20)
```


```python
my_result
```




    40




```python
my_result + my_result
```




    80



# Logica toevoegen aan interne functiebewerkingen (operaties)

Tot nu toe weten we nogal wat over het construeren van logische statements met Python, zoals if/else/elif statements, for en while loops, controleren of een item **in** een lijst is of **niet in** een lijst (Nuttige lezing voor operators). Laten we nu kijken hoe we deze bewerkingen binnen een functie kunnen uitvoeren.

### Controleer of een getal even is

**Herinner de mod-operator % die de rest na deling retourneert, als een getal even is, dan zou mod 2 (% 2) == tot nul moeten zijn.**


```python
2 % 2
```




    0




```python
20 % 2
```




    0




```python
21 % 2
```




    1




```python
20 % 2 == 0
```




    True




```python
21 % 2 == 0
```




    False



** Laten we dit gebruiken om een functie te construeren. Merk op hoe we eenvoudig de booleaanse cheque (boolean) retourneren.**


```python
def even_check(number):
    return number % 2 == 0
```


```python
even_check(20)
```




    True




```python
even_check(21)
```




    False



### Controleer of een getal in een lijst even is

Laten we een boolean teruggeven die aangeeft of **any** getal in een lijst even is. Merk hier op hoe **return** uit de lus breekt en de functie verlaat


```python
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass
```

** Is dit genoeg? NEE! We geven niets terug als ze allemaal oneven zijn!**


```python
check_even_list([1,2,3])
```




    True




```python
check_even_list([1,1,1])
```

** ZEER GEMEENSCHAPPELIJKE FOUT!! LATEN WE EEN GEMEENSCHAPPELIJKE LOGISCHE FOUT ZIEN, LET OP DIT IS VERKEERD!!!**


```python
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # This is WRONG! This returns False at the very first odd number!
        # It doesn't end up checking the other numbers in the list!
        else:
            return False
```


```python
# OH OH! Het geeft False terug na het raken (hitting) van de eerste 1
check_even_list([1,2,3])
```




    False



** Correcte aanpak: we moeten ook een andere return instantieren met False toevoegen die gaat starten NA het doorlopen van de hele lus**


```python
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False
```


```python
check_even_list([1,2,3])
```




    True




```python
check_even_list([1,3,5])
```




    False



### Retourneer alle even getallen in een lijst

Laten we meer complexiteit toevoegen, we zullen nu alle even getallen in een lijst retourneren, anders een lege lijst.


```python
def check_even_list(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers
```


```python
check_even_list([1,2,3,4,5,6])
```




    [2, 4, 6]




```python
check_even_list([1,3,5])
```




    []



## Tuples retourneren voor het uitpakken

** Bedenk dat we een lijst met tuples kunnen doorlopen en de waarden erin kunnen "uitpakken"**


```python
stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]
```


```python
for item in stock_prices:
    print(item)
```

    ('AAPL', 200)
    ('GOOG', 300)
    ('MSFT', 400)
    


```python
for stock,price in stock_prices:
    print(stock)
```

    AAPL
    GOOG
    MSFT
    


```python
for stock,price in stock_prices:
    print(price)
```

    200
    300
    400
    

**Op dezelfde manier retourneren functies vaak tuples, om gemakkelijk meerdere resultaten te retourneren voor later gebruik.**

Laten we ons de volgende lijst voorstellen:


```python
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
```

De functie beneden wilt werknemer van de maand geeft zowel de naam als het aantal gewerkte uren terug voor de top-presteerder (beoordeeld op het aantal gewerkte uren).


```python
def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)
```


```python
employee_check(work_hours)
```




    ('Cassie', 800)



## Interacties tussen functies

Functies gebruiken vaak resultaten van andere functies, laten we een eenvoudig voorbeeld bekijken door middel van een raadspel. Er zullen 3 posities in de lijst zijn, waarvan er één een 'O' is, een functie zal de lijst schudden, een andere zal de gok van een speler nemen, en ten slotte zal een ander controleren of het juist is. Dit is gebaseerd op het klassieke carnavalsspel waarbij je moet raden onder welke beker een rode bal zit.

**Hoe een lijst in Python te shufflen**


```python
example = [1,2,3,4,5]
```


```python
from random import shuffle
```


```python
# Note shuffle is in-place
shuffle(example)
```


```python
example
```




    [3, 1, 4, 5, 2]



**OK, laten we ons simpele spel creëeren**


```python
mylist = [' ','O',' ']
```


```python
def shuffle_list(mylist):
    # Lijst opnemen en shuffle-versie teruggeven
    shuffle(mylist)
    
    return mylist
```


```python
mylist 
```




    [' ', 'O', ' ']




```python
shuffle_list(mylist)
```




    [' ', ' ', 'O']




```python
def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        
        # Terugroepen input() retourneert een string
        guess = input("Pick a number: 0, 1, or 2:  ")
    
    return int(guess)    
```


```python
player_guess()
```

    Pick a number: 0, 1, or 2:  1
    




    1



Nu gaan we de gok van de gebruiker controleren. Merk op dat we hier alleen afdrukken, omdat we de gok van een gebruiker of de geschudde lijst niet hoeven op te slaan.


```python
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)
```

Nu maken we een beetje setup-logica om alle functies uit te voeren. Merk op hoe ze met elkaar omgaan!


```python
# Oorspronkelijke lijst
mylist = [' ','O',' ']

# Schud het
mixedup_list = shuffle_list(mylist)

# Krijg een schatting (guess) van de gebruiker
guess = player_guess()

# Controleer de gok van de gebruiker
#------------------------
# Merk op hoe deze functie de invoer opneemt op basis van de uitvoer van andere functies!
check_guess(mixedup_list,guess)
```

    Pick a number: 0, 1, or 2:  1
    Wrong! Better luck next time
    [' ', ' ', 'O']
    

Geweldig! U zou nu een basiskennis moeten hebben van het maken van uw eigen functies om uzelf te behoeden voor het herhaaldelijk schrijven van code!
