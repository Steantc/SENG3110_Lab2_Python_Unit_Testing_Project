import unittest
import cube

class cubeTest(unittest.TestCase):

    #passing test
    def test_volume1(self):
        assert(cube.volume(7) == 343.00)
    
    #failing tests
    def test_volume2(self):
        assert(cube.volume(7) == 343.001)

    def test_volume3(self):
        assert(cube.volume(7) == 0)


if __name__ == '__main__':
    unittest.main()