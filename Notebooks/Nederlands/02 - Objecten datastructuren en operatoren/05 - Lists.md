<center>
    <img src='https://www.intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em><br/>
    <em> Yilmaz Mustafa, Instructeur Java/Python</em>
</center>

# Lijsten

Eerder, bij het bespreken van strings, introduceerden we het concept van een *sequences* in Python. Lijsten kunnen worden gezien als de meest algemene versie van een *reeks/sequences* in Python. In tegenstelling tot strings zijn ze veranderlijk, wat betekent dat de elementen in een lijst kunnen worden gewijzigd!

In deze sectie leren we over:
    
     1.) Lijsten maken
     2.) Lijsten indexeren en snijden (sliceren)
     3.) Basislijstmethoden
     4.) Lijsten nesten
     5.) Inleiding tot lijstbegrippen (Comprehensations)

Lijsten zijn opgebouwd met vierkantehaakjes [] en komma's die elk element in de lijst scheiden.

Laten we eens kijken hoe we lijsten kunnen maken!


```python
# Maak een List genoemd my_list aan
my_list = [1,2,3]
```

We hebeen net een List van integers gecreëerd maar de lijst kan inderdaad meerdere datatypen bevatten. Bijvoorbeeld.:


```python
my_list = ['A string',23,100.232,'o']
```

Net zoals strings, de len() functie gaat teruggeven het aantal van elementen in de list zitten.


```python
len(my_list)
```




    4



### Indexering en Sliceren
We gebruiken indexering en slicering functies net zoals we vroeger met String gebruiken. Laten wee een nieuwe list creëren voor het herinneren hoe ze met String gebruikt worden:


```python
my_list = ['one','two','three',4,5]
```


```python
# Grijp een element op index 0
my_list[0]
```




    'one'




```python
# Grijp index 1 en alle volgende indexen
my_list[1:]
```




    ['two', 'three', 4, 5]




```python
# Grijp alles tot index 3
my_list[:3]
```




    ['one', 'two', 'three']



We kunnen ook + gebruiken om lijsten te concateneren. Het is vergelijkbaar met de samenvoegingen van Strings. 


```python
my_list + ['new item']
```




    ['one', 'two', 'three', 4, 5, 'new item']



Opmerking: De instructie boven gaat niet de echte waarden van de originele-list veranderen


```python
my_list
```




    ['A string', 23, 100.232, 'o']



// TE DOEN:
U zou de lijst opnieuw moeten toewijzen om de wijziging permanent te maken.


```python
# Opnieuw toewijzen
my_list = my_list + ['add new item permanently']
```


```python
my_list
```




    ['A string', 23, 100.232, 'o']



We kunnen ook de * gebruiken voor een duplicatiemethode die lijkt op strings:


```python
# Verdubbel de lijst
my_list * 2
```




    ['A string', 23, 100.232, 'o', 'A string', 23, 100.232, 'o']




```python
# Opnieuw verdubbeling niet permanent
my_list
```




    ['A string', 23, 100.232, 'o']



## Basislijstmethoden

Als je bekend bent met een andere programmeertaal, zou je parallellen kunnen trekken tussen arrays in een andere taal en lijsten in Python. Lijsten in Python zijn echter over het algemeen flexibeler dan arrays in andere talen om twee goede redenen: ze hebben geen vaste grootte (wat betekent dat we niet hoeven te specificeren hoe groot een lijst zal zijn), en ze hebben geen vaste typebeperking (zoals we hierboven hebben gezien).

Laten we verder gaan en enkele meer speciale methoden voor lijsten verkennen:


```python
# Create a new list
list1 = [1,2,3]
```

Gebruik de **append**-methode om een item permanent aan het einde van een lijst toe te voegen:


```python
# Append
list1.append('append me!')
```


```python
# Show
list1
```




    [1, 2, 3, 'append me!']



Gebruik **pop** om een item uit de lijst te verwijderen. Pop haalt standaard de laatste index uit, maar u kunt ook specificeren welke index moet worden verwijderd. Laten we een voorbeeld bekijken:


```python
# Pop off the item with 0 indexed 
list1.pop(0)
```




    1




```python
# Tonen
list1
```




    [2, 3, 'append me!']




```python
# Wijs (assign) het popped element toe, houd rekenen mee dat de standaard popped index -1 popped_item is
popped_item = list1.pop()
```


```python
popped_item
```




    'append me!'




```python
# Toon resterende lijst
list1
```




    [2, 3]



Er moet ook worden opgemerkt dat indexering van lijsten een fout retourneert als er geen element in die index is. Bijvoorbeeld:


```python
list1[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-22-af6d2015fa1f> in <module>()
    ----> 1 list1[100]
    

    IndexError: list index out of range


We kunnen de **sort** methode en de **reverse** methode gebruiken om ook uw lijsten te beïnvloeden:


```python
new_list = ['a','e','x','b','c']
```


```python
#Tonen
new_list
```




    ['a', 'e', 'x', 'b', 'c']




```python
# Gebruik omgekeerd om de volgorde om te keren (dit is permanent!)
new_list.reverse()
```


```python
new_list
```




    ['c', 'b', 'x', 'e', 'a']




```python
# Gebruik sorteren om de lijst te sorteren (in dit geval alfabetische volgorde, maar voor nummers zal het oplopend (ASC) gaan)
new_list.sort()
```


```python
new_list
```




    ['a', 'b', 'c', 'e', 'x']



## Nestlijsten (Geneste lijsten)

Een geweldige eigenschap van Python-datastructuren is dat ze *nesting* ondersteunen. Dit betekent dat we datastructuren binnen datastructuren kunnen hebben. Bijvoorbeeld: Een lijst in een lijst.

Laten we eens kijken hoe dit werkt!


```python
# Laten we drie lijsten maken
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Maak een lijst van lijsten om een matrix te vormen
matrix = [lst_1,lst_2,lst_3]
```


```python
# Tonen
matrix
```




    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



We kunnen indexering opnieuw gebruiken om elementen te pakken, maar nu zijn er twee niveaus voor de index. De items in het matrixobject en dan de items in die lijst!


```python
# Pak het eerste item in het matrixobject
matrix[0]
```




    [1, 2, 3]




```python
# Pak het eerste item van het eerste item in het matrixobject
matrix[0][0]
```




    1



# Lijstbegrippen (Comprehensies)

Python heeft een geavanceerde functie genaamd lijstbegrippen (list comprehensions). Ze zorgen voor een snelle opbouw van lijsten. Om lijstbegrippen volledig te begrijpen, moeten we for-loops begrijpen. Maak je dus geen zorgen als je dit gedeelte niet helemaal begrijpt, en sla het gerust over, want we komen later op dit onderwerp terug.

Maar voor het geval je het nu wilt weten, hier zijn een paar voorbeelden!


```python
# Bouw een lijstbegrip (comprehension) op door een for-lus te deconstrueren binnen een []
first_col = [row[0] for row in matrix]
```


```python
first_col
```




    [1, 4, 7]



We hebben hier een lijstbegrip gebruikt om het eerste element van elke rij in het matrixobject te pakken. We zullen dit later in veel meer detail behandelen!

Voor meer geavanceerde methoden en functies van lijsten in Python, bekijk de sectie Geavanceerde lijsten verderop in deze cursus of van Python documentatie!
