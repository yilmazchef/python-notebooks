<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python course materials</em>
</center>

# Errors and Exceptions Homework - Solution

### Problem 1
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.


```python
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")
```

    An error occurred!
    

### Problem 2
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'


```python
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')
```

    Can't divide by Zero!
    All Done!
    

### Problem 3
Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.


```python
def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)
```


```python
ask()
```

    Input an integer: null
    An error occurred! Please try again!
    Input an integer: 2
    Thank you, your number squared is:  4
    

# Great Job!
