<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Object georiënteerd programmeren
## Huiswerkopdracht

#### Probleem 1
Vul de methoden van de klasse Line in om coördinaten als een paar tupels te accepteren en de helling (slope) en afstand (distance) van de lijn te retourneren.


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
# EEN VOORBEELD SCENARIO OM UIT TE VOEREN

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
#### Probleem 2

Vul de klas in


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
# EEN VOORBEELD SCENARIO OM UIT TE VOEREN

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


