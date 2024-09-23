import unittest

class test_add_integer(unittest.TestCase):
    """ test class """
    def test_add(self):
        self.assertEqual(add_integer(2, 3), 5)