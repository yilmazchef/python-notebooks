<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python course materials</em>
</center>

# Errors and Exceptions Homework

### Problem 1
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.


```python
for i in ['a','b','c']:
    print(i**2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-c35f41ad7311> in <module>()
          1 for i in ['a','b','c']:
    ----> 2     print(i**2)
    

    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


### Problem 2
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'


```python
x = 5
y = 0

z = x/y
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-2-6f985c4c80dd> in <module>()
          2 y = 0
          3 
    ----> 4 z = x/y
    

    ZeroDivisionError: division by zero


### Problem 3
Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.


```python
def ask():
    pass
```


```python
ask()
```

    Input an integer: null
    An error occurred! Please try again!
    Input an integer: 2
    Thank you, your number squared is:  4
    

# Great Job!
