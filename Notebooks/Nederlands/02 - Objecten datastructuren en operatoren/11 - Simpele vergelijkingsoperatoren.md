<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Vergelijkingsoperatoren

In deze lezing zullen we leren over de vergelijkingsoperatoren (Comparison Operators) in Python. Met deze operatoren kunnen we variabelen vergelijken en een Booleaanse waarde (True of False) uitvoeren.

Als je enige achtergrond in wiskunde hebt, zouden deze operators heel eenvoudig moeten zijn.

We zullen eerst een tabel met vergelijkingsoperatoren presenteren en daarna enkele voorbeelden doornemen:

<h2> Tabel met vergelijkingsoperatoren </h2><p> In de onderstaande tabel, a=3 en b=4.</p>

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Beschrijving</th><th>Voorbeeld</th>
</tr>
<tr>
<td>==</td>
<td>Als de waarden van twee operanden gelijk zijn, wordt de voorwaarde waar.</td>
<td> (a == b) is niet waar.</td>
</tr>
<tr>
<td>!=</td>
<td>Als de waarden van twee operanden niet gelijk zijn, wordt de voorwaarde waar.</td>
<td>(a != b) is waar</td>
</tr>
<tr>
<td>&gt;</td>
<td>Als de waarde van de linker operand groter is dan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &gt; b) is niet waar.</td>
</tr>
<tr>
<td>&lt;</td>
<td>Als de waarde van de linker operand kleiner is dan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &lt; b) is waar.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>Als de waarde van de linker operand groter is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &gt;= b) is niet waar. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>Als de waarde van de linker operand kleiner is dan of gelijk is aan de waarde van de rechter operand, wordt de voorwaarde waar.</td>
<td> (a &lt;= b) is waar. </td>
</tr>
</table>

Laten we nu snelle voorbeelden van elk van deze doornemen.

#### Gelijk


```python
2 == 2
```




    True




```python
1 == 0
```




    False



Merk op dat <code>==</code> (dubbele gelijk symbolen) een <em>vergelijkings</em>-operator is, terwijl <code>=</code> (enkel gelijk symbol) een <em>toewijzings</em>-operator is.

#### Niet gelijk


```python
2 != 1
```




    True




```python
2 != 2
```




    False



#### Groter dan


```python
2 > 1
```




    True




```python
2 > 4
```




    False



#### Kleiner dan


```python
2 < 4
```




    True




```python
2 < 1
```




    False



#### Groter dan of gelijk aan


```python
2 >= 2
```




    True




```python
2 >= 1
```




    True



#### Kleiner dan of gelijk aan


```python
2 <= 2
```




    True




```python
2 <= 4
```




    True



**Geweldig! Overloop elke vergelijkingsoperator om er zeker van te zijn dat u begrijpt wat elke operator zegt. Maar hopelijk was dit duidelijk voor u.**

Vervolgens behandelen we geketende (chained) vergelijkingsoperatoren
