<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Opdrachten Hoofdstuk 00

## Test je eigen kennis.

** Beantwoord de volgende vragen **

Schrijf (of zeg het gewoon hardop tegen jezelf) een korte beschrijving van alle volgende objecttypen en gegevensstructuren waarover we hebben geleerd. U kunt de onderstaande cel bewerken door erop te dubbelklikken. Dit is echt alleen om te testen of je het verschil hiertussen weet, dus voel je vrij om er gewoon over na te denken, aangezien je antwoorden zelfbeoordeeld zijn.

Dubbelklik HIER om deze markdown-cel te bewerken en antwoorden te schrijven.

Getallen:

Strings:

Lists:

Tuples:

Dictionaries:


## Getallen

Schrijf een vergelijking die vermenigvuldiging, deling, een exponent, optelling en aftrekking (multiplication, division, an exponent, addition, and subtraction) gebruikt die gelijk is aan 100,25.
Hint: dit is alleen om je geheugen/kennis van de rekenkundige basiscommando's te testen, werk achteruit vanaf 100.25


```python
# voeg je code hier toe ..
```

Beantwoord deze 3 vragen zonder code te typen. Typ vervolgens code om je antwoord te controleren.

    Wat retourneert het expressie zoals de volgende: 4 * (6 + 5)
    
    Wat retourneert het expressie zoals de volgende: 4 * 6 + 5 
    
    Wat retourneert het expressie zoals de volgende: 4 + 6 * 5 


```python

```

Wat is het *type* van het resultaat van de uitdrukking (berekening) zoals de volgende: 3 + 1.5 + 4?<br><br>

Wat zou je gebruiken om de vierkantswortel (square root) van een getal te vinden, evenals het vierkant (square)?


```python
# Square root:

```


```python
# Square:

```

## Strings

Geef, gezien de string 'hallo', een indexcommando dat 'e' teruggeeft. Voer uw code in de cel hieronder in:


```python
s = 'hello'
# Print 'e' uit met indexering


```

Keer (Reverse) de string 'hallo' om met behulp van het snijden (slicing):


```python
s ='hello'
# Keer de string om met het snijden (slicing)


```

Geef, gezien de String hallo, twee methoden om de letter 'o' te produceren met behulp van indexering.


```python
s ='hello'
# Print de 'o' uit

# Methode 1:


```


```python
# Methode 2:


```

## Lists

Maak deze lijst [0,0,0] aan op twee verschillende manieren samen.


```python
# Methode 1:

```


```python
# Methode 2:

```

Wijs 'hallo' opnieuw toe in deze geneste lijst om in plaats daarvan 'goodbye' te zeggen:


```python
list3 = [1,2,[3,4,'hello']]


```

Sorteer de lijst hieronder:


```python
list4 = [5,3,4,6,1]


```

## Dictionaries

Gebruik keys (sleutels) en indexering om de 'hello' uit de volgende dictionaries/woordenboeken te halen:


```python
d = {'simple_key':'hello'}
# Grijp 'hello'

```


```python
d = {'k1':{'k2':'hello'}}
# Grijp 'hello'

```


```python
# Laten we een beetje tricker worden
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# Grijp hello

```


```python
# Dit zal moeilijk en vervelend zijn!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
```

Kan je een dictionary sorteren? Waarom wel of niet?<br><br>

## Tuples

Wat is het belangrijkste verschil tussen tuples en lijsten?<br><br>

Hoe maak je een tuple aan?<br><br>

## Sets 

Wat is er uniek aan een set?<br><br>

Gebruik een set om de unieke waarden van de onderstaande lijst te vinden:


```python
list5 = [1,2,2,33,4,4,11,22,3,3,2]



```

## Booleans

Voor de volgende quizvragen krijgen we een voorbeeld van vergelijkingsoperatoren. In de onderstaande tabel zijn a=3 en b=4.

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Beschrijving</th><th>Voorbeeld</th>
</tr>
<tr>
<td>==</td>
<td>Als de waarden van twee operanden gelijk zijn, wordt de voorwaarde True.</td>
<td> (a == b) is not true.</td>
</tr>
<tr>
<td>!=</td>
<td>Als de waarden van twee operanden niet gelijk zijn, wordt de voorwaarde 'True'.</td>
<td> (a != b) is true.</td>
</tr>
<tr>
<td>&gt;</td>
<td>Als de waarde van de linker operand groter is dan de waarde van de rechter operand, wordt de voorwaarde 'True'.</td>
<td> (a &gt; b) is not true.</td>
</tr>
<tr>
<td>&lt;</td>
<td>Als de waarde van de linker operand kleiner is dan de waarde van de rechter operand, wordt de voorwaarde 'True'.</td>
<td> (a &lt; b) is true.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>Als de waarde van de linker operand groter is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde 'True'.</td>
<td> (a &gt;= b) is not true. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>Als de waarde van de linker operand kleiner is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde 'True'.</td>
<td> (a &lt;= b) is true. </td>
</tr>
</table>

Wat zal de resulterende Boolean zijn van de volgende stukjes code (antwoord eerst en controleer door het in te typen!)


```python
# Beantwoord voordat u de cel uitvoert
2 > 3
```


```python
# Beantwoord voordat u de cel uitvoert
3 <= 2
```


```python
# Beantwoord voordat u de cel uitvoert
3 == 2.0
```


```python
# Beantwoord voordat u de cel uitvoert
3.0 == 3
```


```python
# Beantwoord voordat u de cel uitvoert
4**0.5 != 2
```

Laatste vraag: Wat is de booleaanse uitvoer van het onderstaande cel-blok?


```python
# twee geneste lijsten
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True of False?
l_one[2][0] >= l_two[2]['k1']
```

## Goed gedaan bij je eerste opdracht!
