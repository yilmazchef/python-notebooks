# Strings
Anything in "" or '' will be treated as string

"ptyhon"
"123"
'343434'
'%%%%%'


```python
s1="python"
print (type(s1))
print (s1)
```


```python
# print (dir(str))
print(dir("python"))
```


```python
print (help(str))
# print("help()")
```


```python
dir(__builtins__)
```
 str1 ="Python"
 P   y   t   h     o     n
 0   1   2   3     4     5
-6  -5  -4  -3    -2    -1

```python
str1 ="python"
print (str1[0])
```


```python
print (str1[1])
```


```python
print (str1[4])
```


```python
print (str1[-1])
```


```python
print (str1[-3])
```

#### Immutable data
Which we can not change , once initialized.
example: String
Mutable data which we can changed
example: List


```python
str1 ="Python"
print(str1[0])
str1[0] = "q"
print (str1)
```


```python
str1 ="Python"
str1="qython"
print (str1)
```
 SLICING
  P   y   t   h     o     n
  0   1   2   3     4     5
 -6  -5  -4  -3    -2    -1
st[m:n]
m is starting index
n is ending index-1( it will stop one element before the n) exclusive
Moves from left to right direction

```python
st="python"
st[0:5]
```


```python
st[1:4]
```


```python
st[0:3]
```


```python
st[2:4]
```


```python
st[:3]
```


```python
st[0:]
```


```python
st[:6]
```


```python
st[0:7]
```


```python
st[0:-1]
```


```python
st[0:-3]
```

> if you are using both index as negative indexes the starting index should be lesser than the ending index otherwise no output


```python

st[-6:-3]
# str1[3:2]
```


```python
st[-2:-6]
```


```python
st[-3:-1]
```


```python
st[-6:]
```


```python
st[2:-2]
```


```python
st[:-2]
```

| P  |  y |  t |  h | o  | n  |
| -- | -- | -- | -- | -- | -- |
|  0 |  1 |  2 |  3 |  4 |  5 |
| -6 | -5 | -4 | -3 | -2 | -1 |
| -- | -- | -- | -- | -- | -- |


```python
x=" i am learning python here "
print(x[0:12])
print(len(x))
```

# Steps

| A  | r  | g  |  e | n  | t  |  i | n  | a  |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
|  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |
| -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |


```python
st="Argentina"

```


```python
st[0:8:2]
```


```python
st[0:7:3]
```


```python
st[0:5:1]
```


```python
st[0:4:2]
```


```python
st[0:6:3]
```


```python
st[::0]
```


```python
st[0::2]
```
 A  r  g  e  n   t   i   n   a
 0  1  2  3  4   5   6   7   8
-9 -8 -7 -6 -5  -4  -3  -2  -1


```python
st[5:0:-1]
```

#  If step is negative the starting index should be greater than ending index
Right to left
left to right if step is negative


```python
st[5::-2]
```


```python
st[:0:-2]
```


```python
st[8::-2]
```


```python
st[::-2]
```


```python
st[::-1]
```


```python
st[-1:-8:-2]
```


```python
A  r  g  e  n   t   i   n   a
0  1  2  3  4   5   6   7   8
-9 -8 -7 -6 -5  -4  -3  -2  -1

```

s[m:n]
n is always exclusive
Left to right
if we use both negative starting index should be lesser than ending index

s[m:n:steps]
n is exclusive
if we give negative step starting index should be greater than ending index 
right to left

### STRING Functions


```python
s="python"
dir(s)
# dir("java")
```


```python
help(str)
```

As String is immutable whatever operation we perform on string , it will either return true false or it will return a new string


```python
str1 ="Python"
result=str1.startswith("P")# case sensitive language
print (result)
```

    True
    


```python
result=str1.startswith("p")# case sensitive language
print (result)
```

    False
    


```python
str1="python"
print (str1.endswith("py"))
```

    False
    


```python
result=str1.endswith("n")
print (result)
```

    True
    


```python
str1 ="Python"
str2=str1.center(50)
print(str2)
print (str1.ljust(50))
print (str1.rjust(50))
print (str1)
```

                          Python                      
    Python                                            
                                                Python
    Python
    


```python
str1 = "am i the person and flowr s row person"
# t= str1.partition('e')
print(str1.partition('and'))
# print (t)
```

    ('am i the person ', 'and', ' flowr s row person')
    


```python
print (str1.partition(' '))
```

    ('am', ' ', 'i the person and flowr s row person')
    


```python
str2= "i love python. i love sas"
print( str2.capitalize()) # Left to right 
print( str2.title())
```

    I love python. i love sas
    I Love Python. I Love Sas
    


```python
print( str2.capitalize().lower()) # Left to right 

```

    i love python. i love sas
    


```python
s=str2.upper()
print(s)
print(str2)
```

    I LOVE PYTHON. I LOVE SAS
    i love python. i love sas
    


```python
str2.lower()
```


```python
str1 = "am i the only one who loves the way i am"
x= str1.count("the")
print (x)
```

    2
    


```python
x= str1.count(" ")
print (x)
```

    10
    


```python
str1 = "am i the one only one who loves am the way i"
x= str1.find("am")
# x= str1.find("only")
print (x)
```

    0
    

# rfind will search from end , but the index returned is positive only not negative


```python
x= str1.rfind("am")
print (x)
```

    32
    


```python
len(str1)
```


```python
str1= "    ffasdfsdf  sdfsff   "
print (str1.strip())
print (str1.lstrip())
print (str1.rstrip())
# print ("python","python")
```

    ffasdfsdf  sdfsff
    ffasdfsdf  sdfsff   
        ffasdfsdf  sdfsff
    


```python
str1
```


```python
print (str1.rstrip())

help(str)
```


```python
st=" hello {}"
print(st)
```

     hello {}
    


```python
"hello {}".format("world")
```




    'hello world'




```python
st=" hello {}"
st2=st.format("world")
print (st2)
print(st)
```

     hello world
     hello {}
    


```python
st=" hello {}"
st.format("python")
```




    ' hello python'




```python
st = "hello {} {} ! how is {}"
```


```python
print(st.format("python","java","scala"))
print(st)
```

    hello python java ! how is scala
    hello {} {} ! how is {}
    


```python
st.format("Ram","Shayam")
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-165-de3f1009d18b> in <module>
    ----> 1 st.format("Ram","Shayam")
    

    IndexError: Replacement index 2 out of range for positional args tuple



```python
result=st.format("Shayam","Ram")
print (result)
```


```python
st = "hello {} ! how is {} hello {}  how {} hello {}  how {}  "
```


```python
result=st.format("Shayam","Ram","mohan","sohan", "ravi", "ashok")
print (result)

```

    hello Shayam ! how is Ram hello mohan  how sohan hello ravi  how ashok  
    


```python
name2="Ram"
st1 = "hello {name2} ! how is {name1}"
print (st1.format(name2="ram",name1="Shayamala"))
print (st1.format(name1="Ramala",name2="Shayamala"))
```

    hello ram ! how is Shayamala
    hello Shayamala ! how is Ramala
    


```python
st1 = "hello {a} ! how is {name2}"
print (st1.format(a=1,name2="Shayamala"))
print(st1)
```

    hello 1 ! how is Shayamala
    hello {a} ! how is {name2}
    

f-Strings: A New and Improved Way to Format Strings in Python
The good news is that f-strings are here to save the day. They slice! They dice! They make julienne fries! Okay, they do none of those things, but they do make formatting easier. They joined the party in Python 3.6. You can read all about it in PEP 498, which was written by Eric V. Smith in August of 2015.

Also called “formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the __format__ protocol. As always, the Python docs are your friend when you want to learn more.

Here are some of the ways f-strings can make your life easier.


```python
name = "Eric"
age = 74
print("Hello, {name}. You are {age}.")
```


```python
print(f"Hello, {name}. You are {age}.")
```


```python
st = "ahdg@shjd#skdsdj1 "
st1=st.replace('j','*******')
print (st1)
print(st)
```

isalnum - returns true if string is made of only numbers and characters
if any special character is there it will return the false


```python
st="python5@"
print (st.isalnum())# only numbers and charachter not speial character
```


```python
st="python5"
print (st.isalnum())
```


```python
"python".index('o')
```




    4



## Unpacking


```python
s = 'Hello'
a, b, c, d ,e= s#hello
print(a, b, c, d, e)
print(list(s))
```

ASSIGNMENT
1. check if it is perllindrome (NITIN)
2. print the  reverse half of a string (argentina.. negratina)
3. write a program to check if the string is startswith, endswith, capitalize


```python
s="python"
s[:int(len(s)/2):-1]
# s[:len(s)/2:-1]
```


```python

```
