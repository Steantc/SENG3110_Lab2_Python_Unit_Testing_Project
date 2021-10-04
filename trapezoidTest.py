import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #passing test
    def test_area1(self):
        assert(trapezoid.area(26,20,15) == 345.00)
    
    #failing tests
    def test_area2(self):
        assert(trapezoid.area(26,20,15) == 345.000001)

    def test_area3(self):
        assert(trapezoid.area(26,20,15) == 0)


if __name__ == '__main__':
    unittest.main()