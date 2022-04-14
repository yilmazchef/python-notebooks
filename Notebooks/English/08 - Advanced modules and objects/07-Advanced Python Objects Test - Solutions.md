<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python course materials</em>
</center>

# Advanced Python Objects Test

## Advanced Numbers

**Problem 1: Convert 1024 to binary and hexadecimal representation**


```python
print(bin(1024))
print(hex(1024))
```

    0b10000000000
    0x400
    

**Problem 2: Round 5.23222 to two decimal places**


```python
round(5.23222,2)
```




    5.23



## Advanced Strings
**Problem 3: Check if every letter in the string s is lower case**


```python
s = 'hello how are you Mary, are you feeling okay?'

s.islower()
```




    False



**Problem 4: How many times does the letter 'w' show up in the string below?**


```python
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count('w')
```




    12



## Advanced 
**Problem 5: Find the elements in set1 that are not in set2:**


```python
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)
```




    {2}



**Problem 6: Find all elements that are in either set:**


```python
set1.union(set2)
```




    {1, 2, 3, 5, 6, 7, 8}



## Advanced Dictionaries

**Problem 7: Create this dictionary:
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
 using a dictionary comprehension.**


```python
{x:x**3 for x in range(5)}
```




    {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}



## Advanced Lists

**Problem 8: Reverse the list below:**


```python
list1 = [1,2,3,4]

list1.reverse()

list1
```




    [4, 3, 2, 1]



**Problem 9: Sort the list below:**


```python
list2 = [3,4,2,5,1]

list2.sort()

list2
```




    [1, 2, 3, 4, 5]



# Great Job!
