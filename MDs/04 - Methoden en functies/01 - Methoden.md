<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Methoden en functies

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
lst = [1,2,3,4,5,6,7,8,9,10]
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

Geweldig! Hoe zit het nu met tellen ()? De methode count() telt het aantal keren dat een element in een lijst voorkomt.


```python
# Controleer hoe vaak 2 in de lijst voorkomt
lst.count(2)
```

U kunt altijd Shift+Tab gebruiken in Jupyter Notebook om meer hulp over de methode te krijgen. In Python kun je in het algemeen de help() functie gebruiken:


```python
help(lst.count)
```


```python
numbers = [1, 3, 5, 3, 3]

numbers.append(5)

print(numbers)

print(numbers.count(5))
print(numbers.count(3))

```


```python
shakespeare_quotes = [
    "To be or not to be", 
    "That is the question", 
    "Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune",
    "Or to take arms against a sea of troubles",
    "And by opposing end them",
    "To die, to sleep, no more; and by a sleep to say we end the heart-ache and the thousand natural shocks that flesh is heir to",
]

# print(shakespeare_quotes)

#for quote in shakespeare_quotes:
    #print(quote.split().count("to"))
    #print(len(quote.split()))
    
print(max(shakespeare_quotes))
```


```python
# get the max length of the quotes
max_length = 0

for quote in shakespeare_quotes:
    if len(quote.split()) > max_length:
        max_length = len(quote.split()) 
```


```python
names = ["John", "Jane", "Jack", "Jill", "Joe"]

print(names)

print(names.count("John"))

print(names.count("Jo"))
```


```python
lorem_ipsum = """
Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:

“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.

The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
"""

print(lorem_ipsum)

def count_words(text):
    words = text.split()
    return len(words)

def search_words(text, word):
    words = text.split()
    return words.count(word)

def remove_words(text, word):
    words = text.split()
    while word in words:
        words.remove(word)
    return " ".join(words)
```


```python
s = "Hello World"

# test all string methods
print(s.split())
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.replace("World", "Python"))
print(s.startswith("Hello"))
print(s.endswith("World"))
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
```

    ['Hello', 'World']
    HELLO WORLD
    hello world
    Hello World
    Hello world
    hELLO wORLD
    Hello Python
    True
    True
    False
    False
    False
    

Voel je vrij om te spelen met de rest van de methoden voor een lijst. Verderop in dit gedeelte zal je quiz gebruik maken van help en Google zoeken naar methoden voor verschillende soorten objecten!

Geweldig! Door deze lezing zou je je op je gemak moeten voelen bij het aanroepen van methoden van objecten in Python!
