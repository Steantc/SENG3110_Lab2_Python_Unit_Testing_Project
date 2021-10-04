import unittest
import cuboid

class ciuboidTest(unittest.TestCase):

    #passing test
    def test_volume1(self):
        assert(cuboid.volume(21,15,10) == 3150.00)
    
    #failing tests
    def test_volume2(self):
        assert(cuboid.volume(21,15,10) == 3150.00001)

    def test_volume3(self):
        assert(cuboid.volume(10,1000,100) == 0)


if __name__ == '__main__':
    unittest.main()