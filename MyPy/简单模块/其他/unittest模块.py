import unittest

def fun(a, b):
    return a.update(b)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual({'a', 'b', 'c', 'd'}, fun({'a', 'b'}, {'c', 'd'}))
unittest.main()