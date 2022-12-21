<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Functie Opdrachten met oplossingen

Problemen zijn gerangschikt in oplopende moeilijkheidsgraad:
* Opwarmen - deze kunnen worden opgelost met behulp van basisvergelijkingen en methoden
* Niveau 1 - dit kan betrekking hebben op als/dan voorwaardelijke uitspraken en eenvoudige methoden
* Niveau 2 - hiervoor kan het nodig zijn om reeksen te herhalen, meestal met lus
* Uitdagend - deze zullen wat creativiteit vergen om op te lossen

## OPWARMINGSSECTIE

#### LESS OF TWO EVENS: Schrijf een functie die het kleinste van twee gegeven getallen retourneert *als* beide getallen even zijn, maar de grotere retourneert als een of beide getallen oneven zijn

    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5


```python
a = 10
b = 20
c = 15

print( "Min of a,b,c is " + str(min(a,b,c)))

d = 99

print( "Max of a,b,c,d is " + str(max(a,b,c,d)))

numbers = [ 1, 5, 7, 20, 55, 22, 4 ]

print( "Min of numbers list is " + str(min(numbers)))
print( "Max of numbers list is " + str(max(numbers)))
```

    Min of a,b,c is 10
    Max of a,b,c,d is 99
    Min of numbers list is 1
    Max of numbers list is 55
    


```python
# als a = 6, b = 10 -> return min, 6
# als a = 5, b = 12 -> return max, 12

def lesser_of_two_evens(a,b):
    # if first number is even and the second number is even then return min
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    # else the first or the second number is odd then return max
    else:
        return max(a,b)
```


```python
# Controleren
lesser_of_two_evens(2,4)
```




    2




```python
# Controleren
lesser_of_two_evens(2,5)
```




    5



#### ANIMAL CRACKERS: Schrijf een functie neemt een string van twee woorden en retourneert True als beide woorden met dezelfde letter beginnen

    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False


```python
def animal_crackers(text):
    words = text.split()
    if(len(words) == 2):
        first_word = words[0]
        second_word = words[1]
        first_letter = first_word[0].lower()
        second_letter = second_word[0].lower()
        if first_letter == second_letter:
            return True
        else:
            return False
        

def animal_crackers_one_liner(text):
    return text.split()[0][0].lower() == text.split()[1][0].lower()
```


```python
# Controleren
animal_crackers('Levelheaded Llama')
```




    True




```python
# Controleren
animal_crackers('Crazy Kangaroo')
```




    False




```python
# Controleren
animal_crackers("Yilmaz yoo")
```




    True



#### MAKES TWENTY: Gegeven twee gehele getallen, retourneer True als de som van de gehele getallen 20 is *of* als een van de gehele getallen 20 is. Zo niet, retourneer False

    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False


```python
# a = 15, b = 5 -> return True
# a = 12, b = 33 -> return False
# a = 20, b = 4 -> return True
# a = 66, b = 20 -> return True

def makes_twenty(a,b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False

def makes_twenty_one_liner(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
```


```python
# Controleren
makes_twenty(20,10)
```




    True




```python
# Controleren
makes_twenty(12,8)
```




    True




```python
# Controleren
makes_twenty(2,3)
```




    False




```python
# Controleren
makes_twenty(4, 20)
```




    True



# NIVEAU 1 PROBLEMEN

#### OLD MACDONALD: Schrijf een functie die de eerste en vierde letter van een naam als hoofdletter gebruikt
     
    old_macdonald('macdonald') --> MacDonald
    
Note: `'macdonald'.capitalize()` retourneert `'Macdonald'`


```python
def old_macdonald(name):
    if len(name) > 3:
        # first letter
        # letters between first and fourth 
        # fourth letter
        # all other letters after fourth
        first_letter = name[0]
        # name[start:end:step]
        # MacDonald -> M -> 0, a -> 1, c -> 2, D -> 3
        all_letters_between_first_and_fourth = name[1:3]
        fourth_letter = name[3]
        all_letters_after_fourth = name[4:]
    
        return first_letter.upper() + all_letters_between_first_and_fourth + fourth_letter.upper() + all_letters_after_fourth
    else:
        return "Name is too short!"

def old_macdonald_shorter(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
```


```python
# Controleren
old_macdonald('macdonald')
```




    'MacDonald'




```python
old_macdonald("hey")
```




    'Name is too short!'




```python
old_macdonald("helloworld")
```




    'HelLoworld'




```python
no_of_chars_in_a_string = len("Hello World")
max_index_of_a_string = len("Hello World") - 1

print ( no_of_chars_in_a_string == max_index_of_a_string )
```

    False
    

#### MASTER YODA: Geef een zin terug met de woorden omgekeerd

    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    
Opmerking: de methode .join() kan hier handig zijn. Met de methode .join() kun je strings samenvoegen in een lijst met een connectorstring. Sommige toepassingen van de methode .join() zijn bijvoorbeeld:
    >>> "--".join(['a','b','c'])
    >>> 'a--b--c'

Dit betekent dat als je een lijst met woorden had die je weer in een zin wilde veranderen, je ze gewoon kon samenvoegen met een enkele spatie:

    >>> " ".join(['Hello','world'])
    >>> "Hello world"


```python
def m1():
    print("Hello")
    
def m2():
    return "Hello"

```


```python
m1()
```

    Hello
    


```python
type(m1()) # return_type
```

    Hello
    




    NoneType




```python
type("Hello") == type("World")
```




    True




```python
"Hello" == "World"
```




    False




```python
m2()
```




    'Hello'




```python
def list_to_string(words):
    separator = " "
    converted_text = separator.join(words)
    return converted_text

def master_yoda(text):
    # split the text into list of words
    words = text.split()
    # reverse the list
    words.reverse()
    # convert list of words to one sentenced string
    return list_to_string(words)

def master_yoda_one_liner(text):
    return ' '.join(text.split()[::-1])
```


```python
messages = [ "Hello", "World", "Yilmaz" ]
messages.reverse()

print(messages)
```

    ['Yilmaz', 'World', 'Hello']
    


```python
message = "Hello World"
message = message[::-1]

print(message)
```

    dlroW olleH
    


```python
# Controleren
master_yoda('I am home')
```




    'home am I'




```python
# Controleren
master_yoda('We are ready')
```




    'ready are We'




```python
# Controleren
master_yoda("How deep is your love?")
```




    'love? your is deep How'



#### BIJNA ER: Gegeven een geheel getal n, retourneer True als n binnen 10 van 100 of meer dan 200 ligt

    almost_there(90) --> True
    almost_there(104) --> False
    almost_there(150) --> False
    almost_there(209) --> True
    
OPMERKING: `abs(num)` geeft de absolute waarde van een getal


```python
def almost_there(n: int = 0):
    if abs(n) in range(10, 101) or abs(n) > 200:
        return True
    else:
        return False
```


```python
# def method_name( var1: type1, var2: type2)
def calc_sum(a: int = 0, b:int = 0):
    return a + b
```


```python
calc_sum(10.55, 22.6)
```




    33.150000000000006




```python
calc_sum("Hello", "World")
```




    'HelloWorld'




```python
calc_sum()
```




    0




```python
help(calc_sum)
```

    Help on function calc_sum in module __main__:
    
    calc_sum(a: int, b: int)
        # def method_name( var1: type1, var2: type2)
    
    


```python
def change_resolution(w: int = 1920, h: int = 1080):
    pass
```


```python
change_resolution(1024, 768)
```


```python
change_resolution()
```


```python
abs(99)

abs(99.5)

abs(-500)
```




    500




```python
# Controleren
almost_there(90)
```




    True




```python
# Controleren
almost_there(104)
```




    False




```python
# Controleren
almost_there(150)
```




    False




```python
# Controleren
almost_there(209)
```




    True



# NIVEAU 2 PROBLEMEN

#### VIND 33:

Gegeven een lijst met gehele getallen, retourneer True als de array ergens een 3 naast een 3 bevat.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False


```python
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False
```


```python
# Controleren
has_33([1, 3, 3])
```




    True




```python
# Controleren
has_33([1, 3, 1, 3])
```




    False




```python
# Controleren
has_33([3, 1, 3])
```




    False



#### PAPER DOLL: Geef een tekenreeks, retourneer een tekenreeks waarbij voor elk teken in het origineel drie tekens zijn

    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


```python
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
```


```python
# Controleren
paper_doll('Hello')
```




    'HHHeeellllllooo'




```python
# Controleren
paper_doll('Mississippi')
```




    'MMMiiissssssiiissssssiiippppppiii'



#### BLACKJACK: Gegeven drie gehele getallen tussen 1 en 11, als hun som kleiner is dan of gelijk is aan 21, retourneer dan hun som. Als hun som hoger is dan 21 *en* er een elf is, verlaag dan de totale som met 10. Ten slotte, als de som (zelfs na aanpassing) groter is dan 21, retourneert u 'BUST'

    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19


```python
def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
```


```python
# Controleren
blackjack(5,6,7)
```




    18




```python
# Controleren
blackjack(9,9,9)
```




    'BUST'




```python
# Controleren
blackjack(9,9,11)
```




    19



#### SUMMER OF '69:  Retourneer de som van de getallen in de array, behalve negeer secties van getallen die beginnen met een 6 en doorlopen tot de volgende 9 (elke 6 wordt gevolgd door ten minste één 9). Retourneer 0 voor geen getallen.
 
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14


```python
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
```


```python
# Controleren
summer_69([1, 3, 5])
```




    9




```python
# Controleren
summer_69([4, 5, 6, 7, 8, 9])
```




    9




```python
# Controleren
summer_69([2, 1, 6, 9, 11])
```




    14



# UITDAGENDE PROBLEMEN

#### SPY GAME: Schrijf een functie die een lijst met gehele getallen inneemt en True retourneert als deze 007 in de juiste volgorde bevat.

     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False



```python
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
```


```python
# Controleren
spy_game([1,2,4,0,0,7,5])
```




    True




```python
# Controleren
spy_game([1,0,2,4,0,5,7])
```




    True




```python
# Controleren
spy_game([1,7,2,0,4,5,0])
```




    False



#### COUNT PRIMES: Schrijf een functie die het *aantal* teruggeeft van priemgetallen die bestaan tot en met een bepaald getal.

    count_primes(100) --> 25

Volgens conventies zijn 0 en 1 geen priemgetallen.


```python
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
                
```


```python
# Controleren
count_primes(100)
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    




    25



BONUS: Here is er een snellere versie die verzameld primenummers.


```python
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
```


```python
count_primes2(100)
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    




    25



### Voor de lol:

#### PRINT BIG: Schrijf een functie die een enkele letter nodig heeft, en retourneert een 5x5 representatie van die letter

    print_big('a')
    
    out:   *  
          * *
         *****
         *   *
         *   *
         *   *

HINT: Overweeg om een dictionary te maken van mogelijke patronen en het alfabet toe te wijzen aan specifieke 5-regelige combinaties van patronen. <br>Voor deze oefening is het oké als je woordenboek stopt bij "E".


```python
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
```


```python
print_big('a')
```

      *  
     * * 
    *****
    *   *
    *   *
    

## Goed gedaan!
