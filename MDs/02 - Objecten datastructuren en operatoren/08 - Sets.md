<center>
    <img src='https://www.intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em><br/>
    <em> Yilmaz Mustafa, Instructeur Java/Python</em>
</center>

# Sets

Een van de andere bekende-objecttypen in Python is een 'Set' die we snel kunnen behandelen omdat het vergelijkbaar met een 'List' is.

Sets zijn een ongeordende verzameling *unieke* elementen. We kunnen ze construeren met behulp van de set() functie. Laten we doorgaan en een set maken om te zien hoe het werkt


```python
x = set()
```


```python
# We kunnen een element toevoegen naar een set met de add()-methode
x.add(1)
```


```python
#Tonen
x
```




    {1}



Let op de accolades(brackets). Dit duidt niet op een dictionary/woordenboek! Hoewel je analogieën kunt tekenen als een set die een woordenboek is met alleen sleutels.

We weten dat een set alleen unieke items heeft. Dus wat gebeurt er als we iets proberen toe te voegen dat al in een set zit?


```python
# Voeg een ander element toe
x.add(2)
```


```python
#Tonen
x
```




    {1, 2}




```python
# Probeer om hetzelfde element toe te voegen
x.add(1)
```


```python
#Tonen
x
```




    {1, 2}



Merk op hoe het daar nog een 1 zal niet toegevoegd worden. Een set gaat namelijk alleen om unieke elementen! We kunnen een lijst met meerdere herhalingselementen casten naar een set om de unieke elementen te krijgen. Bijvoorbeeld:


```python
# Creëer een lijst met herhalingen
list1 = [1,1,2,2,3,4,5,6,1,1]
```


```python
# Cast de lijst als set om unieke values (waarden) te krijgen
set(list1)
```




    {1, 2, 3, 4, 5, 6}



Het hebben van zoveel kennis over sets zou voldoende zijn op junior niveau.
