import unittest
import equilateral

class equilateralTest(unittest.TestCase):

    #passing test
    def test_area1(self):
        assert(equilateral.area(6) == 15.59)
    
    #failing tests
    def test_area2(self):
        assert(equilateral.area(6) == 15.588457268119894)

    def test_area3(self):
        assert(equilateral.area(6) == 0)


if __name__ == '__main__':
    unittest.main()