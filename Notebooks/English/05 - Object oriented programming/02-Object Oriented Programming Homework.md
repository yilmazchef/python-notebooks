<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python course materials</em>
</center>

# Object Oriented Programming
## Homework Assignment

#### Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


```python
class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass
```


```python
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
```


```python
li.distance()
```




    9.433981132056603




```python
li.slope()
```




    1.6



________
#### Problem 2

Fill in the class 


```python
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass
```


```python
# EXAMPLE OUTPUT
c = Cylinder(2,3)
```


```python
c.volume()
```




    56.52




```python
c.surface_area()
```




    94.2


