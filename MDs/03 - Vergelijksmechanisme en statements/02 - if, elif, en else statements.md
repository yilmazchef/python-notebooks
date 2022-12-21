<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# if, elif, else Verklaringen

<code>if</code>-statements in Python stellen ons in staat om de computer te vertellen alternatieve acties uit te voeren op basis van een bepaalde reeks (een of meerdere) resultaten.

Verbaal kunnen we ons voorstellen dat we tegen de computer zeggen:

"Hé, als dit geval zich voordoet, voer dan een actie/instructie uit"

We kunnen het idee dan verder uitbreiden met <code>elif</code> en <code>else</code> statements, waarmee we de computer kunnen vertellen:

"Hé, als dit geval zich voordoet, voer dan een actie uit. Anders, als een ander geval zich voordoet, voer dan een andere actie uit. Anders, als *geen* van de bovenstaande gevallen is gebeurd, voer dan deze actie uit."

Laten we eens kijken naar de syntaxisindeling voor <code>if</code>-statements om hier een beter idee van te krijgen:

    if case1:
        perform action1
    elif case2:
        perform action2
    else: 
        perform action3

## Eerste voorbeeld

Laten we een snel voorbeeld hiervan bekijken:


```python
if True:
    print('It was true!')
```

    It was true!
    

Laten we nog andere logica toevoegen:


```python
x = False

if x:
    print('x was True!')
else:
    print('I will be printed in any case where x is not true')
```

    I will be printed in any case where x is not true
    

### Meerdere vestigingen (branches)

Laten we een vollediger beeld krijgen van hoe ver <code>if</code>, <code>elif</code> en <code>else</code> ons kunnen brengen!

We schrijven dit uit in een geneste structuur. Let op hoe de <code>if</code>, <code>elif</code> en <code>else</code> op één lijn liggen in de code. Dit kan je helpen te zien wat <code>if</code> is gerelateerd aan wat <code>elif</code> of <code>else</code>-statements.

We zullen een vergelijking-syntaxis voor Python opnieuw introduceren.


```python
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')
```

    Welcome to the bank!
    

Merk op hoe de geneste <code>if</code>-instructies elk worden gecontroleerd totdat een True-boolean ervoor zorgt dat de geneste code eronder wordt uitgevoerd. 
Houd er ook rekening mee dat u zoveel <code>elif</code>-statements kunt invoeren als u wilt voordat u afsluit met een <code>else</code>.

Laten we nog twee eenvoudige voorbeelden maken voor de instructies <code>if</code>, <code>elif</code> en <code>else</code>:


```python
person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")
```

    Welcome Sammy!
    


```python
person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")
```

    Welcome George!
    

## Inspringing (Indentation)

Het is belangrijk om goed te begrijpen hoe inspringen in Python werkt om de structuur en volgorde van uw code te behouden. We zullen dit onderwerp opnieuw bespreken wanneer we beginnen met het bouwen van functies!
