# Code Scope - Bereikbaarheid


```python
# Global scope

a = 1


def f():
    print("Inside method f(), a is {}".format(a))


def g():
    a = 2
    print("Inside method g(), a is {}".format(a))


def h():
    global a
    a = 3
    print("Inside method h(), a is {}".format(a))


# Zonder code uit te voeren probeer om te inschatten wat de volgende instructies gaan afdrukken.
print("Global a is now {}".format(a))
f()
print("Global a is now {}".format(a))
g()
print("Global a is now {}".format(a))
h()
print("Global a is now {}".format(a))






```

    Global a is now 1
    Inside method f(), a is 1
    Global a is now 1
    Inside method g(), a is 2
    Global a is now 1
    Inside method h(), a is 3
    Global a is now 3
    
