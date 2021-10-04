import unittest
import triangle

class triangleTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(triangle.area(11,15,18,22) == 82.32)
    
    #failing test
    def test_area2(self):
        assert(triangle.area(11,15,18,22) == 82.3164625090267)
    
    def test_area3(self):
        assert(triangle.area(11,15,18,22) == 0)


if __name__ == '__main__':
    unittest.main()