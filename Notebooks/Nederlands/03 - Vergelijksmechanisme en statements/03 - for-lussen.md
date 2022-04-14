<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# for-lussen

Een <code>for</code> lus fungeert als een iterator in Python; het gaat door items die zich in een *sequence* of een ander itereerbaar item bevinden. 
Objecten waarover we hebben geleerd en die we kunnen herhalen, zijn onder meer strings, lijsten, tuples en zelfs ingebouwde iterables voor woordenboeken, zoals sleutels of waarden.

We hebben de <code>for</code>-verklaring al een beetje gezien in eerdere lezingen, maar laten we nu ons begrip formaliseren.

Hier is het algemene formaat voor een <code>for</code>-lus in Python:

    for item in object:
        statements/instructies om uit te voeren
    

De variabelenaam die voor het item wordt gebruikt, is volledig aan de codeur, dus gebruik je gezond verstand om een naam te kiezen die logisch is en die je kunt begrijpen wanneer je je code opnieuw bekijkt. 
Naar deze item-naam kan vervolgens in uw lus worden verwezen, bijvoorbeeld als u <code>if</code>-instructies wilt gebruiken om controles uit te voeren.

Laten we doorgaan en verschillende voorbeelden van <code>for</code>-lussen doornemen met behulp van verschillende typen gegevensobjecten. We beginnen eenvoudig en bouwen later meer complexiteit op.

## Voorbeeld 1
Een lijst itereren


```python
# We zullen leren hoe we dit soort lijst kunnen automatiseren in de volgende lezing
list1 = [1,2,3,4,5,6,7,8,9,10]
```


```python
for num in list1:
    print(num)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

Geweldig! Hopelijk heeft dit zin. Laten we nu een <code>if</code>-statement toevoegen om te controleren op even getallen. We introduceren hier eerst een nieuw concept: de modulo.

### Modulo
De modulo stelt ons in staat om de rest in een deling te krijgen en gebruikt het %-symbool. Bijvoorbeeld:


```python
17 % 5
```




    2



Dit is logisch aangezien 17 gedeeld door 5 3 en de rest 2 is. Laten we nog een paar snelle voorbeelden bekijken:


```python
# 3 rest 1
10 % 3
```




    1




```python
# 3 rest 1
18 % 7
```




    4




```python
# 2 geen rest
4 % 2
```




    0



Merk op dat als een getal volledig deelbaar is zonder rest, het resultaat van de modulo-aanroep (4 % 2) 0 is. We kunnen dit gebruiken om te testen op even getallen, want als een getal modulo 2 gelijk is aan 0, betekent dit dat het een even getal is!

Terug naar de <code>for</code> loops!

## Voorbeeld 2
Laten we alleen de even getallen uit die lijst afdrukken!


```python
for num in list1:
    if num % 2 == 0:
        print(num)
```

    2
    4
    6
    8
    10
    

We hadden daar ook een <code>else</code>-statement kunnen plaatsen:


```python
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')
```

    Odd number
    2
    Odd number
    4
    Odd number
    6
    Odd number
    8
    Odd number
    10
    

## Voorbeeld 3
Een ander veelvoorkomend idee tijdens een <code>for</code>-lus is het bijhouden van een aantal loops tijdens meerdere lussen. Laten we bijvoorbeeld een <code>for</code>-lus maken die de lijst samenvat:


```python
# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum = list_sum + num

print(list_sum)
```

    55
    

Geweldig! Lees de bovenstaande cel door en zorg ervoor dat u volledig begrijpt wat er aan de hand is. We hadden ook een <code>+=</code> kunnen implementeren om de optelling bij de som uit te voeren. Bijvoorbeeld:


```python
# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num

print(list_sum)
```

    55
    

## Voorbeeld 4
We hebben <code>for</code> loops gebruikt met lijsten, wat dacht je van met strings? Onthoud dat strings een reeks zijn, dus als we er doorheen gaan, hebben we toegang tot elk item in die string.


```python
for letter in 'This is a string.':
    print(letter)
```

    T
    h
    i
    s
     
    i
    s
     
    a
     
    s
    t
    r
    i
    n
    g
    .
    

## Voorbeeld 5
Laten we nu kijken hoe een <code>for</code>-lus kan worden gebruikt met een tuple:


```python
tup = (1,2,3,4,5)

for t in tup:
    print(t)
```

    1
    2
    3
    4
    5
    

## Voorbeeld 6
Tuples hebben een unieke kwaliteit als het gaat om <code>for</code> loops. Als je wilt een reeks itereren die tuples bevat, kan het item de tuple zelf zijn, dit is een voorbeeld van *tuple unpacking*. 
Tijdens de <code>for</code>-lus zullen we de tuple in een reeks uitpakken en hebben we toegang tot de afzonderlijke items in die tuple!


```python
list2 = [(2,4),(6,8),(10,12)]
```


```python
for tup in list2:
    print(tup)
```

    (2, 4)
    (6, 8)
    (10, 12)
    


```python
# Nu met uitpakken!
for (t1,t2) in list2:
    print(t1)
```

    2
    6
    10
    

Koel! Met tupels in een reeks hebben we toegang tot de items erin door ze uit te pakken! De reden dat dit belangrijk is, is omdat veel objecten hun iterables via tuples zullen leveren. 
Laten we beginnen met het verkennen van iteratie door dictionaries om dit verder te onderzoeken!

## Voorbeeld 7


```python
d = {'k1':1,'k2':2,'k3':3}
```


```python
for item in d:
    print(item)
```

    k1
    k2
    k3
    

Merk op hoe dit alleen de sleutels produceert. Dus hoe kunnen we de waarden (values) krijgen? Of zowel de sleutels (keys) als de waarden?

We gaan drie nieuwe Dictionary-methoden introduceren: **.keys()**, **.values()** en **.items()**

In Python retourneert elk van deze methoden een *dictionary view-object*. Het ondersteunt bewerkingen zoals lidmaatschapstest (membership-test) en iteratie, maar de inhoud ervan is niet onafhankelijk van het originele woordenboek - het is slechts een weergave. 
Laten we het in actie zien:


```python
# Create a dictionary view object
d.items()
```




    dict_items([('k1', 1), ('k2', 2), ('k3', 3)])



Sindsdien ondersteunt de .items()-methode iteratie, we kunnen *dictionaries uitpakken* uitvoeren om sleutels en waarden te scheiden, net zoals we deden in de vorige voorbeelden.


```python
# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 
```

    k1
    1
    k2
    2
    k3
    3
    

Als u een echte lijst met keys, values of key/value-tuples wilt verkrijgen, kunt u de weergave *casten* als een lijst:


```python
list(d.keys())
```




    ['k1', 'k2', 'k3']



Onthoud dat dictionaries ongeordend zijn en dat keys en values in willekeurige (random) volgorde terugkomen. U kunt een gesorteerde lijst verkrijgen met behulp van Sort():


```python
sorted(d.values())
```




    [1, 2, 3]



## Gevolgtrekking

We hebben geleerd hoe we for-lussen kunnen gebruiken om door tuples, lijsten, strings en dictionaries te itereren. Het zal een cruciaal hulpmiddel voor ons zijn, dus zorg ervoor dat u het goed kent en de bovenstaande voorbeelden begrijpt.

[Meer bronnen] (http://www.tutorialspoint.com/python/python_for_loop.htm)
