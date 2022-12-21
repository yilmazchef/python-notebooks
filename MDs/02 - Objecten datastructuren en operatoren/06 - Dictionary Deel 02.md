## Dictionary Deel 02

In de vorige sessie hebben we geleerd over "sequenties". Laten we nu overschakelen en leren over "mappings" in Python. Deze woordenboeken zijn niets anders dan hashtabellen in andere programmeertalen.

In dit deel zullen we kort leren over een inleiding tot woordenboeken en waar ze uit bestaan:

1.) Het construeren van een woordenboek
2.) Objecten benaderen vanuit een woordenboek
3.) Woordenboeken nesten
4.) Basismethoden voor woordenboeken

Voordat we diep in dit concept duiken, laten we eerst begrijpen wat Mappings zijn?

Mappings zijn een verzameling objecten die worden opgeslagen aan de hand van een "sleutel". In tegenstelling tot een sequentie, slaan mappings objecten op volgens hun relatieve positie. Dit is een belangrijk onderscheid, omdat mappings de volgorde niet behouden, omdat ze objecten hebben die worden gedefinieerd door een sleutel.

Een Python woordenboek bestaat uit een sleutel en dan een geassocieerde waarde. Die waarde kan bijna elk Python-object zijn.
Een woordenboek construeren

Laten we eens kijken hoe we woordenboeken kunnen construeren om beter te begrijpen hoe ze werken!
" " or ' '- String
[]- Lists
() tuple
([]) set or {}
{} dictionary, but it will have key value

```python
l=["Thor","Marvel", "Thor- Ragnarok"]
      0       1            2
     name     studio     movie   
```

dictionary is a key -valye pair<br>
{key1:value1,key2:value2.....}<br>
its mutable data type<br>
No indexing required<br>


```python
w={"name":"Thor","place":"Asguardian","movie":"Thor--Ragnarok"}
```


```python
w={"name":"Thor","place":"Asguardian","movie":"Thor--Ragnarok", "name": ["Thor","Ironman","Captain America"] }
w
# print(w['name'])
```




    {'name': ['Thor', 'Ironman', 'Captain America'],
     'place': 'Asguardian',
     'movie': 'Thor--Ragnarok'}




```python
type(w)
```




    dict




```python
w["name1"]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-62-895bdb824833> in <module>
    ----> 1 w["name1"]
    

    KeyError: 'name1'



```python
w["place"]
```




    'Asguardian'




```python
data = {1:1,2:7,'b':2,'c':7}
```


```python
data[1]=200
data
```




    {1: 200, 2: 7, 'b': 2, 'c': 7}




```python
data1 = dict(a=10, b=2, c=3)
```


```python
data1
```




    {'a': 10, 'b': 2, 'c': 3}




```python
w={"name":"Thor","place":"Asguardian","movie":"Thor: Ragnarok"}
```


```python
# dir(w)
```


```python
# type(w.keys())
# type(w.keys())
list(w.keys())
```




    ['name', 'place', 'movie']




```python
list(w.values())
```




    ['Thor', 'Asguardian', 'Thor: Ragnarok']



### De sleutels van een woordenboek kunnen elk soort onveranderlijk type zijn, waaronder tekenreeksen, getallen en tupels:



```python
mydict = {"hello": "world",
          0: "a",
          1: "b",
          "2": "not a number",
         (1, 2, 3): "a tuple!"}
mydict
```




    {'hello': 'world', 0: 'a', 1: 'b', '2': 'not a number', (1, 2, 3): 'a tuple!'}




```python
a=(1,2,3)
dict1 = {"hello": "world",
          0: "a",
          1: "b",
          "2": "not a number",
         a: "a tuple!"}
dict1
```




    {'hello': 'world', 0: 'a', 1: 'b', '2': 'not a number', (1, 2, 3): 'a tuple!'}




```python
a=[1,2,3]
# a="python"
mydict = {"hello": "world",
          0: "a",
          1: "b",
          "2": "not a number",
         a: "a list!"}
mydict
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-73-d39b7788463c> in <module>
          1 a=[1,2,3]
          2 # a="python"
    ----> 3 mydict = {"hello": "world",
          4           0: "a",
          5           1: "b",
    

    TypeError: unhashable type: 'list'



```python
mydict = {"hello": "world",
          10: "a",
          1: "b",
          "2": "not a number",
         1: "a tuple!",
         0: "abc",}
mydict
```




    {'hello': 'world', 10: 'a', 1: 'a tuple!', '2': 'not a number', 0: 'abc'}




```python
data = {'z':1,'b':2,'c':7,'d':6}
```


```python
data['z']
```




    1




```python
data['b']
```




    2




```python
data['a']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-78-3aa42f1ca3be> in <module>
    ----> 1 data['a']
    

    KeyError: 'a'



```python
data[(1,2,3)]=3  # updates if 'a' exists, else adds 'a'
data
```




    {'z': 1, 'b': 2, 'c': 7, 'd': 6, (1, 2, 3): 3}




```python
data['a']=4
data
```




    {'z': 1, 'b': 2, 'c': 7, 'd': 6, (1, 2, 3): 3, 'a': 4}




```python
data.update({'a':"football"})
print(data)
data['a']="python"
data
```

    {'z': 1, 'b': 2, 'c': 7, 'd': 6, (1, 2, 3): 3, 'a': 'football'}
    




    {'z': 1, 'b': 2, 'c': 7, 'd': 6, (1, 2, 3): 3, 'a': 'python'}




```python
data = {'z':1,'b':2,'c':7,'d':6}
data.update(dict(a=10099))
data
```




    {'z': 1, 'b': 2, 'c': 7, 'd': 6, 'a': 10099}



## Het samenvoegen van 2 dictionaries



```python
data1 = {'a':1,'b':2,'c':7,'k':6}
data2 = {'e':1,'l':2}
data3 = {'a':4,'l':5,'c':"python",'f':89}
```


```python
data1.update(data2)  # Where data2 is also a dict.
data1
```




    {'a': 10, 'b': 2, 'c': 3, 'e': 1, 'l': 2}




```python
data1.update(data3)
```


```python
data1
```




    {'a': 4, 'b': 2, 'c': 'python', 'e': 1, 'l': 5, 'f': 89}



### Verwijdering van gegevens


```python
data = {100:1,'b':2,'c':7,'k':6}
del data['b']
```


```python
data
```




    {100: 1, 'c': 7, 'k': 6}




```python
del data
```


```python
data
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-89-c5d84736ba45> in <module>
    ----> 1 data
    

    NameError: name 'data' is not defined



```python
data = {100:1,'b':2,'c':7,'k':6, 'm':[1,2,3]}
# data.clear()
data['m']=[1,2]
```


```python
data
```

### Het samenvoegen van 2 lijsten


```python
dishes = ["pizza", "sauerkraut", "paella", "Hamburger", ' ']
countries = ["Italy", "Germany", "Spain", "USA"]
c1 = [1,2,3,4]
```


```python
country_specialities = zip(countries, dishes)
# help(zip)
```


```python
for i in country_specialities:
    print(i)
# print(dict(country_specialities))
```

    ('Italy', 'pizza')
    ('Germany', 'sauerkraut')
    ('Spain', 'paella')
    ('USA', 'Hamburger')
    


```python
print(list(country_specialities))
print(id(country_specialities))
print(type(country_specialities))
```

    []
    2273043636032
    <class 'zip'>
    


```python
d=dict(country_specialities)
d
```




    {}




```python
dishes = ["pizza", "paella", "paella", "Hamburger",]
countries = ["Italy", "Germany", "Spain", "USA","asdfs",2332,232]
country_specialities = zip(dishes,countries)
dict((country_specialities))
```




    {'pizza': 'Italy', 'paella': 'Spain', 'Hamburger': 'USA'}




```python
country_specialities = zip(dishes,countries)
```


```python
l=list((country_specialities))
# counrtySpecilities
print(l)
# print(l[0][1])
```

    [('pizza', 'Italy'), ('paella', 'Germany'), ('paella', 'Spain'), ('Hamburger', 'USA')]
    

### Opdracht


```python
l=list()
t=tuple()
heights={}
heights['belgian horse']= 162
heights['tiger']= 168
heights['cat']=58
heights['dog']=57
heights['cow']=59
heights['lion']=109
```


```python
heights.keys()
```




    dict_keys(['belgian horse', 'tiger', 'cat', 'dog', 'cow', 'lion'])




```python
heights.values()
```




    dict_values([162, 168, 58, 57, 59, 109])




```python
x=heights.items()
print(x)
# help(x)
```

    dict_items([('belgian horse', 162), ('tiger', 168), ('cat', 58), ('dog', 57), ('cow', 59), ('lion', 109)])
    


```python
for i in "python":
    print (i)
```

    p
    y
    t
    h
    o
    n
    


```python
l=["python","java", "scala"]
for i in l:
    print (i)
```

    python
    java
    scala
    


```python
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
for i in heights:
    print (i)
```

    belgian horse
    tiger
    cat
    dog
    cow
    lion
    


```python
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
for i in heights:
    print (heights[i])
```

    162
    168
    58
    57
    59
    109
    


```python
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
for i in heights:
    print (i,heights[i])
```

    belgian horse 162
    tiger 168
    cat 58
    dog 57
    cow 59
    lion 109
    

#### Lees een gebruikersinvoer als een diernaam en geef de hoogte van dat dier terug


```python
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
```


```python
user_input_animal_name = input("Enter the name of animal: ")
# print(heights[user_input_animal_name])
for x in heights:
    if x==user_input_animal_name:
        print(heights[x])
```

#### Neem een gebruikersinvoer als hoogte en druk de naam van het dier af


```python
# findanimal=57
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
findanimal=int(input("Enter the height of animal "))
for i in heights:
	if heights[i]==findanimal:
		print (i)
        
```

#### Behandeling van ontbrekende keys in Python-dictionaries

In python zijn woordenboeken containers die een sleutel aan zijn waarde koppelen met een toegangstijdcomplexiteit van O(1). Maar in veel toepassingen kent de gebruiker niet alle sleutels in de woordenboeken. In dergelijke gevallen, als de gebruiker probeert een ontbrekende sleutel te openen, verschijnt er een foutmelding over ontbrekende sleutels.



```python
# initializing Dictionary 
d = { 'a' : 1 , 'b' : 2 } 
print ("The value associated with 'c' is : ") 
print (d['c']) 
print(" learning python is fun")
print(" python is awsome")
```

get(key,def_val) is nuttig wanneer we de sleutel moeten controleren. Als de sleutel aanwezig is, wordt de bij de sleutel behorende waarde afgedrukt, anders wordt de def_value die in de argumenten wordt meegegeven, teruggegeven.


```python
d = { 'a' : 1 , 'b' : 2,'c': 'python' } 
print (d.get('d',"key does not exist ") )
print("learning python is fun")
```


```python
d = { 'a' : 1 , 'b' : 2,'c': 'python' } 
print (d.get('abc',"1111") )
```


```python
d = { 'a' : 1 , 'b' : 2,'abc': 'python' } 
print (d.get('abc',"1111") )
```


```python
d = { 'a' : 1 , 'b' : 2 } 
print (d.get('c','sdf') )
```


```python
phonebook = {"Mike Jones": "281-330-8004", "Jenny": "867-5309","Destiny": "900-783-3369"}
```


```python
print(sorted(phonebook))
print(phonebook["Destiny"])    
```


```python
for contact_name in sorted(phonebook):
    print(contact_name, phonebook[contact_name])
```


```python
phonebook = {"Mike Jones": "281-330-8004",'1': "867-5309",'3': "900-783-3369"}
print(sorted(phonebook))

```


```python
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['c'] = 2
d['b'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value)
```


```python
from collections import OrderedDict 
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() # preserve the order in which key values are entered
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items(): 
    print(key, value)

```

defaultdict" is een container die is gedefinieerd in de module "collections". Het neemt een functie (default factory) als argument. Standaard is default factory ingesteld op "int", d.w.z. 0. Als een sleutel niet aanwezig is in defaultdict, wordt de standaard fabriekswaarde geretourneerd en weergegeven. Dit heeft voordelen ten opzichte van get() of setdefault().

Een standaardwaarde wordt ingesteld bij de declaratie. Het is niet nodig de functie steeds opnieuw aan te roepen en soortgelijke waarden als argumenten door te geven. Dat bespaart tijd.

De implementatie van defaultdict is sneller dan get() of setdefault().

Lijsten zijn eigenlijk vrij snel wanneer je een item benadert via zijn indexnummer - aangezien alles wat er onder de motorkap gebeurt een directe toegang is tot een bekende en gemakkelijk te berekenen geheugenlocatie. Lijsten kunnen echter erg traag zijn bij het zoeken (met behulp van in), omdat de enige manier om een lijst te doorzoeken is elk item in de lijst te benaderen, beginnend bij het negende element en oplopend tot het laatste element in de lijst.

Een woordenboek gebruikt een gegevensstructuur die een hashmap heet (Python-woordenboeken zijn geoptimaliseerde versies), en een sleutel wordt met een hash-algoritme omgezet van een tekenreeks (of wat dan ook) in een geheel getal, en het is een paar heel eenvoudige berekeningen om dat geheel getal te nemen en de juiste plaats in het woordenboek te vinden om te zoeken.

Het verschil tussen een lijst en een woordenboek is het verschil tussen een grote verzameling boekenplanken en een bibliotheek. Om een boek te vinden in een reeks boekenplanken moet je elke plank één voor één doorzoeken, terwijl een bibliotheek een index heeft waarmee de lezer vanaf de titel van een boek direct naar een specifieke plank kan gaan. In een Python-woordenboek is het het "hash-algoritme" dat fungeert als bibliotheekindex.

### Opdracht

Schrijf een programma om sleutels om te zetten in waarden en omgekeerd.


```python
person = {'name': 'abc', 'age': 50}
copy_person = {}
for i in person:
    copy_person[person[i]] = i
print(copy_person)
```


```python
inverse=dict()
for key in heights:   # 'dog' in heights
	val=heights[key]      # val= heigths[dog]-->57
	if val not in inverse:
		inverse[val] = key    #inverse[57]='dog'
	# else:
	# 	inverse[val].append(key)
print (inverse)

```

* Python-programma om een sleutel-waarde-paar aan het dictionary toe te voegen
* Python-programma om twee dictionaries tot één samen te voegen
* Python-programma om te controleren of een gegeven sleutel al dan niet in een dictionary voorkomt*. 
* Python Programma om een dictionary te genereren dat getallen bevat (tussen 1 en n) in de vorm (x,x*x).
* Python-programma om alle items in een dictionary op te tellen
* Python-programma om alle items in een dictionary te vermenigvuldigen
* Python-programma om de gegeven sleutel uit een dictionary te verwijderen
* Python-programma om een dictionary te vormen uit een object van een klasse
* Python-programma om twee lijsten in een dictionary in te delen
* Python-programma voor het tellen van de frequentie van woorden in een string met behulp van een dictionary
* Python-programma om een dictionary te maken met sleutel als eerste teken en waarde als woorden die beginnen met dat teken* er


```python
s=10
print("hello",s)
```


```python
myDict = {'a': 100, 'b':200, 'c':300} 
sum = 0
for i in myDict: 
    sum = sum + myDict[i] 
print("Sum :", sum) 
```


```python
import sys
sys.version
```


```python

```
