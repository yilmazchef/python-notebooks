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
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
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
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
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



#### MAKES TWENTY: Gegeven twee gehele getallen, retourneer True als de som van de gehele getallen 20 is *of* als een van de gehele getallen 20 is. Zo niet, retourneer False

    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False


```python
def makes_twenty(n1,n2):
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



# NIVEAU 1 PROBLEMEN

#### OLD MACDONALD: Schrijf een functie die de eerste en vierde letter van een naam als hoofdletter gebruikt
     
    old_macdonald('macdonald') --> MacDonald
    
Note: `'macdonald'.capitalize()` retourneert `'Macdonald'`


```python
def old_macdonald(name):
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
def master_yoda(text):
    return ' '.join(text.split()[::-1])
```


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



#### BIJNA ER: Gegeven een geheel getal n, retourneer True als n binnen 10 van 100 of 200 ligt

    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    
OPMERKING: `abs(num)` geeft de absolute waarde van een getal


```python
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
```


```python
# Controleren
almost_there(90)
```




    True




```python
# Controleren
almost_there(104)
```




    True




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



BONUS: Here's a faster version that makes use of the prime numbers we're collecting as we go!


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
