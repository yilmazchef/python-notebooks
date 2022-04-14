<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Object Oriented Programming
## Homework Assignment

#### Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


```python
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
```


```python
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
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)
```


```python
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


