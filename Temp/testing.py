import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("setup method execution")
    def test(Self):
        print("test method execution")
    def tearDown(self):
        print("teardown method execution ")
unittest.main()
print()
    

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("setup method execution")
    def test_method1(Self):
        print("test_method1 execution")
    def test_method2(self):
        print("test_method2 execution")
    def tearDown(self):
        print("tesrdown methos execution")
unittest.main()
print()



class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class method execution")
    def setUp(self):
        print("setup method execution")
    def test_method1(self):
        print("test_method1 execution")
    def test_method2(self):
        print("test_method2 execution")
    def tearDown(self):
        print("teardown method execution")
    @classmethod
    def tearDownClass(cls):
        print("teardown class method execution")   
unittest.main()
print()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        