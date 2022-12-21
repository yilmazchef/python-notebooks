# Samenvatting

Python, ontworpen door Guido van Rossum bij het CWI, is een veelgebruikte universele programmeertaal op hoog niveau geworden.

Vereisten:

Kennis van elke programmeertaal kan een pluspunt zijn.


# Interpreter en Compiler

We schrijven een computerprogramma meestal in een high-level taal. Een high-level taal is een taal die voor ons mensen begrijpelijk is. Het bevat woorden en zinnen uit de Engelse (of andere) taal. Maar een computer begrijpt geen high-level taal. Hij begrijpt alleen programma's geschreven in binaire 0's en 1's, de zogenaamde machinecode. Een programma geschreven in high-level taal wordt broncode genoemd. We moeten de broncode omzetten in machinecode en dit wordt gedaan door compilers en tolken. Een compiler of een interpreter is dus een programma dat programma's geschreven in high-level taal omzet in machinecode die de computer begrijpt.


# Gegevenstypes

Datatypes zijn niets anders dan variabelen die je gebruikt om ruimte in het geheugen te reserveren. Python-variabelen hebben geen expliciete verklaring nodig om geheugenruimte te reserveren. De declaratie gebeurt automatisch wanneer u een waarde aan een variabele toekent.


```python
# JAVA or C++
int a =10 #java or c++
String s="python"
s=10 # error 
```


```python
a=101
print (a)
a="python"
print(a)
# shift+ enter
```

    101
    python
    


```python
a=10.0  # float
print(a)
```

    10.0
    


```python
s="python"
print(s)
```

    python
    


```python
s=True
print(s)
```

    True
    


```python
s=False
print (s)
print(True)
```

    False
    True
    


```python
x=233
y=337
z=2
a=233798
b=88


# Garbage collector
# REFERENCE SCHEMENTICS
```

### TODO: add an interpreter schema here.



```python
import sys
print(sys.getrefcount(x))
```

#### Assignment Operator
It always works frol Right hand side to Left hand side



```python
x=10
print(x)
```

    10
    


```python
a=10
a=a+10+30
print(a)
```

    50
    


```python
a=30
b=10
a=b+20+a+40
print(a)
print(a*10)
```

    100
    1000
    


```python
a=b=c=10 
print(a)
print(b)
print(c) #shift + enter
```

    10
    10
    10
    

## Type operator
It returnes the type of a variable



```python
a=100
print(type(a))
```

    <class 'int'>
    


```python
j=10.00
print (type (j))
```

    <class 'float'>
    


```python
s="python"
print (type(s))
```

    <class 'str'>
    


```python
s1='pyth'
print(type(s1))
```

    <class 'str'>
    


```python
x= True
print (type(x))

y= False
print (type(y))
```

    <class 'bool'>
    <class 'bool'>
    


```python
k='10'
print (type(k))
print (k)
```

    <class 'str'>
    10
    


```python
a='a123'
type(a)
```




    str




```python
boo2= "False"
print (type(boo2))
```

    <class 'str'>
    


```python
s=123a
print(s)
```


      File "<ipython-input-112-d27a2d210b80>", line 1
        s=123a
             ^
    SyntaxError: invalid syntax
    


### ID Operator
Returns the address of a variable


```python
a=10
print (id(a))
```

    140726194026560
    


```python
b=10
print (id(b))
```

    140726194026560
    


```python
c=11
print (id(c))
```

    140726194026592
    


```python
k=10
print (id(k))
```

    140726194026560
    


```python
a=10
b=10.0
c=int(b)
print (id(a))
print (id(c))
print (id(b))
```

    140726194026560
    140726194026560
    2665414213744
    

## IS Operator
Is operator-- If id is same for 2 variable it will return the true othewise false



```python
a=10
print (id(a))
b=10
print (id(b))
print (a is b)
```

    140726194026560
    140726194026560
    True
    


```python
a=10
b=10.0
print (id(b))
print (a is int(b))
```

    2665414215440
    True
    


```python
a=b
print (id(a))
print (id(b))
```

    2665414215440
    2665414215440
    


```python
i=10
print (id(i))
j=11
print (id(j))
print (i is j)
```

    140726194026560
    140726194026592
    False
    


```python
l=10
k=10.0
m='10'
print (l is k)
print (l is m)
```

    False
    False
    


```python
p="python"
q="Python"
r="python"
print (p is q)
print (p is r)
```

    False
    True
    


```python
import sys
s="python"
s1="python"
s3="python"
s4="python"
s5="python"
sys.getrefcount(s)
```

### == Operator
== operator - numeric values are same or not



```python
i=10
j=10
print (i==j)
```

    True
    


```python
i=10
j=10.0
print ("Comparison operator ",i==j)
print ("IS operator", i is j)
```

    Comparison operator  True
    IS operator False
    


```python
i=10
j=10.1
print (i==j)
```

    False
    


```python
i='10'
j=10
print (i==j)
```

    False
    


```python
s1="python"
s2="Python" # case sensitive
s3="Python" # case sensitive
print (s1 == s2)
print (s3 == s2)
```

    False
    True
    

### Swapping values of 2  Variable

a=40
b=50

after execution
a=50
b=40




```python
a=50
b=100
a=b
b=a
# b=a
print(a,b)

```


```python
a= 110 
b=50
c=a
d=b
b=c
a=d
print(a)
print(b)
```


```python
a=40
b=50
print(a=b)

```

##### Write a program to swap values of a and b
So after execution of program a should be 20
and b =10


```python
a=10
b=20
c=a # c=10
a=b  # a=20
b=c  # b=10
print(a)
print(b)# this is to explain the swapping
```

    20
    10
    


```python
a=id(b)
a
```

With out using 3rd variable


```python
a=100
b=200
a=a+b    # a=100+200=300
b=a-b    # b=300-200=100
a=a-b    # a= 300-100=200
print("value of a :",a)
print("Value of b : ",b)
```


```python
print(xyx)
xyx=10
```

### Comma operator


```python
print("python learning")
```

    python learning
    


```python
a=100
print("Value of a is  ",a)
```

    Value of a is   100
    


```python
a,b=10,200
print("value of a ",a)
print ("value of b ",b)
```

    value of a  10
    value of b  200
    


```python
a,b,c=10,20,100
print("value of a ",a)
print ("value of b", b)
print ("value of c", c)
```

    value of a  10
    value of b 20
    value of c 100
    

#### Swapping values again


```python
a=10.0
b=33
a,b = b,a  # a,b = 33,10.0
print("value of a ",a)
print ("value of b", b)# ========
```

    value of a  33
    value of b 10.0
    

## Plus operator
![Interpeter](plusoperator.png)



```python
print (10+20)
```

    30
    


```python
print (10+20.0)
```

    30.0
    


```python
print (10.0+20.0)
```

    30.0
    


```python
print ("Python"+" Scala")
```

    Python Scala
    


```python
print ("Python"+10)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-139-4f0588bb35e9> in <module>
    ----> 1 print ("Python"+10)
    

    TypeError: can only concatenate str (not "int") to str



```python
print ("Python"+"10")
```

    Python10
    

## Multiplication operator
![Interpeter](multiplication.png)



```python
print (10*20)
```

    200
    


```python
print (10*20.0)
```

    200.0
    


```python
print (10.0*20.0)
```

    200.0
    


```python
print ("python "*5)
```

    python python python python python 
    


```python
print (5*"python ")
```

    python python python python python 
    


```python
print ('5'*"python")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-146-6d1a03bcf76d> in <module>
    ----> 1 print ('5'*"python")
    

    TypeError: can't multiply sequence by non-int of type 'str'


### Modulus operator %
Gives the reminder
![Interpeter](01_Division.gif)




```python
# print (4%4)
5/4
```


```python
5%4
```




    1




```python
10%3
```




    1




```python
3%10   # if dividend is smaller than divisor than dividend will be reminder
```




    3




```python
3333%1000000

```




    3333



### Power **


```python
a=10
b=3
print (a**b)
```

    1000
    


```python
print (2**3)
```

    8
    

#### Absolute function
returns absolute value of a number( convert to positive value)
abs(x)



```python
print( abs (+10-30))
print (abs (-10000))
print (abs(10)) 
print (abs(-10+30))
```

    20
    10000
    10
    20
    

### Formatted Output
* %d for integer
* %s for strings
* %r for raw
* %f for float


```python
print ("python" + " scala")
```

    python scala
    


```python
st="python"
st1="java"
s="   "
```


```python
print (st + "    " +st1)
```

    python    java
    


```python
print (st + st1)
```

    pythonjava
    


```python
st="python"
print ("Directory changed successfully " +st + " to the home directory")
```

    Directory changed successfully python to the home directory
    


```python
st="python"
st1="java"
print ("Directory changed successfully %s" %st1)
print ("Directory changed successfully %s" %st)
```

    Directory changed successfully java
    Directory changed successfully python
    


```python
print ("Directory changed successfully to %s" %"java python")
```

    Directory changed successfully to java python
    


```python
s="learning"
print ("%s" %"java python")
print ("%s" %s)
```

    java python
    learning
    


```python
st="python"
st1="java"
print ("Directory %s changed successfully to %s " %(st1,st))
```

    Directory java changed successfully to python 
    


```python
print ("Directory changed %d successfully" %(100))
```

    Directory changed 100 successfully
    


```python
st=100
st1="java"
print ("Directory %d changed successfully %s " %(st,st1))
print ("Directory %d changed successfully %s ")
# print ("Directory %s changed successfully %s " %(st,st1))
```

    Directory 100 changed successfully java 
    Directory %d changed successfully %s 
    


```python
print ("Directory changed %f successfully" % 100.000000)
```

    Directory changed 100.000000 successfully
    


```python
a=10.6 # sdfsdfsa
b=20
c=200
print ("a is  %s and b is %d" %(a,b))
print ("b is  %f and a is %d" %(b,a))
```

    a is  10.6 and b is 20
    b is  20.000000 and a is 10
    


```python
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the months: %s" % months)
```

    Here are the months: 
    Jan
    Feb
    Mar
    Apr
    May
    Jun
    Jul
    Aug
    


```python
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the months: %r" % months)
```

    Here are the months: '\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
    


```python
VAL = "A"# 65
print("The ASCII value of '" + VAL + "' is", ord(VAL))
```


```python
val = "a"
print("The ASCII value of '" + val + "' is", ord(val))
```


```python
print (chr(65))
print (chr(97))
```


```python
print(bin(173) )
```

### Assignments
1. How a C program compiled
2. C program memory structure
3. How to swap 2 variables( apart from , and +/- operator)
4. Create GIT account


```python
print('"'"vfvf"'"')
```


```python
print("hello")
```


```python
# Start with 1, discard 2 and move to 3 and discard 4 and move to 5 discard 6 
# . Keep going on till 100 in a circular way until you left with 1 number at last
l=[1,2,3,4,5]
l2=l[::-1]
while len(l2)>1:
    del l2[len(l2)%2::2]
    print(l2)
print(l2)

# while         
    
```


```python
import ctypes
my_var = 10
my_var1 = 10
my_var_address = id(my_var)
ctypes.c_long.from_address(my_var_address).value
```


```python
arr=[1,2,3,4,5]
s_arr=[]
while (s_arr.length==1):
    i=0
    while (i<arr.length):
        s_arr.push(arr[i])
        i+=2
        arr=s_arr.reverse
  s_arr=arr 
print(arr)
```


```python
arr=[1,2,3,4,5]
s_arr=[]
until s_arr.length == 1
  s_arr = []
  i=0
  while i < arr.length
    s_arr.push(arr[i])
    i+=2
  arr=s_arr.reverse
print (arr)
```


```python
arr=[1,2,3,4,5]
s_arr=[]
i=0
while i < len(arr):
    s_arr.append(arr[i])
    i+=2
print (s_arr)
```


```python
l=[1,2,3]
len(l)
```


```python

```
