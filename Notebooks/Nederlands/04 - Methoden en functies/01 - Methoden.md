<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Methoden

We hebben al een paar voorbeelden van methoden gezien bij het leren over object- en gegevensstructuurtypen in Python. Methoden zijn in wezen functies die in objecten zijn ingebouwd. 
Later in de cursus leren we hoe we onze eigen objecten en methoden kunnen maken met behulp van Object Oriented Programming (OOP) en klassen.

Methoden voeren specifieke acties uit op een object en kunnen ook argumenten aannemen, net als een functie. 
Deze lezing is slechts een korte introductie tot methoden en zet je aan het denken over algemene ontwerpmethoden die we zullen bespreken wanneer we OOP in de cursus bereiken.

Methoden zijn in de vorm:

    object.method(arg1,arg2,etc...)
    
Je zult later zien dat we methoden kunnen zien als een argument 'zelf' dat verwijst naar het object zelf. Je kunt dit argument niet zien, maar we zullen het later in de cursus gebruiken tijdens de OOP-lezingen.

Laten we eens kijken wat een voorbeeld is van de verschillende methoden die een lijst heeft:


```python
# Create a simple list
lst = [1,2,3,4,5]
```

Gelukkig kunnen we met iPython en de Jupyter Notebook snel alle mogelijke methoden zien met behulp van de tab-toets (tab-key). De methoden voor een lijst zijn:

* append
* count
* extend
* insert
* pop
* remove
* reverse
* sort

Laten we er een paar uitproberen:

append() stelt ons in staat om elementen toe te voegen aan het einde van een lijst:


```python
lst.append(6)

```


```python
lst
```




    [1, 2, 3, 4, 5, 6]



Geweldig! Hoe zit het nu met tellen ()? De methode count() telt het aantal keren dat een element in een lijst voorkomt.


```python
# Controleer hoe vaak 2 in de lijst voorkomt
lst.count(2)
```




    1



U kunt altijd Shift+Tab gebruiken in Jupyter Notebook om meer hulp over de methode te krijgen. In Python kun je in het algemeen de help() functie gebruiken:


```python
help(lst.count)
```

    Help on built-in function count:
    
    count(...) method of builtins.list instance
        L.count(value) -> integer -- return number of occurrences of value
    
    

Voel je vrij om te spelen met de rest van de methoden voor een lijst. Verderop in dit gedeelte zal je quiz gebruik maken van help en Google zoeken naar methoden voor verschillende soorten objecten!

Geweldig! Door deze lezing zou je je op je gemak moeten voelen bij het aanroepen van methoden van objecten in Python!
