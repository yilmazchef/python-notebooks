<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Functies en methoden Huiswerk

Vul de volgende vragen in:
____
**Schrijf een functie die het volume van een bol (sphere) berekent op basis van zijn straal (radius).**
<p>Het volume van een bol wordt gegeven als $$\frac{4}{3} πr^3$$</p>


```python
def vol(rad):
    pass
```


```python
# Check
vol(2)
```




    33.49333333333333



____
**Schrijf een functie die controleert of een getal binnen een bepaald bereik valt (inclusief hoog en laag)**


```python
def ran_check(num,low,high):
    pass
```


```python
# Controleren
ran_check(5,2,7)
```

    5 is in the range between 2 and 7
    

Als je alleen een boolean wilt retourneren:


```python
def ran_bool(num,low,high):
    pass
```


```python
ran_bool(3,1,10)
```




    True



____
**Schrijf een Python-functie die een string accepteert en het aantal hoofdletters en kleine letters berekent.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

HINT: Twee string-methoden die nuttig kunnen zijn: **.isupper()** en **.islower()**

Als je ambitieus bent, verken dan de module Collecties om dit probleem op te lossen!


```python
def up_low(s):
    pass
```


```python
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
```

    Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
    No. of Upper case characters :  4
    No. of Lower case Characters :  33
    

____
**Schrijf een Python-functie die een lijst nodig heeft en een nieuwe lijst retourneert met unieke elementen van de eerste lijst.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]


```python
def unique_list(lst):
    pass
```


```python
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
```




    [1, 2, 3, 4, 5]



____
**Schrijf een Python-functie om alle getallen in een lijst te vermenigvuldigen (multiply).**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24


```python
def multiply(numbers):  
    pass
```


```python
multiply([1,2,3,-4])
```




    -24




____
**Schrijf een Python-functie die controleert of een woord of zin palindroom is of niet.**

Opmerking: een palindroom is een woord, zin of reeks die achterstevoren hetzelfde leest als vooruit, bijvoorbeeld "madam", "kayak", "racecar" of een zinsnede "nurses run". Hint: misschien wil je de methode .replace() in een string bekijken om te helpen bij het omgaan met spaties. Zoek ook op Google hoe u een string in Python kunt omkeren, er zijn enkele slimme manieren om dit te doen met slicing-notatie.


```python
def palindrome(s):
    pass
```


```python
palindrome('helleh')
```




    True



____
#### Moeilijk:

**Schrijf een Python-functie om te controleren of een string pangram is of niet. (Stel dat de ingevoerde tekenreeks geen leestekens/punctuation heeft)**

     Let op: Pangrammen zijn woorden of zinnen die elke letter van het alfabet minstens één keer bevatten.
     Bijvoorbeeld: "The quick brown fox jumps over the lazy dog"

Hint: misschien wilt u de methode .replace() gebruiken om spaties te verwijderen.

Hint: kijk naar de [string-module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)

Hint: als je [set-vergelijkingen](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41) wilt gebruiken


```python
import string

def is_pangram(str1, alphabet=string.ascii_lowercase):
    pass
```


```python
is_pangram("The quick brown fox jumps over the lazy dog")
```


```python
string.ascii_lowercase
```




    'abcdefghijklmnopqrstuvwxyz'



#### Veel succes!
