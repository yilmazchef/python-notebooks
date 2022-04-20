<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Variabele Toewijzing (Assignments)

## Regels voor namen van variabelen (Naamgevingsconventies)

* namen mogen niet beginnen met een cijfer
* namen mogen geen spaties bevatten, gebruik _ intead
* namen mogen geen van deze symbolen bevatten:

       :'",<>/?|\!@#%^&*~-+

* het wordt als de beste praktijk beschouwd ([PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)) dat namen in kleine letters met underscores zijn
* vermijd het gebruik van ingebouwde Python-sleutelwoorden zoals `list` en `str`
* vermijd het gebruik van de enkele karakters `l` (kleine letter l), `O` (hoofdletter o) en `I` (hoofdletter i), aangezien deze kunnen worden verward met `1` en `0`

## Dynamisch typen

Python gebruikt *dynamisch typen*, wat betekent dat je variabelen opnieuw kunt toewijzen aan verschillende gegevenstypen. Dit maakt Python erg flexibel in het toewijzen van datatypes; het verschilt van andere talen die *statisch getypt* zijn.

```python
my_dogs = 2
```

```python
my_dogs
```

    2

```python
my_dogs = ['Sammy', 'Frankie']
```

```python
my_dogs
```

    ['Sammy', 'Frankie']

### Voor- en nadelen van dynamisch typen

#### Voordelen van dynamisch typen

* zeer gemakkelijk om mee te werken
* snellere ontwikkeltijd

#### Nadelen van dynamisch typen

* kan leiden tot onverwachte bugs!
* je moet op de hoogte zijn van `type()`

## Variabelen toewijzen

Variabele toewijzing volgt `naam = object`, waarbij een enkel gelijkteken `=` een *toewijzingsoperator* is

```python
a = 5
```

```python
a
```

    5

Hier hebben we het integer-object `5` toegewezen aan de variabelenaam `a`.<br>Laten we `a` aan iets anders toewijzen:

```python
a = 10
```

```python
a
```

    10

U kunt nu `a` gebruiken in plaats van het getal `10`:

```python
a + a
```

    20

## Variabelen opnieuw toewijzen

Met Python kun je variabelen opnieuw toewijzen met een verwijzing naar hetzelfde object.

```python
a = a + 10
```

```python
a
```

    20

Hier is een snelkoppeling voor. Met Python kun je getallen optellen, aftrekken, vermenigvuldigen en delen door ze opnieuw toe te wijzen met behulp van `+=`, `-=`, `*=` en `/=`.

```python
a += 10
```

```python
a
```

    30

```python
a *= 2
```

```python
a
```

    60

## Variabel type bepalen met `type()`

U kunt controleren welk type object aan een variabele is toegewezen met behulp van de ingebouwde functie `type()` van Python. Veel voorkomende gegevenstypen zijn:

* **int** (voor integer)
* **float**
* **str** (voor string)
* **list**
* **tuple**
* **dict** (voor dictionary)
* **set**
* **bool** (voor Boolean True/False)

```python
type(a)
```

    int

```python
a = (1,2)
```

```python
type(a)
```

    tuple

## Eenvoudige oefening

Dit laat zien hoe variabelen berekeningen leesbaarder en gemakkelijker te volgen maken.

```python
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
```

```python
my_taxes
```

    10.0

Geweldig! U zou nu de basisprincipes van het toewijzen en opnieuw toewijzen van variabelen in Python moeten begrijpen.
