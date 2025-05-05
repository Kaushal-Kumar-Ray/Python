import unittest
def add (x,y):
    return x+y          #  + - * / 
class Fortest(unittest.TestCase):
    def test_sdd(self):
        self.assertEqual(add(2,3),5)
unittest.main()

"""
assertEqual()
assertNotEqual()
assertTrue()
assertFalse()         
"""