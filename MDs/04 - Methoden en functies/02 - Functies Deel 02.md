# Functies Deel 02


### Een stuk code dat geresued kan worden.
Inleiding tot functies

Wat is een functie in Python en hoe maak je een functie?

Functies zullen een van onze belangrijkste bouwstenen zijn wanneer we steeds grotere hoeveelheden code bouwen om problemen op te lossen.

Dus wat is een functie?

Een functie groepeert een reeks beweringen om de beweringen meer dan eens uit te voeren. We kunnen parameters opgeven die als invoer voor de functies kunnen dienen.

Functies stellen ons in staat de code te hergebruiken in plaats van deze steeds opnieuw te schrijven. Als je je strings en lijsten herinnert, herinner je je dat de functie len() wordt gebruikt om de lengte van een string te vinden. Aangezien het controleren van de lengte van een reeks een veelvoorkomende taak is, zou je een functie willen schrijven die dit herhaaldelijk kan doen op commando.

Functie is een van de meest elementaire niveaus van hergebruik van code in Python, en het laat ons ook toe om na te denken over het ontwerp van programma's.




```python
len
```




    <function len(obj, /)>




```python
type(len)
```




    builtin_function_or_method




```python
num_letters = len("four")
print(num_letters)
```

    4
    


```python
l=[3,4,5,6]
x=l.pop ()
print (x)
print(l)
```

    6
    [3, 4, 5]
    

### def Statements

Laten we nu leren hoe we een functie bouwen en wat de syntaxis in Python is.

De syntaxis voor def statements is in de volgende vorm:


```python
def subject():
    print( "python class")
    print ("I Am learning python")
print ("I am after function")
```

    I am after function
    


```python
def subject():
    print( "python class")
    print ("I Am learning python")
subject()
```

    python class
    I Am learning python
    


```python
subject()
subject()
subject()
subject()
```

    python class
    I Am learning python
    python class
    I Am learning python
    python class
    I Am learning python
    python class
    I Am learning python
    


```python
def python_subject():
    print( "python class")
    print ("I Am learning python")

print ("I am before function")
print("python_subject")
python_subject()# function call
print ("I am after function")
```

    I am before function
    python_subject
    python class
    I Am learning python
    I am after function
    


```python
python_subject()
```

    python class
    I Am learning python
    


```python
python_subject()
python_subject()
```

    python class
    I Am learning python
    python class
    I Am learning python
    


```python
def java_subject():
    print( "Java class")
    print ("I Am learning Java")
java_subject()
```

    Java class
    I Am learning Java
    


```python
def printsubject(name):
    print (" I am learning " ,name)
```


```python
printsubject("python")
```

     I am learning  python
    


```python
printsubject("java")
printsubject("JavaScript")
printsubject("scala")
printsubject(1000)
```

     I am learning  java
     I am learning  JavaScript
     I am learning  scala
     I am learning  1000
    


```python
x=input("enter subject name :")
printsubject(x)
```

    enter subject name :data science
     I am learning  data science
    


```python
def printrevevrsesubject(name):
	print (name[::-1])
```


```python
printrevevrsesubject("python")
```

    nohtyp
    


```python
printrevevrsesubject("javaScript")
```

    tpircSavaj
    


```python
printrevevrsesubject("java")
```

    avaj
    


```python
x=input("enter string ")
printrevevrsesubject(x)
```

    enter string machine learning
    gninrael enihcam
    


```python
def detail(age,name):
    print (age,name)
```


```python
detail("richard",20)
```

    richard 20
    


```python
def demofunction():
    """This function is for demo purpose
    This function is anotehr line for demo purpose"""# docstring

    print ("demo ")
    # this is to demo comments comments are writtern using #
```


```python
help(demofunction)
```

    Help on function demofunction in module __main__:
    
    demofunction()
        This function is for demo purpose
        This function is anotehr line for demo purpose
    
    


```python
demofunction()
```

    demo 
    


```python
def increasesalary(salary):
    newsalary=salary*1.10
    print ("Revised salary ",newsalary)
```


```python
increasesalary(100)
```

    Revised salary  110.00000000000001
    


```python
bonus=2*newsalary/100
print (" Bonus is : ", bonus)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-170-9fa61237a567> in <module>
    ----> 1 bonus=2*newsalary/100
          2 print (" Bonus is : ", bonus)
    

    NameError: name 'newsalary' is not defined



```python
def increasesalary(salary):
    newsalary=salary*1.10
    print ("Revised salary ",newsalary)
    return newsalary
x=increasesalary(200)
print (x)
bonus=2*x/100
print (" Bonus is : ", bonus)
```

    Revised salary  220.00000000000003
    220.00000000000003
     Bonus is :  4.4
    


```python
def calculatearea(base,height):
	area=base*height
	print ("inside the function area: " ,area)
	return area
x=calculatearea(10,20)
print (x)
print (type(x))
```

    inside the function area:  200
    200
    <class 'int'>
    

### Default Argument

Standaardargument: Python staat toe een functie aan te roepen door een minimum aan mogelijke argumenten op te geven. 
In dergelijke gevallen kent de functie een standaardwaarde toe die geen overeenkomend argument heeft in de functieaanroep.
Standaardwaarden worden gespecificeerd wanneer de functie wordt gedeclareerd. 

De compiler kijkt naar het prototype om te zien hoeveel argumenten een functie gebruikt en waarschuwt het programma voor mogelijke standaardwaarden.

Standaardwaarden worden gespecificeerd van rechts --> naar links in de argumentenlijst.



```python
def calculatearea(base=20,height=100):
	area=base*height/2
	print (area)
   
# def calculatearea():
#     print(" i am in 3 parameter")
#     area=base*height/2
#     print(area)
calculatearea()
# calculatearea(base=2,height=1)
```

    1000.0
    


```python
def calculatearea(base=20,height=100):
	area=base*height/2
	print(area)
```


```python
calculatearea()
```

    1000.0
    


```python
calculatearea(height=5)
```

    50.0
    


```python
calculatearea(4,5)
```

    10.0
    


```python
calculatearea(4)
```

    200.0
    


```python
calculatearea(base=5)
```

    250.0
    


```python
def parrot(voltage, state='a stiff', action='voom', parrottype='Norwegian Blue'):
    print ("-- This parrot wouldn't", action)
    print ("--if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", parrottype)
    print ("-- It's", state, "!")
```


```python
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

    -- This parrot wouldn't voom
    --if you put a thousand volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's pushing up the daisies !
    


```python
parrot('a million', 'bereft of life', 'jump')     # 3 positional arguments
```

    -- This parrot wouldn't jump
    --if you put a million volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's bereft of life !
    


```python
parrot( 'a million','bereft of life',state='jump')     # 3 positional arguments
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-204-5f78f9bec76d> in <module>
    ----> 1 parrot( 'a million','bereft of life',state='jump')     # 3 positional arguments
    

    TypeError: parrot() got multiple values for argument 'state'



```python
parrot(1000,'',"wet")# 1 positional argument
```

# UnPacking of data


```python
d={}
type(d)
```




    dict




```python
d ={}
d['name']='Rakesh'
d['age'] = 20
d['subject']="java"
d["level"]="beginner"
d["second_subject"]= "python"
# d['extra_subject']="java"
d
```




    {'name': 'Rakesh',
     'age': 20,
     'subject': 'java',
     'level': 'beginner',
     'second_subject': 'python'}




```python
def varlength(mclass,age,name,subject,second_subject,level):
	print( name,age,subject,level,second_subject)
```


```python
varlength("java",**d)
# print(d)
```

    Rakesh 20 java beginner python
    


```python
# def varlength(name,age,level,subject,second_subject,mclass):
# 	print( name,mclass,age,level)
# d ={}
# d['name']='Rakesh'
# d['age'] = 20
# d['subject']="java"
# d["level"]="beginner"
# d["second_subject"]= "python"
# d['extra_subject']="java"
# d
# varlength(**d, mclass="school")

```


```python
- Dictionary should be last parameter in function call
- If you want to pass dictionary before anoter parameter , another parameter should be key value pair
- If you want to have default paramter in function definition it should be after dictionary keys
```


```python
def varlength(mclass,name,age,level,subject,second_subject):
    print( name,mclass,age,level)
    print(subject)
d ={}
d['name']='Rakesh'
d['age'] = 20
d['subject']="java"
d["level"]="beginner"
d["second_subject"]= "python"
varlength(**d, mclass="school")
```


```python
def varlength(name,age,level,subject,second_subject,mclass="java"):
    print( name,mclass,age,level)
    print(subject)
d ={}
d['name']='Rakesh'
d['age'] = 20
d['subject']="java"
d["level"]="beginner"
d["second_subject"]= "python"
varlength(**d)
```

    Rakesh java 20 beginner
    java
    


```python
def varlength(mclass,name,age,level,subject,second_subject):
    print( name,mclass,age,level)
    print(subject)
d ={}
d['name']='Rakesh'
d['age'] = 20
d['subject']="java"
d["level"]="beginner"
d["second_subject"]= "python"

```


```python
varlength("school",**d)
```

    Rakesh school 20 beginner
    java
    


```python
def moreVarLen(f,h):
    print(f)
    print(h)
```


```python
d = ('abc','def')
moreVarLen(*d)
```

    abc
    def
    


```python
def moreVarLen(x,y,z):
    print (x,y)
    print(z)
d = ['abc','def']
moreVarLen("python",*d)
```

    python abc
    def
    


```python
def moreVarLen(x,y,z):
    print (x,y)
    print(z)
d = ['abc','def']
moreVarLen("java",*d)
```

    java abc
    def
    


```python
def moreVarLen(x,y,z):
    print (x,y)
    print(z)
d = ['abc','def']
moreVarLen(*d,"java")
```

    abc def
    java
    


```python
def moreVarLen(x,y,z):
    print (x,y)
    print(z)
d=['abc',[12,11,123]]
moreVarLen("java",*d)
```

    java abc
    [12, 11, 123]
    


```python
def moreVarLen(x,y,name,age):
    print(x,y,name,age)    
# 	print( " %s, %s , %s , %d" %(x,y,name,age))
```


```python
d1 ={}
d1['name']='Ashok'
d1['age'] = 20
l = ['abc','def']
moreVarLen(*l,**d1)
```

    abc def Ashok 20
    

## Packing of Data


```python
def revArgLen(**d):
    print (d)
    print(type(d))
```


```python
revArgLen(name='abc',age=20,subject="python")
```

    {'name': 'abc', 'age': 20, 'subject': 'python'}
    <class 'dict'>
    

## Verpakte gegevens zullen altijd Tuple of dictionary zijn


```python
def revArgLen(x,*t):
	print (t)
	print (type(t))
```


```python
revArgLen(234,33,"python","java","abc")
# revArgLen(234)
```

    (33, 'python', 'java', 'abc')
    <class 'tuple'>
    


```python
def revArgLen(x,y,z,x1,y1,z1):
	print (x,y,z,x1,y1,z1)
t=(1,2,3)
l=("a","b","c")
revArgLen(*t,*l)
```

    1 2 3 a b c
    


```python
def revArgLen(x,y):
	print (x,y)
t=(1,2,3)
# l=("a","b","c")
revArgLen((1,2,3),["x","y"])
```

    (1, 2, 3) ['x', 'y']
    

## Pass by Value /Reference
Het is noch pass-by-value noch pass-by-reference - het is call-by-object.



```python
def set_list(list): 
    print(id(list))
    list = ["A", "B", "C"] 
    print(id(list))
    return list
  
def add(list): 
    list.append("D") 
    print(id(list))
    return list
  
my_list = ["E"] 
print(set_list(my_list)) 
print(add(my_list))
print(my_list)
```

    1949475826560
    1949475823744
    ['A', 'B', 'C']
    1949475826560
    ['E', 'D']
    ['E', 'D']
    


```python
def clear_a(x):
  x += [1,2,2]


def clear_b(x):
  while x: x.pop()

z = [1,2,3]
clear_a(z) # z will not be changed
# print(z)
# clear_b(z) #
print(z)
```

    [1, 2, 3, 1, 2, 2]
    


```python
def append_one(li):
    li.append(1)
x = [0]
append_one(x)
print (x)
```

    [0, 1]
    

Hier maakt het statement x = [0] een variabele x (box) die naar het object [0] wijst.

Bij het aanroepen van de functie wordt een nieuwe box li gemaakt. De inhoud van li is dezelfde als die van box x. Beide vakjes bevatten hetzelfde object. Dat wil zeggen, beide variabelen wijzen naar hetzelfde object in het geheugen. Daarom zal elke verandering in het object waarnaar li verwijst ook worden weerspiegeld in het object waarnaar x verwijst.

Kortom, de uitvoer van het bovenstaande programma is:

[0, 1]

Opmerking:

Als de variabele li opnieuw wordt toegewezen in de functie, dan zal li naar een apart object in het geheugen wijzen. x zal echter blijven wijzen naar hetzelfde object in het geheugen waarnaar het eerder wees.


```python
def append_one(li):
    li = [0, 1]
x = [0]
append_one(x)
print (x)
```

    [0]
    

## Namespace


```python
a=100
def func():
    print(a)
func()
```

    100
    


```python
def func():
    b_func1=100
    print(b_func1)
func()
print(b_func1)
```

    100
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-255-5bc9acaca5b3> in <module>
          3     print(b_func1)
          4 func()
    ----> 5 print(b_func1)
    

    NameError: name 'b_func1' is not defined



```python
b="python"
def func():
    b=100
    print(b)
func()
```

    100
    


```python
a=5454
def revArgLen(d):
    a=d    # a= 234
    print ("insie of function d value " ,d)
    print (a)
    print(id(a))
revArgLen(234) 
print(id(a))
print(a)
```

    insie of function d value  234
    234
    140726194033728
    1949471122064
    5454
    


```python
a="python"
def revArgLen(d):
    print ("Inside function value of a inside func :",a)
    print (d)
    return a
x=revArgLen(234) 
print("Outside value of x :" ,x)
print("value of a outside function :",a)
```

    Inside function value of a inside func : python
    234
    Outside value of x : python
    value of a outside function : python
    


```python
a_var = 'global variable'
def a_func():
    print (a_var, '[ a_var inside a_func() ]')
a_func()
print (a_var, '[ a_var outside a_func() ]')
```

    global variable [ a_var inside a_func() ]
    global variable [ a_var outside a_func() ]
    


```python
a_var = 'global value'
def a_func():
    a_var = 'global value'
    print(id(a_var))
    print (a_var, '[ a_var inside a_func() ]')
a_func()
print (a_var, '[ a_var outside a_func() ]')
print(id(a_var))
```

    1949474347760
    global value [ a_var inside a_func() ]
    global value [ a_var outside a_func() ]
    1949474346032
    


```python
a="python"
```


```python
b_var = 'outside value'# inside value
# b_var = 'local value'
def b_func():
	global b_var
# 	b_var = 'inside value'
	print(b_var, '[ b_var inside a_func() ]')
print (b_var, '[ b_var outside a_func() ]')
b_func()
print(b_var, '[ b_var outside a_func() ]')
```

    outside value [ b_var outside a_func() ]
    outside value [ b_var inside a_func() ]
    outside value [ b_var outside a_func() ]
    


```python
a_var = 1
def a_func():
	global a_var
	a_var = a_var + 1
	print (a_var, '[ a_var inside a_func() ]')
print (a_var, '[ a_var outside a_func() ]')
a_func()
print (a_var, '[ a_var outside a_func() ]')
```

    1 [ a_var outside a_func() ]
    2 [ a_var inside a_func() ]
    2 [ a_var outside a_func() ]
    


```python
a_var = 'global value'
def outer():
#     inner="inside function"
    a_var = 'enclosed value'
    print (a_var)
    b_var="in outer"
    def inner():
        global a_var
        a_var = 'local value'
        print(a_var)
        print(b_var)

    inner()
outer()
print (a_var)
```

    enclosed value
    local value
    in outer
    local value
    


```python
from math import pi
a_var = 'global value'
def outer():
       a_var = 'local value'
       pi="#434"
       print ("pi value ",pi)
       print('outer before:', a_var)
       def inner():
           a_var = 'inner value'
           print('in inner():', a_var)
       inner()
       print("outer after:", a_var)
print (pi)
outer()
print("global:", a_var)
pi="#435"
print (pi)
```

    3.141592653589793
    pi value  #434
    outer before: local value
    in inner(): inner value
    outer after: local value
    global: global value
    #435
    

Python staat deze dubbelzinnigheid gelukkig niet toe. Het zal dus een fout geven, zoals we kunnen zien in het volgende voorbeeld:

def f():
    print(s)
    s = "I love London!"
    print(s)
 
s = "I love Paris!"
f()

Een variabele kan niet zowel lokaal als globaal zijn in een functie. Python besluit dus dat we een lokale variabele willen door de toewijzing aan s in f(), dus de eerste afdrukopdracht vóór de definitie van s geeft de bovenstaande foutmelding. Elke variabele die in een functie wordt gewijzigd of aangemaakt is lokaal, als hij niet als globale variabele is gedeclareerd. Om Python te vertellen dat we de globale variabele willen gebruiken, moeten we dit expliciet aangeven met het sleutelwoord "globaal", zoals te zien is in het volgende voorbeeld:

## Opdracht

Zet alle voorgaande opdrachten om in functie..... slechts één opdracht

1. Schrijf een functie genaamd kubus() met één getal als parameter en geef de waarde van dat getal, verheven tot de derde macht, terug. Test de functie door het resultaat weer te geven van het aanroepen van je kubus() functie op een paar verschillende getallen.

2. Schrijf een functie genaamd greet() die een stringparameter genaamd naam aanneemt en de tekst "Hallo <naam>!" weergeeft, waarbij <naam> is
vervangen door de waarde van de naamparameter.

Schrijf een script genaamd temperature.py dat twee functies definieert:

1. convert_cel_to_far() die één floatparameter neemt die graden Celsius voorstelt en een float teruggeeft die dezelfde temperatuur voorstelt
in graden Fahrenheit met behulp van de volgende formule: F = C * 9/5 + 32

2. convert_far_to_cel() die een floatparameter neemt die graden Fahrenheit voorstelt en een float teruggeeft die dezelfde temperatuur voorstelt
in graden Celsius met de volgende formule: C = (F - 32) * 5/9

Het script moet de gebruiker eerst vragen een temperatuur in graden Fahrenheit in te voeren en vervolgens de temperatuur omgerekend naar Celsius weergeven. Vervolgens moet de gebruiker een temperatuur in graden Celsius invoeren en de temperatuur omgerekend naar Fahrenheit weergeven. Alle omgerekende temperaturen moeten worden afgerond op 2 decimalen. Hier is een voorbeeld van het programma:

Voer een temperatuur in graden F in: 72
72 graden F = 22,22 graden C

Voer een temperatuur in graden C in: 37
37 graden C = 98,60 graden F


```python
def multiply(x, y):
    product = x * y
    return product
num = multiply(2, 4)
print(num)
```


```python
help(multiply)
```


```python
def multiply(x, y):
    """Return the product of two numbers x and y."""
    product = x * y
    return product
```


```python
# help(len)
help(multiply)
```

  /** <br/>
         * @memberof lib <br/>
         * @description This method sets the default audio language. <br/>
         * @param {String} lang Language to be set as default for audio <br/>
         * @returns {Boolean} true if success, false if not. <br/>
         */


```python
num = float(input("Enter a positive number: "))
while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))
```


```python
word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1
```


```python
x = "Hello World"
def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")
func()
print(f"Outside 'func', x has the value {x}")
```


```python
x = 5
def outer_func():
    y = 3
    def inner_func():
        z = x + y
        return z
    return inner_func()
#     return 8

outer_func()
```


```python
total = 0
def add_to_total(n):
    total=5
    total = total + n
    print(total)

add_to_total(5)
print(total)
```


```python
def test():
    return "python"

# x=calculatearea(10,20)
print (x1)
x1=test()#
```

Maak een functie manipulate_data die het volgende doet. 

- Accepteert als eerste parameter een string die de te gebruiken gegevensstructuur specificeert lijst, set of woordenboek. 
- Accepteert als tweede parameter de te manipuleren gegevens op basis van de gespecificeerde gegevensstructuur, bijvoorbeeld [1, 4, 9, 16, 25] voor een lijstgegevensstructuur. 

- geeft op basis van de eerste parameter het omgekeerde van een lijst terug of voegt de items "ANDELA", "TIA" en "AFRICA" toe aan de verzameling en geeft de resulterende verzameling terug geef de sleutels van een woordenboek terug. 

manipulate("lijst",[1,2,3])
