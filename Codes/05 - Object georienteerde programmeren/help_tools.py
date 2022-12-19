class MyClass():
    def __init__(self, x, y, z): # x, y, z zijn argumenten van __init__() methode
        self.a = x # a is een attribuut van MyClass
        self.b = y # b is een attribuut van MyClass
        self.c = z # c is een attribuut van MyClass
        self.d = 10 # d is een attribuut van MyClass
    
    def m1(self):
        print("M1 is called..")
        
    def m2(self):
        print("M2 is called..")
        
        
c1 = MyClass(10, 20, 30)

print(c1.a)
print(c1.d)

c1.m1()
c1.m2()

