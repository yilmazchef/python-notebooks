<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Nuttige operators

Er zijn een paar ingebouwde functies en "operators" in Python die niet goed in een categorie passen, dus we zullen ze in deze lezing bespreken, laten we beginnen!

## range (bereik)

Met de bereikfunctie kun je snel *genereren* een lijst met gehele getallen, dit is erg handig, dus let goed op hoe je het gebruikt! 
Er zijn 3 parameters die u kunt doorgeven, een start, een stop en een stapgrootte. Laten we enkele voorbeelden bekijken:


```python
# range(0,11)

for num in range(0, 10): # 2de argument is exclusief
    print(num)
```

Merk op dat dit een **generator**-functie is, dus om er een lijst uit te halen, moeten we deze naar een lijst casten met **list()**. Wat is een generator? 
Het is een speciaal type functie dat informatie genereert en niet in het geheugen hoeft op te slaan. We hebben het nog niet gehad over functies of generatoren, dus houd dit voorlopig in je notities.


```python
# Notice how 11 is not included, up to but not including 11, just like slice notation!
# list(range(0,11))

for num in range(0, 1000, 100): # 3rde argument is de stapgrootte
    print(num)
    

```


```python
for num in range(10, 0, -1): # stapgrootte kan ook negatief zijn
    print(num)
```


```python
list(range(0,12))
```


```python
# Derde parameter is stapgrootte!
# stapgrootte betekent gewoon hoe groot je sprong/leap/stap je bent
# neem van het start-getal om naar het volgende getal te gaan.

list(range(0,11,2))
```


```python
list(range(0,101,10))
```

## opsommen (enumerate)

Enumerate is een zeer nuttige functie om te gebruiken met for-lussen. Laten we ons de volgende situatie voorstellen:


```python
message = "Hello World!"

for c in message:
    print(c)
```

    H
    e
    l
    l
    o
     
    W
    o
    r
    l
    d
    !
    


```python
print(len(message))

counter = 0
for c in message:
    counter = counter + 1
    
print(counter)
```

    12
    12
    


```python
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
```


```python
message = "Hello World!"

enumerated_message = enumerate(message)
print(type(enumerated_message))
# enumerated_message heeft een index en een value
# [0, 'H']
# [1, 'e']
# [2, 'l']
# [3, 'l']
# [4, 'o']
# [5, ' ']
# [6, 'W']
# [7, 'o']
# [8, 'r']
# [9, 'l']
# [10, 'd']
# [11, '!']

for i, c in enumerate(message):
    print("At index {} the letter is {}".format(i, c))
    
```

    <class 'enumerate'>
    At index 0 the letter is H
    At index 1 the letter is e
    At index 2 the letter is l
    At index 3 the letter is l
    At index 4 the letter is o
    At index 5 the letter is  
    At index 6 the letter is W
    At index 7 the letter is o
    At index 8 the letter is r
    At index 9 the letter is l
    At index 10 the letter is d
    At index 11 the letter is !
    


```python
# bijvoorbeeld:
# stel je hebt een lijst met namen en je wilt de namen

students = ["John", "Jane", "Jack", "Jill", "Joe"]

for index, student in enumerate(students):
    print("At index {} the student is {}".format(index, student))

# verwijder een student uit de lijst met index 3

students.pop(3)

print("########################################################")

# druk de lijst af

for index, student in enumerate(students):
    print("At index {} the student is {}".format(index, student))

```

    At index 0 the student is John
    At index 1 the student is Jane
    At index 2 the student is Jack
    At index 3 the student is Jill
    At index 4 the student is Joe
    ########################################################
    At index 0 the student is John
    At index 1 the student is Jane
    At index 2 the student is Jack
    At index 3 the student is Joe
    

Het bijhouden (track) van hoeveel loops je hebt doorlopen is zo gewoon, dat enumerate is gemaakt, zodat je je geen zorgen hoeft te maken over het creëren en updaten van deze index_count of loop_count variabele.


```python
# Let op het uitpakken van de tuple!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
```

## zip

Merk op dat het formaat enumerate daadwerkelijk terugkeert, laten we eens kijken door het te transformeren naar een list()


```python
message1 = "Hello World!"
message2 = "Hello Jupiter!"
message3 = "Hello Mars!"

all_messages = zip(message1, message2, message3)

print(type(all_messages))

print(list(all_messages))

# [
    # ('H', 'H', 'H'), 
    # ('e', 'e', 'e'), 
    # ('l', 'l', 'l'), 
    # ('l', 'l', 'l'), 
    # ('o', 'o', 'o'), 
    # (' ', ' ', ' '), 
    # ('W', 'J', 'M'), 
    # ('o', 'u', 'a'), 
    # ('r', 'p', 'r'), 
    # ('l', 'i', 's'), 
    # ('d', 't', '!')
# ]
```

    <class 'zip'>
    [('H', 'H', 'H'), ('e', 'e', 'e'), ('l', 'l', 'l'), ('l', 'l', 'l'), ('o', 'o', 'o'), (' ', ' ', ' '), ('W', 'J', 'M'), ('o', 'u', 'a'), ('r', 'p', 'r'), ('l', 'i', 's'), ('d', 't', '!')]
    


```python
number_list_1 = [1, 2, 3, 4, 5]
number_list_2 = [6, 7, 8, 9, 10]

all_numbers = zip(number_list_1, number_list_2)
all_numbers = list(all_numbers)

print(all_numbers)

print(type(all_numbers[0]))
```

    [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
    <class 'tuple'>
    


```python
list(enumerate('abcde'))
```

Het was een lijst met tuples, wat betekent dat we tuple uitpakken konden gebruiken tijdens onze for-loop. Deze datastructuur is eigenlijk heel gewoon in Python , vooral als je met externe bibliotheken werkt. 
U kunt de functie **zip()** gebruiken om snel een lijst met tuples aan te maken door twee lijsten aan elkaar te "zippen".


```python
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
```


```python
# Deze is ook een generator! We zullen dit later uitleggen, maar laten we het nu omzetten (transformeren) in een lijst
zip(mylist1,mylist2)
```


```python
list(zip(mylist1,mylist2))
```

Om de generator te gebruiken, kunnen we gewoon een for-lus gebruiken


```python
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
```


```python
bad_words = [ "hate", "hell" ]
offensive_words = [ "stupid", "idiot", "dumb" ]

all_words = bad_words + offensive_words

print(all_words)
```

    ['hate', 'hell', 'stupid', 'idiot', 'dumb']
    


```python
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
no_of_vacations = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

salary_matrix = zip(months, days_per_month, no_of_vacations)
salary_matrix = list(salary_matrix)

print(salary_matrix)
```

    [('January', 31, 0), ('February', 28, 0), ('March', 31, 1), ('April', 30, 1), ('May', 31, 1), ('June', 30, 1), ('July', 31, 1), ('August', 31, 1), ('September', 30, 1), ('October', 31, 1), ('November', 30, 0), ('December', 31, 0)]
    

## in operator

We hebben het trefwoord (keyword) **in** al gezien tijdens de for-lus, maar we kunnen het ook gebruiken om snel te controleren of een object in een lijst staat.


```python
"h" in "hello"
```




    True




```python
'x' in ['x','y','z']
```


```python
'x' in [1,2,3]
```


```python
x = 10

x in [10, 20, 30]
```




    True



## not in

We kunnen **in** combineren met een **not** operator, om te controleren of een object of variabele niet in een lijst voorkomt/staat.


```python
'x' not in ['x','y','z']
```


```python
"h" not in "hello"
```




    False




```python
'x' not in [1,2,3]
```


```python
x = 10

x not in [10, 20, 30]
```




    False



## min and max

Controleer snel het minimum of maximum van een lijst met deze functies.


```python
mylist = [10,20,30,40,100]
```


```python
min(mylist)
```




    10




```python
max(mylist)
```




    100




```python
min("Hello")
```




    'H'




```python
max("Hello")
```




    'o'




```python
floating_numbers = [1.2, 5.9, 2.1, 4.3, 5.2, 5.9]

print(
    min(floating_numbers),
    max(floating_numbers)
)
```

    1.2 5.9
    


```python
# sort the list met min en max

# floating_numbers.sort()

for i in range(0, len(floating_numbers)):
    print(min(floating_numbers))
    floating_numbers.remove(min(floating_numbers))

```

    1.2
    2.1
    4.3
    5.2
    5.9
    5.9
    

## random (willekeurig)

Python wordt geleverd met een ingebouwde willekeurige (random) bibliotheek. Er zijn veel functies in deze willekeurige bibliotheek, dus we zullen je voorlopig slechts twee handige functies laten zien.


```python
from random import shuffle
```


```python
# Hierdoor wordt de lijst "in-place" geschud (shuffled), wat betekent dat er niets wordt geretourneerd, maar dat het de doorgegeven lijst beïnvloedt.
shuffle(mylist)
```


```python
mylist
```


```python
from random import randint
```


```python
# Retourneer willekeurig geheel getal in bereik [a, b], inclusief beide eindpunten.
randint(0,100)
```


```python
# Retourneer willekeurig geheel getal in bereik [a, b], inclusief beide eindpunten.
randint(0,100)
```

## input (invoer)


```python
input('Enter Something into this box: ')
```


```python
chosen_number = int(input('Enter a number: '))

print(chosen_number)
```

    99
    
