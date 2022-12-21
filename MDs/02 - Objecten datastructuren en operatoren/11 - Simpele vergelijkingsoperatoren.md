<center>
    <img src='https://www.intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em><br/>
    <em> Yilmaz Mustafa, Instructeur Java/Python</em>
</center>


# Vergelijkingsoperatoren

In deze lezing zullen we leren over de vergelijkingsoperatoren (Comparison Operators) in Python. Met deze operatoren kunnen we variabelen vergelijken en een Booleaanse waarde (True of False) uitvoeren.

Als je enige achtergrond in wiskunde hebt, zouden deze operators heel eenvoudig moeten zijn.

We zullen eerst een tabel met vergelijkingsoperatoren presenteren en daarna enkele voorbeelden doornemen:

<h2> Tabel met vergelijkingsoperatoren </h2><p> In de onderstaande tabel, a=3 en b=4.</p>

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Beschrijving</th><th>Voorbeeld</th>
</tr>
<tr>
<td>==</td>
<td>Als de waarden van twee operanden gelijk zijn, wordt de voorwaarde waar.</td>
<td> (a == b) is niet waar.</td>
</tr>
<tr>
<td>!=</td>
<td>Als de waarden van twee operanden niet gelijk zijn, wordt de voorwaarde waar.</td>
<td>(a != b) is waar</td>
</tr>
<tr>
<td>&gt;</td>
<td>Als de waarde van de linker operand groter is dan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &gt; b) is niet waar.</td>
</tr>
<tr>
<td>&lt;</td>
<td>Als de waarde van de linker operand kleiner is dan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &lt; b) is waar.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>Als de waarde van de linker operand groter is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &gt;= b) is niet waar. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>Als de waarde van de linker operand kleiner is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &lt;= b) is waar. </td>
</tr>
</table>


Laten we nu snelle voorbeelden van elk van deze doornemen.

#### Gelijk



```python
2 == 2

a = 10
b = 10

a == b

first_name = "John"
last_name = "Doe"

print(first_name == "John" and last_name == "Doe")

print(first_name == "John" or last_name == "Koe")

gender = 'M'
age = 18

print(gender == 'M' and age >= 18)

print(gender == 'M' or age > 55)

print(gender == 'M' and age > 55)

volvo_xc90 = 55000

budget = 30000
country = "BE"

can_you_buy_this_car = budget >= volvo_xc90 and country == "BE"

can_you_buy_this_card = budget < 20000 or country == "BE"

rich = True
charisma = False

marry_victoria_secret_model = rich or charisma

marry_victoria_secret_model = rich and charisma

marry_victoria_secret_model = not rich and not charisma

```




    True




```python
print(not (1 == 1))

print(not (1 == 2))

bad_words = ["stupid", "no IQ", "no HQ"]

print("stupid" not in bad_words)

# "keyword" not in list
# paragraph

```

    False
    True
    False
    


```python

p = "I want to meet with her but she seems so genius!."

# convert this p to a list/set/tuple of words

plist = p.split()

print(plist)

print("stupid" not in plist)

```

    ['I', 'want', 'to', 'meet', 'with', 'her', 'but', 'she', 'seems', 'so', 'genius!.']
    True
    True
    


```python

print(5 in [1, 2, 3, 4, 5])

print("hello" in ["john", "hello", "whats up?"])

print("hello" in "hello world")

print("john" in "hey mary how do you do?")

```

    True
    True
    True
    False
    


```python

ip_address = "192.168.1.23"

ip_address_list = [
    "192.168.1.1",
    "192.168.1.23",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5",
    "192.168.1.99"
]

print(ip_address in ip_address_list)

```

    True
    


```python
x = 10
y = 20

# if -> sleutelewoord (keyword) is TRUE
#       dan voer de volgende code uit
# elif -> else if (sleutelewoord) is TRUE
#       dan voer de volgende code uit
# else -> anders (sleutelewoord) is TRUE
#       dan voer de volgende code uit

if(False):
    print("x is groter dan y")
    print("2de lijn voor if statement")
    print("3de lijn voor if statement")
else:
    print("x is kleiner dan y")
    print("2de lijn voor else statement")
    print("3rde lijn voor else statement")

```

    x is kleiner dan y
    2de lijn voor else statement
    3rde lijn voor else statement
    


```python
age = 20
cash = 30

if( age >= 18 and cash >= 1000 ):
    print("welcome to the casino")
    cash = -1000
    print("Go home boi!")
elif ( age < 18 ):
    print("Come on boi, go home!")
elif ( cash < 1000 ):
    print("You poor! What are you doing here?")
    
# else:
    # print("Dono why but boss doesn't want you here!")
```

    You poor! What are you doing here?
    


```python
weather = "sunny"
choice = "football"

if(weather == "sunny"):
    print("Go outside!")
    if(choice == "Barbecue"):
        print("Stay at the backyard!")
else:
    print("Stay at home!")
```

    Go outside!
    


```python
# if (condition):
#    instruction 1
#    instruction 2
#    instruction 3
# else:
#    instruction 1
#    instruction 2

```


```python
# read the input from the user
# ask the user for his/her year of birth

yob = input("What is your year of birth? ")
# yob = "1986" (string)
yob = int(yob)
# yob = 1986 (integer)

age = 2022 - yob

# if the user is older than 18
#   print "you are allowed to vote"
if (age >= 18):
    print("you are allowed to vote")
# if the user is younger than 18
#   print "you are not allowed to vote"
else:
    print("you are not allowed to vote")
    
print("this should always be printed")


```

    you are not allowed to vote
    this should always be printed
    


```python
1 == 0

```




    False



Merk op dat <code>==</code> (dubbele gelijk symbolen) een <em>vergelijkings</em>-operator is, terwijl <code>=</code> (enkel gelijk symbol) een <em>toewijzings</em>-operator is.


#### Niet gelijk



```python
2 != 1

```




    True




```python
2 != 2

```




    False



#### Groter dan



```python
2 > 1

```




    True




```python
2 > 4

```




    False



#### Kleiner dan



```python
2 < 4

```




    True




```python
2 < 1

```




    False



#### Groter dan of gelijk aan



```python
2 >= 2

```




    True




```python
2 >= 1

```




    True



#### Kleiner dan of gelijk aan



```python
2 <= 2

```




    True




```python
2 <= 4

```




    True




```python
if(1 == 1):
    print("this line is printed because 1 == 1 is True")

print("this line is always printed")

if(1 == 0):
    print("this line is always printed")
    
print("this line is always printed")
```

**Geweldig! Overloop elke vergelijkingsoperator om er zeker van te zijn dat u begrijpt wat elke operator zegt. Maar hopelijk was dit duidelijk voor u.**

Vervolgens behandelen we geketende (chained) vergelijkingsoperatoren

